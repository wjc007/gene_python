from bwt_index import getBWTIndex
import sys


class BWTIndex (object) :
    
    def __init__(self, bwt, cumulativeMap, bwtRanks, suffixArray):
        self.bwt = bwt
        self.cumulativeMap = cumulativeMap
        self.bwtRanks = bwtRanks
        self.suffixArray = suffixArray

    # Search for a given string
    # Returns the range [x,y) of matches. Returns None if no match found
    def search(self, query):
        start = self.cumulativeMap.getStart(query[-1])
        end = self.cumulativeMap.getEnd(query[-1])
        for i in range(len(query)-2, -1, -1):
            el = query[i]
            if (start >= end):
                return None
            bwtStartRow = self.bwtRanks[start].ranks
            bwtEndRow = self.bwtRanks[end].ranks

            elStart = bwtStartRow[el]
            elEnd = bwtEndRow[el]
            if (elStart < 0) or (elEnd < 0):
                return None
            start = self.cumulativeMap.getPosition(el, elStart)
            end = self.cumulativeMap.getPosition(el, elEnd)

        if (start >= end):
            return None
        ret = set() 
        for i in range(start, end):
            ret.add(self.suffixArray[i])
        return ret
		
def Search(string, query, result):
	f_txt = open(string,"r")
	input = f_txt.read()
	index = getBWTIndex(input)
	getLocation = BWTIndex(index)
	location = getLocation.search(query)
#	print location
	if not location:
		return
	
	path_Info = string[:-4] + 's' +string[-4:]
#	print path_Info
	f_info = open(path_Info, "r")
	sInfo = f_info.read()
	pos = sInfo.find(" ",0)
	flag = sInfo[:pos]
	overlap = sInfo[pos+1:]
	
	iFlag = int(float(flag))
	iOverlap = int(overlap)
	
#	print flag, overlap, iFlag, iOverlap

	f_res = open(result, "a")

	ret = []
	for i in location:
		if i > iOverlap - len(query) and iFlag != 0:
			i += iFlag
			ret.append(i)
			
	print ret
	sRet = str(ret)
	f_res.write(sRet)
	f_res.close()