import re

# dictionary comprehension example

output = """
GigabitEthernetOne    192.168.190.1
GigabitEthernetTwo    192.168.190.2  
GigabitEthernetThree  192.168.190.3
"""

port_regex = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
if port_regex.search(output):
    d = {key: value for key, value in zip(("port1", "port2", "port3"), port_regex.findall(output))}
print(d)

# unpacking example

a, b = [0, 1]
print(a, b)


# args use sample:


def sample_function(requiredVariables, *anyNumerOfVariables):
    for value in anyNumerOfVariables:
        print(value),
    print(requiredVariables)


sample_function("Piotr!", "Learn", "py", "hard")


# kwargs


def k(**kwargs):
    for key in kwargs:
        print key, ":", kwargs


k(name="kevin", surname="mups", job="bs")


def k(**kwargs):
    for key in kwargs:
        print key, ":", kwargs[key]


k(name="kevin", surname="mups", job="bs")

