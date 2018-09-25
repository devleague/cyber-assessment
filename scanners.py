# import ssh.log
with open('./devleague_discovery/ssh.log.txt', 'r') as file:

  # all lines
  all_lines = file.readlines()

  # scan count
  scan_count = len(all_lines)
  scanners_found = open('scanners_found.txt', 'a+')
  scanners_found.write('[scan attempts] ')
  scanners_found.write(str(scan_count) + '\n\n')

  # scan origin hosts
  scanners_found.write('[scan origin hosts]\n')
  scanners_found.write('\txxx.xxx.x.xx')
  scanners_found.close()

  for i, lines in enumerate(all_lines):
    scan_number = i
    each_line = all_lines[i]

    print('EACH LINE', each_line)
  
    # found_scans = open('scanners_found.txt', 'a+')
    # found_scans.write(each_line)
  



  # print(len(all_lines))
  # print(all_lines, 'ALL LINES')

  # print(len(data))
  
  # for i, scan in enumerate(data):
  #   print(data[i])

  # with open('scanners_found.txt', 'r+') as f:
  #   scanner_data = f.read()
  #   print()
  #   for line in scanner_data:
  #     print('LINE', line)


# print ssh_log
# print(data)
