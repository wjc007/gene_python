import sys
import string
from math import ceil, floor


def Overlap(string, parts, overlap, destination):
	ref = open(string,"r")
	input = ref.read()
	n = len(input)
	
	iOverlap = int(overlap)
	iParts = int(parts)
	r = (n + iOverlap * iParts - iOverlap) % iParts 
	l = (n + float(overlap) * float(parts) - float(overlap)) / float(parts)
	L1 = ceil(l)
	L2 = floor(l)
	flag = 0
#	print L1, L2, r, l, input, n, iOverlap, iParts
	print n
	for i in range(1, iParts+1):
		if i <= r :
		
			info = str(flag) + ' ' + str(overlap)
		
			path_2 = destination + '/' + str(i) + 's.txt'
			f = open(path_2,"w")
			f.write(info)
			f.close()
		
			s = input[int(flag):int(flag + L1)]
			path = destination + '/' + str(i) + '.txt'
			f = open(path,"w")
			f.write(s)
			f.close()
			
			flag = flag + L1 - iOverlap
			
    
		if i > r and i <= iParts :
		
			info = str(flag) + ' ' + str(overlap)
		
			path_2 = destination + '/' + str(i) + 's.txt'
			f = open(path_2,"w")
			f.write(info)
			f.close()
		
			s = input[int(flag):int(flag + L2)]	
			path = destination + '/' + str(i) + '.txt'
			f = open(path,"w")
			f.write(s)
			f.close()
			
			flag = flag + L2 - iOverlap
	
"""
if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
"""