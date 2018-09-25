# import ssh.log
with open('./devleague_discovery/ssh.log.txt', 'r') as file:

  # all lines
  all_lines = file.readlines()
  for i, lines in enumerate(all_lines):
    scan_count = i

  print('SCAN COUNT', scan_count)
  
  # print(len(all_lines))
    # print('EACH LINE', all_lines[i])
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