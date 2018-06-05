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

for line in source_file:
    line_count += 1
    some_content = []
    some_content = line.split('\t') # The format of the log file is split by tabs, in which we can use this to our advantage! We                                 # simply convert the line into a list, and we call on the appropriate index.

    inbound_ip += ['Line ' + str(line_count) + ': ' + some_content[2]]
    target_ip += ['Line ' + str(line_count) + ': ' + some_content[4]]



# The 'if' statement below will run tests on each index where an IP address 'should' be. If all tests fail to qualify that
# particular string as an IP, it is clear that we have some error. The entire line will be stored to the respective container, 
# and it will be saved to our file later. 

    if look_for_ip1(some_content[2]) == False and look_for_ip2(some_content[2]) == False and look_for_ip3(some_content[2]) == False and look_for_ip4(some_content[2]) == False: 
        inbound_malicious += ['Line ' + str(line_count) + ': ' + line]
        # print(line) #----- Uncomment this to see in command line.

# The 'elif' statement will run the same tests on index 4. All instances do occur with bad IPs on both index 2 and 4, but this is
# just for exhaustive purposes. Basically, this test is likely not to run because failed Ips are captured by the 'if' statement # first.

    elif look_for_ip1(some_content[4]) == False and look_for_ip2(some_content[4]) == False and look_for_ip3(some_content[4]) == False and look_for_ip4(some_content[4]) == False:
        target_malicious += ['Line ' + str(line_count) + ': ' + line]
        # print(line) #----- Uncomment this to see in command line.

# for x in inbound_ip: #----- Uncomment this to see in command line.
#     print(x) 
# for y in target_ip: #----- Uncomment this to see in command line.
#     print(x)



new_file = open('scanners_found.txt', 'a')
new_file.write(str(line_count) + ' Scans were performed.\n\n\nInbound IPs Adresses:\n')
for x in inbound_ip:   
    new_file.write(x + '\n')

new_file.write('\n\n\nTarget Ip Adresses:\n')
for y in target_ip:   
    new_file.write(y + '\n')

new_file.write('\n\n\nSuspected Malicious Activity:\n')
for x in inbound_malicious:
    new_file.write(x + '\n')

for y in target_malicious:
    new_file.write(y + '\n')

source_file.close()
new_file.close()

