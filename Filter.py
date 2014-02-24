import sys
import string

def Filter(string, destination):

	i = 0
	path = destination + '/seg_' + str(i) + '.txt'
	f = open(path,"w")
	with open(string,"r") as FileIn:
		for line in FileIn:
		
			if '>' in line:
				f.close() #close the previous file
				i += 1
				path = destination + '/seg_' + str(i) + '.txt'
				f = open(path,"w")
#				f.write(line)
				
			else:
				f.write(line.strip('\n'))
				
	return i
"""
				if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
"""				