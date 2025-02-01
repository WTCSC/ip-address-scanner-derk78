[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/cYbEVSqo)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=17937005)


# Python IP Scanner Script 

This is a Python script that is designed to scan all the hosts within a specified network range with CIDR notation which will then determine whether a host inside the range is `UP`, `DOWN`, or if an `ERROR` occured
## How to run it

- Make sure you have Python installed.
- Run it in the terminal by placing `python` or `python3` infront of the path of the file then place the network you want to scan with cidr notation of course (e.g. `python3 ip_scanner.py python ip_scanner.py 192.168.1.0/24`).
- In the event you need to run the script with elevated privileges on Linux/Mac use `sudo` at the beginning of the command `(sudo python3 ip_scanner.py`).

## Dependencies 

- Python
- Linux system 
- Windows system

Modules (although they should all be pre-installed with Python):

- **ipaddress**: To validate and parse CIDR notation.
- **subprocess**: For executing shell commands inside Python.
- **sys**: To exit out of the script incase of any errors.
- **time**: Used to measure the responses times for the IP addresses.
- **argparse**: Handling command line input.

## Error handling

- If the end user puts in the wrong CIDR notation they will recieve an error telling them it isn't in the proper CIDR Notation.

- If the ping command encounters an issue it will reserve the host as an error and return the error message associated with it.

- Incase a host doesn't respond to the ping in a set amount of time a message will appear telling the end user that there was no response or the host is unreachable.

## Why?

The reason I made this script is because Python one of the most used programming languages and probably the most beginner friendly coding language , and it can even be used cross-platform in the event you need a script that's interchangable on both Linux and Windows systems.

## Example usage

![alt text](image.png)