```python
#.format explicit for ver 3.6 only 
#for ealier versions use standard %s or %d placeholders
>>> import re
>>> text = """Router# show ip interface brief
Interface             IP-Address      OK?    Method Status     	Protocol
GigabitEthernet0/1    unassigned      YES    unset  up         	up
GigabitEthernet0/2    192.168.190.235 YES    unset  up         	up
TenGigabitEthernet2/1 unassigned      YES    unset  up         	up
Te36/46               unassigned      YES    unset  down       	down
Te36/47               unassigned      YES    unset  down       	down
Te36/48               unassigned      YES    unset  down       	down
Virtual36             unassigned      YES    unset  up         	up
The following table describes the significant fields shown in the display."""

>>> reg = re.compile(r"(?P<name>^\S+\d).+(?P<state>(up)|(down)$)", re.MULTILINE | re.IGNORECASE)
>>> matches = reg.finditer(text)
>>> for m in matches:
	print("Interface Name: {}\nInterface State: {}".format(m.groupdict()["name"], m.groupdict()["state"]))

	
Interface Name: GigabitEthernet0/1
Interface State: up
Interface Name: GigabitEthernet0/2
Interface State: up
Interface Name: TenGigabitEthernet2/1
Interface State: up
Interface Name: Te36/46
Interface State: down
Interface Name: Te36/47
Interface State: down
Interface Name: Te36/48
Interface State: down
Interface Name: Virtual36
Interface State: up
```
