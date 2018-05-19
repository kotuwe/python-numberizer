#
# Author: Lykov A.
# Python version: 3 and up 
#


import os
import sys
import binascii

sourceDir = './' # Here is files for replace strings
resultDir = './result' # Result dir with replaced strings 
fileExt = '.txt' # File extensoin for parse

def parseContent(content):
	path = resultDir + '\\' + file 
	fout = open(path, 'w', encoding='utf-8')
	idx = 1
	for line in content:
		#print(line)
		if len(line) > 0:
			fout.write(line.replace('_number', '_' + str(idx)))
			idx += 1
	fout.close()
	f.close()
	print('--> lines replaced: ' + str(idx - 1))

if int(sys.version[0]) != 3:
    print('Aborted: Python 3.x required. Please install Python 3 version: https://www.python.org/downloads/')
    sys.exit(1)

if not os.path.exists(resultDir):
	os.mkdir(resultDir)

files = os.listdir(sourceDir)
for file in files:
	if file.find(fileExt) > 0:
		print('Processing ' + file)
		try:
			with open(file, encoding='utf-16') as f:
				content = f.readlines()
				parseContent(content)
		except UnicodeError:
			with open(file) as f:
				content = f.readlines()
				parseContent(content)
