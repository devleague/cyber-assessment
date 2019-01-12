import os
import re
from zipfile import ZipFile

data_list = open('data/ssh.log.txt', 'r')

lineCount = 0
scanCount = 0
lineList = []
fromIP = []
toIP = []
filePaths = []

with data_list as reader:
  for line in reader:
    lineList.append(line)

for value in lineList:
  lineList[lineCount] = value.split()
  if len(lineList[lineCount]) > 4:
    scanCount += 1
    if not lineList[lineCount][2] in fromIP:
      fromIP.append(lineList[lineCount][2])
    if not lineList[lineCount][4] in toIP:
      toIP.append(lineList[lineCount][4])
  lineCount += 1

scanners = open('scanners.txt', 'w')
scanners.write('Scan log \n\n')
scanners.write('Scan attempts = ' + str(scanCount) + ' \n\n')

scanners.write('Scan Origin Hosts: \n\n')
for ip in fromIP:
  scanners.write(ip + "\n")

scanners.write('Scan Destination hosts: \n\n')
for ip in toIP:
  scanners.write(ip + "\n")

scanners.close()
print('Scan successful, scanners.txt created')

print('Files to be added to results.zip:')
for root, directories, files in os.walk('.'):
  for filename in files: 
    if filename == 'scanners.txt' or filename == 'ssh.log.txt' or filename == 'summary.txt':
      print(os.path.join(root, filename))
      filePaths.append(os.path.join(root, filename))


with ZipFile('report.zip','w') as zip: 
  for filepath in filePaths:
    zip.write(filepath)

print('All files zipped successfully')
