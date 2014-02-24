import sys
import os
from search import Search
from Filter import Filter
from overlap import Overlap


def main(query, string, parts, overlap, destination):

	Path_Filter = destination + '/Filter'	
#	if not os.path.exists(Path_Filter):
#		 os.makedirs(Path_Filter)
#	seq = Filter(string, Path_Filter)


#	for i in range(1, seq + 1):
#		inPath_Overlap = Path_Filter + '/seg_' + str(i) + '.txt'
#		Path_Overlap = Path_Filter + '/seg_' + str(i)
#		if not os.path.exists(Path_Overlap):
#			os.makedirs(Path_Overlap)
#		Overlap(inPath_Overlap, parts, overlap, Path_Overlap)
		
	result = destination + '/result.txt'	

	seq = 25
	for i in range(1, seq + 1):
		print i
		Path_Overlap = Path_Filter + '/seg_' + str(i)
		for j in range(1, int(parts) + 1):
			print j
			inPath_Search = Path_Overlap + '/' + str(i) + '.txt'
			Search(inPath_Search, query, result)


	
if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])