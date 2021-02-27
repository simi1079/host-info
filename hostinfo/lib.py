from .exceptions import InvalidIP, InvalidHostname


def usage():
    """
    Displays a usage message
    parameters: none
    """

    how_to_use = """
Usage:
    hostfile [-args]

arguments:
    # -h: To display help
    # -r <search_string>: display a list of hosts matching the search_string or all hosts otherwise
    # -w <IP> <Host>: write the supplied IP address and Hostname into the hostfile.txt

interactive:
    # -i: to run the program in the interactive mode
"""

    print(how_to_use)


def show_menu():
    """
    Display menu options in interactive mode
    parameters: none
    """

    print("1. Read & search hosts file")
    print("2. Update hosts file")
    print("3. Quit")


def get_hostinput(prompt_msg: str = ""):
    """
    Purpose: prompt for input (example: prompt for IP address); used anytime user input is required.
    parameters: prompt (example: “Enter IP address: “)
    return: user input (example: IP address)
    """
    input(prompt_msg)


def is_dns_name(hostname: str):
    """is_dns_name(hostname: str)

    Purpose: validate hostname
    Parameters: hostname
    return: True/False Function
    body: 
        Verify that the hostname is not an empty string.
        Note: By setting up a function dedicated to hostname validation we can refine our hostname
            validation at a later date without touching the main program code.
    """
    if not hostname:
        return False
    elif len(hostname.split(".")) == 1:
        return False

    return True


def is_ip_octet(octet: int):
    """isipoctet(ip: str)

    Purpose: validate IP octet
    Parameters: octet
    return: True/False
    body:
        return True if the octet is a digit in the range between 0 and 255,
        False otherwise.
    """
    if not octet in range(0, 256):
        return False

    return True


def is_ip(ip_addr: str):
    """is_ip(ip_addr: str)

    Purpose: validate IP address
    Parameters: IP address
    return: True/False
    body:
        Verify that the IP address has 4 octets. Note: You may find split() helpful.
        Validate each octet by calling the isipoctet function.
        If any one octet is invalid the entire IP address invalid.
    """
    octets = ip_addr.split(".")
    if not len(octets) == 4:
        return False

    for octet in octets:
        if not is_ip_octet(octet=int(octet)):
            return False

    return True


def search_hosts(file, query_str: str = ""):
    """search_hosts(file, query_str: str = "")

    Purpose: display matching hosts in host file 
    Parameters: optional search string
    Note: We will set up the empty string as the default value for the function
    parameter - the search string - in the function definition header line. 
        Syntax: def func_name(file, query_str: str = ""="")
    """
    with open(file, mode="r") as reader:
        query_str_exists = False

        if not query_str:
            print(reader.read())
            return

        for line in reader:
            if query_str in line:
                query_str_exists = True
                print(line)

        if not query_str_exists:
            print(reader.read())


def update_host(file_path: str, ip_addr: str, hostname: str):
    """update_host(file: str, ip_addr: str, hostname: str)

    Purpose: write host information to hosts file
    Parameters: IP address, hostname
    Body: 
        open file in append mode
        Update hosts file 
    """
    if not is_ip(ip_addr):
        raise InvalidIP(f"'{ip_addr}': is not a valid IP address")
    elif not is_dns_name(hostname):
        raise InvalidHostname(f"'{hostname}' is not a valid hostname")

    with open(file_path, mode="a") as writer:
        new_line = ip_addr + " " + hostname
        writer.write(new_line)
