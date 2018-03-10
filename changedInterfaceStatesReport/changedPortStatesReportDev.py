#!/usr/bin/env python
# py 2.x

# python command to be run on ipmon : ### python net_18.py '{'mode': 0, 'hostname': 'test.ho'}' ###


# global
import re
import pickle  # binaries
import sys  # used here to capture parsed in variables - JSON
import json

int_state_current = {}

# global variables:
bin_location = "net_18.bin"

# regex to capture int name and protocol status only
regex_int_prot_state = re.compile(r"(?P<name>^\S+\d).+(?P<state>(up)|(down))\s+((up)|(down)$)", re.MULTILINE | re.IGNORECASE)

comm1_out = """Router# show ip interface brief
Interface             IP-Address      OK?    Method Status     	Protocol
GigabitEthernet0/1    unassigned      YES    unset  up         	down
GigabitEthernet0/2    192.168.190.235 YES    unset  DOWN         	up
TenGigabitEthernet2/1 unassigned      YES    unset  up          down
Te36/46               unassigned      YES    unset  down       	up
Virtual36             unassigned      YES    unset  up         	up
The following table describes the significant fields shown in the display."""


# Global functions

# verify input_json, load it and store variables
def load_input_json():
    # capture parsed in json from the command
    sys.argv.append('{"mode": 1, "hostname": "bbp-test-switch-2.ho", "ip_address": "10.10.10.20"}')
    try:
        input_json = json.loads(sys.argv[1])
        mode = input_json["mode"]
        hostname = input_json["hostname"]
        ip_address = input_json["ip_address"]
        return mode, hostname, ip_address
    except (IndexError, TypeError, KeyError):
        print(json.dumps({"status": 1, "output": "failed to load json input"}))
        quit(1)


# Define globally variables
mode, hostname, ip_address = load_input_json()


# check if the output contains interface information and get current reading
def get_int_state_current(regex):
    if regex.search(comm1_out):
        int_state_current[hostname] = {}
        for match in regex.finditer(comm1_out):
            interface = match.groupdict()["name"]
            state = match.groupdict()["state"]
            int_state_current[hostname][interface] = state
        return int_state_current
    else:
        exit(500)


# main
def main():

    # main variables
    int_state_base = {}  # base reading {host:int:status}
    int_state_changed = {}  # status change dict {int:base protocol state,current protocol state}
    int_state_current = get_int_state_current(regex_int_prot_state)  # current reading {host:int:status}
    int_state_current_short = int_state_current[hostname]  # current reading {int:status}

# mode 0 - get new baseline
    if mode == 0:  # get current reading create new baseline
        print 'Current reading dumped to :'
        print int_state_current
        with open(bin_location, "wb") as f:
            pickle.dump(int_state_current, f)

# mode 1 - check for changes in protocol status
    elif mode == 1:
        # compare baseline with current reading
        print "- int_state_current:"
        print int_state_current

        # get baseline
        try:
            with open(bin_location, "rb") as f:
                int_state_base = pickle.load(f)
                print "- int_state_base:"
                print int_state_base

                # compare base with current
                for k in int_state_current_short:
                    if k in int_state_base[hostname]:
                        if int_state_current_short[k] != int_state_base[hostname][k]:
                            int_state_changed[k] = int_state_base[hostname][k], int_state_current_short[k]
                        else:
                            "do nothing -same state"
                    else:
                        print "FAILURE"
                print 'int_state_changed: '
                print int_state_changed

        except IOError as e:
            # net_18 = {}
            print "Missing Baseline"
    return int_state_changed


if __name__ == "__main__":  # parse json if run via directly
    main()
