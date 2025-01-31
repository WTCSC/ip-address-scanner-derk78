import ipaddress
import subprocess
import time 
import argparse
import sys

def validate_cidr(cidr):
    
    #`ipaddress.ip_network` is used to parse the cidr string and verify that it is in the valid cidr notation.
    #If it is the right notation then `network` will hold it if not network will be "None"
    try:
        return ipaddress.ip_network(cidr, strict=False)
    except ValueError:
        return None
    

def ping_host(ip):

    #Use the time module to get the exact time when we ping the host
    start_time = time.time()

    #Since the ping command works differently on Windows and Linux if the system is Windows then go with the first option or we know it's Linux and go with the second option.
    if sys.platform == "win32":

        #'ping' is the actual command we want to run and '-n' is the amount of packets we want to send which is '1' and then '-w' is the timeout which is '1000' miliseconds.
        command = ['ping', '-n', '1', '-w', '1000', str(ip)]
    else:
        #Samething here just with slightly different parameters because it is Linux.
        command = ['ping', '-c', '1', '-W', '1', str(ip)]

    #Here is where we run the ping command we came up with using the `subprocess.run` command to run a shell command in Python and also captures the output and return status.
    result = subprocess.run(command, capture_output=True, text=True)

    #Get the reponse time of the ping request by taking the time after the ping finished and subtracting it from the time before the ping request and then multiple it by 1000 to get the milliseconds and round it 2 decimal places.
    response_time = round((time.time() - start_time) * 1000, 2)

    #For these if statements if the result is 0 then we know the IP is UP, if we have a standard error then we return the standard error we got and strip any unnecessary information.
    #Finally if the standard result has something like timed out in it then we know it is down and without giving us all the extra information if the standard output says 
    #"requested timed out" or "timed out" then we return "DOWN" plus 'No response".
    if result.returncode == 0:
        return "UP", response_time
    elif result.stderr:
        return "ERROR", result.stderr.strip()
    else:
        stdoutresult = result.stdout.lower()
        if "request timed out" in stdoutresult or "timed out" in stdoutresult:
            return "DOWN", "No response"
            

def scan_network(cidr):

    #Checks if the input string has the right CIDR notation using our validate_cidr function
    #If network is "None" then it will tell you that it is not in valid CIDR notation and exit. 

    network = validate_cidr(cidr)
    if not network:
        print(f"Error: '{cidr}' is not a valid CIDR notation.")
        sys.exit(1)

    #Prompt the user that the specified network is being scanned.
    print(f"Scanning network {cidr}...\n")

    #Create the counters for the number of "UPs", "DOWNs", and "ERRORs" we will get.
    up_count = 0 
    down_count = 0 
    error_count = 0 

    #Use a for loop to go through all the IPs in the range in the range and use the `ping_host()` function on them.
    #Also have two variables for the status of the IP and the extra info that we specified earlier such as the response time or any errors.
    #Then use if statements to print what we want for each of the cases.
    for host in network.hosts():
        status, info = ping_host(str(host))
        if status == "UP":
            print(f"{host} - UP ({info}ms)")
            up_count += 1 
        elif status == "DOWN":
            print(f"{host} - DOWN ({info})")
            down_count += 1
        elif status == "ERROR":
            print(f"{host} - ERROR ({info})")
            error_count += 1 

    #Once the scan is complete tell the end user and give the number of hosts that were "DOWN", "UP", and how many "ERRORs" there were.
    print(f"\nScan complete. Found {up_count} active hosts, {down_count} down, {error_count} errors")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scan IP addresses within a CIDR range.")
    parser.add_argument("cidr", help="The CIDR notation of the network to scan")
    args = parser.parse_args()
    scan_network(args.cidr)