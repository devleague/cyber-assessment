# origin (new port each connection) = user machine that attempted scan
# destination (has reserved port) = machine that user attempted to scan

# import ssh.log
with open('./devleague_discovery/ssh.log.txt', 'r') as file:

  # all lines
  all_lines = file.readlines()

  # scan count
  scan_count = len(all_lines)

  # create scanners_found.txt if doesnt exist in append
  scanners_found = open('scanners_found.txt', 'a+')

  # write scan attempts
  scanners_found.write('[scan attempts] ')
  scanners_found.write(str(scan_count) + '\n\n')

  # scan origin hosts - header
  scanners_found.write('[scan origin hosts]\n')

  # write all origin ip
  for line in all_lines:
    # split line values into list
    line_col_value = line.split()
    # print('SCAN LIST', line_col_value)

    # origin ip
    scan_origin = line_col_value[2]
    # print('ORIGIN', scan_origin)
    scanners_found.write('\t' + scan_origin + '\n')

    # questionable ips
    # print('LENGTH', len(scan_origin))
    if(len(scan_origin) > 15):
      print('WHO DIS?!', scan_origin)

  # scan destination hosts - header
  scanners_found.write('[scan destination hosts]\n')  

  # write all destination ips
  for line in all_lines:

    # destination ip
    scan_destination = line_col_value[4]
    # print('DESTINATION', scan_destination + '\n')
    scanners_found.write('\t' + scan_destination + '\n')

  scanners_found.close()