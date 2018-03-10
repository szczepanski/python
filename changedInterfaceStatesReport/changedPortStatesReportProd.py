#!/usr/bin/env python


import re
import pickle
import sys
import json
import connection_handler


# static variables

# Declare global variables parsed in from the py command
BIN_LOCATION = "/apps/Networks/AutomationFiles/net_18.bin"
try:
    INPUT_JSON = json.loads(sys.argv[1])
    MODE = INPUT_JSON["mode"]
    HOSTNAME = INPUT_JSON["hostname"]
    IP_ADDRESS = INPUT_JSON["ipAddress"]
except (IndexError, TypeError, KeyError) as e:
    print(json.dumps(
        {"status": 1,
         "output": "Failed to load input JSON. Error: {0}".format(e)}))
    quit(1)


# main
def main():
    """"""
    # declare function variables

    # read existing bin file or create blank dictionary
    try:
        with open(BIN_LOCATION, "rb") as f:
            net_18 = pickle.load(f)
    except IOError:
        net_18 = {}

    interfaces_changed = {}

    # regex to capture int name and protocol status only
    port_regex = re.compile(
        r"(?P<name>^\S+\d).+(?P<state>(up)|(down))$",
        re.MULTILINE | re.IGNORECASE)
    # run py connection handler and command output
    connection = connection_handler.SSHHandler(
        IP_ADDRESS, ["show ip interface brief"], "e")
    connection.shell()
    if connection.out_json["status"] != 200:
        print(json.dumps(
            {"status": 1,
             "output": "Failed to login to the device. Error: {0}".format(
                 connection.out_json["output"])}))
        quit(1)
    output = connection.out_json["output"]

    # Create new baseline
    if MODE == 0:
        if port_regex.search(output):
            net_18[HOSTNAME] = {}
            # populate blank net_18 dictionary
            for match in port_regex.finditer(output):
                interface_name = match.groupdict()["name"]
                interface_state = match.groupdict()["state"].lower
                net_18[HOSTNAME][interface_name] = interface_state
        else:
            print(json.dumps(
                {"status": 1,
                 "output": "Failed to retrieve interfaces. Error: {0}".format(
                     output)}))
            quit(1)
        # dump populated net_18 dictionary as bin file
        with open(BIN_LOCATION, "wb") as f:
            pickle.dump(net_18, f)
        print(json.dumps(
            {"status": 0,
             "output": net_18[HOSTNAME]}))

    # Compare current reading with baseline
    if MODE == 1:
        if HOSTNAME in net_18:  # check for host in baseline
            if port_regex.search(output):  # verify if current output contains interface information
                for match in port_regex.finditer(output):
                    interface_name = match.groupdict()["name"]  # current interface name
                    interface_state = match.groupdict()["state"].lower  # current status
                    if interface_name in net_18[HOSTNAME]: # if current int found in baseline
                        if interface_state != net_18[HOSTNAME][interface_name]:
                            interfaces_changed[interface_name] = (
                                net_18[HOSTNAME][interface_name],
                                interface_state)
                    else:
                        print(json.dumps(
                            {"status": 1,
                             "output": "Interface {0} not found in baseline".format(
                                 interface_name)}))
                        quit(1)
                print(json.dumps(
                            {"status": 0,
                             "output": interfaces_changed}))
            else:
                print(json.dumps(
                    {"status": 1,
                     "output": "Failed to retrieve interfaces. Error: {0}".format(
                         output)}))
                quit(1)
        else:
            print(json.dumps(
                {"status": 1,
                 "output": "{0} not found in baseline dictionary.".format(
                     HOSTNAME)}))
            quit(1)


if __name__ == "__main__":
    main()
