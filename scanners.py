row_count = 0 
source_ips = []
target_ips = []
mal_traffic = 0
mal_target_ip = []
mal_source_ip = []

input_file = open('data/ssh.log.txt')

for line in input_file:
  row_count = row_count + 1
  all_fields = line.split('\t')
  timestamp = all_fields[0]  
  uid = all_fields[1],
  source_ip = all_fields[2],
  source_port = all_fields[3],
  target_ip = all_fields[4],
  target_port = all_fields[5],
  status = all_fields[6],
  traffic_type = all_fields[7],
  host_agent = all_fields[8],
  
  if 'Nmap' in line:
    mal_traffic = mal_traffic + 1
    if source_ip not in mal_source_ip:
      mal_source_ip.append(source_ip)
    if target_ip not in mal_target_ip:  
      mal_target_ip.append(target_ip)

  if source_ip not in source_ips:
    source_ips.append(source_ip)
  
  if target_ip not in target_ips:
    target_ips.append(target_ip)
  
output_file = open('./data/scanners_found.txt', 'w')
output_file.write('Scan results\n\n')
output_file.write('Total records: ' + str(row_count) + '\n')
output_file = open('./data/scanners_found.txt', 'a')
output_file.write('\n\nSource IP addresses\n\n')
for ip in source_ips:
  output_file.write(str(ip) + '\n')
output_file = open('./data/scanners_found.txt', 'a')
output_file.write('\n\nTarget IP addresses\n\n')
for ip in target_ips:
  output_file.write(str(ip) + '\n')
output_file = open('./data/scanners_found.txt', 'a')
output_file.write('\n\nTotal malicious traffic\n\n')
output_file.write(str(mal_traffic) + '\n')
output_file.write('\n\nMalicious Attacked Target IP Address\n\n')
for ip in mal_target_ip:
    output_file.write(str(ip) + '\n')
output_file.write('\n\nMalicious Source IP Address\n\n')
for ip in mal_source_ip:
  output_file.write(str(ip) + '\n')




input_file.close()
output_file.close()