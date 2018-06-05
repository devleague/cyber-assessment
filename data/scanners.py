def look_for_ip1(some_string):
    if not some_string[0:3].isdecimal():
        return False
    elif some_string[3] != '.':
        return False
    elif not some_string[4:7].isdecimal():
        return False
    elif some_string[7] != '.':
        return False
    elif not some_string[8:11].isdecimal():
        return False
    elif some_string[11] != '.':
        return False
    elif not some_string[12:15].isdecimal():
        return False
    else:
        return True

#The purpose of this function is to recognize IP addresses with this particular format.

def look_for_ip2(some_string):
	if not some_string[0:3].isdecimal():
		return False
	elif some_string[3] != '.':
		return False
	elif not some_string[4:7].isdecimal():
		return False
	elif some_string[7] != '.':
		return False
	elif not some_string[8:11].isdecimal():
		return False
	elif some_string[11] != '.':
		return False
	elif not some_string[12:14].isdecimal():
		return False
	else:
		return True

def look_for_ip3(some_string):
    if not some_string[0:3].isdecimal():
        return False
    elif some_string[3] != '.':
        return False
    elif not some_string[4:7].isdecimal():
        return False
    elif some_string[7] != '.':
	    return False
    elif not some_string[8:10].isdecimal():
        return False
    elif some_string[10] != '.':
        return False
    elif not some_string[11:14].isdecimal():
        return False
    else:
        return True

def look_for_ip4(some_string):
    if not some_string[0:3].isdecimal():
        return False
    elif some_string[3] != '.':
        return False
    elif not some_string[4:7].isdecimal():
	    return False
    elif some_string[7] != '.':
    	return False
    elif not some_string[8:10].isdecimal():
        return False
    elif some_string[10] != '.':
        return False
    elif not some_string[11:13].isdecimal():
        return False
    else:
        return True

# A total of (4) functions will be used to run tests on possible IP addresses. There are other variations, but this will be 
# sufficient for the file that needs to be read.


# The purpose of the functions above are to test the contents that will be saved. Basically, a 'for' loop below will place 
# indexed items into a list. They are indexed based on the format of the ssh.log.txt file, where index 2 & 4 display the inbound # and target IP addresses respectively.


source_file = open('ssh.log.txt', 'r')  # This is the file that will be scanned.
new_file = open('scanners_found.txt', 'w')  # This file will be used to store our results
new_file.close()


line_count = 0  
inbound_ip = [] # This container will hold inbound ip addresses.
target_ip = []  # Likewise, this one will hold the target ip addresses.
inbound_malicious = []  # After running the functions on every line at index 2, any contents that fail my tests will be placed                           # here. However, the whole line and its number will be saved, not just the suspect IP.
target_malicious = []   # This container will hold the same information, but for index 4. 


new_file = open('scanners_found.txt', 'a')

