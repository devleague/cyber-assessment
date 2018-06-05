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