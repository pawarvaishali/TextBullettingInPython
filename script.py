''' author : Vaishali Pawar '''
''' date : 30th August 2018 '''

import re
import fileinput

bulletLines = []	
bulletLinesEx = []
lst = []
indent = '  '
prev = 0

for line in fileinput.input():
	if len(line) != 0:
		''' splits the data line based on occurences of * and . in the line content	'''
		lineData = re.match("^(\.*)(\**)\s*(.*)$", line)	
		
		if not re.search(r"^\s+$", line):	# checking if line doesn't have only whicte spaces
					
			if lineData.group(1):
				''' bullet writing for . character '''
				
				currBlt = lineData.group(1)
				if len(bulletLinesEx) > 0:
					if prev < len(currBlt):
						bulletLinesEx[-1] = bulletLinesEx[-1].replace('-', '+', 1)
				bulletLinesEx.append(indent*len(currBlt) + "- " + lineData.group(3).strip())
				prev = len(currBlt)
				
			elif lineData.group(2):
				''' bullet writing for * character '''
				
				currBlt = lineData.group(2)
				while len(lst) < len(currBlt):
					lst.append(0)
					
				lst[len(currBlt)-1] = lst[len(currBlt)-1] + 1
				for i in range(len(currBlt), len(lst)):
					lst[i] = 0
				
				bulletLines += bulletLinesEx
				bulletLinesEx = []
				bulletLines.append(".".join(map(str, lst[:len(currBlt)])) + " " + lineData.group(3).strip())
			
			else:
				bulletLinesEx.append(indent*len(currBlt) + "  " + lineData.group(3).strip())
bulletLines += bulletLinesEx
				
''' write the output file '''
	
for each in bulletLines:	
	print(each)
