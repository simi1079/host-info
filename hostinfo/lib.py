def usage():
    """
    Displays a usage message
    parameters: none
    return: none
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
    return: none
    """

    print("1. Read & search hosts file")
    print("2. Update hosts file")
    print("3. Quit")


def search_hosts(searchstr=""):
    if searchstr == "":
        file = open("/etc/hosts", "r")
    for searchstr in file:
        print(file.readlines(searchstr))
    else:
        print(file.read())
        file.close()


# cli = input("Select menu option [a, b, q]: ")


# CLI arguments: help option
# if cli[1] == '-h' or cli[1] == 'help':
# if cli == '-h' or cli == 'help':
#     print(usage)

# elif cli == 'a':
#     print(search_hosts())


def get_hostinput():
    """
    Purpose: prompt for input (example: prompt for IP address); used anytime user input is required.
    parameters: prompt (example: “Enter IP address: “)
    return: user input (example: IP address)
    """


def isdnsname():
    """
    Purpose: validate hostname
    Parameters: hostname
    return: True/False Function
    body: 
        Verify that the hostname is not an empty string.
        Note: By setting up a function dedicated to hostname validation we can refine our hostname
            validation at a later date without touching the main program code.
    """


def isipoctet():
    """
    Purpose: validate IP octet
    Parameters: octet
    return: True/False
    body: 
        return True if the octet is a digit in the range between 0 and 255;
        return False otherwise
        print appropriate error message if a requirement does not apply 
    """


def isip():
    """
    Purpose: validate IP address
    Parameters: IP address
    return: True/False
    body:  
        Verify that the IP address has 4 octets. Note: You may find split() helpful.
        Validate each octet by calling the isipoctet function.
        If any one octet is invalid the entire IP address invalid.
    """


def search_host():
    """
    Purpose: display matching hosts in host file 
    Parameters: optional search string
    Note: We will set up the empty string as the default value for the function
    parameter - the search string - in the function definition header line. 
        Syntax: def function(parameter="")
        Example: defsearch_hosts(searchstr="")
    """


def update_host():
    """
    Purpose: write host information to hosts file
    Parameters: IP address, hostname
    return: none
    Body: 
        open file in append mode
        Update hosts file 
    """
