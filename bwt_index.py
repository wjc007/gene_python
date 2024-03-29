from copy import deepcopy

"""
Get bwt for the given string
"""
class BWTCreator(object):
    TERMINATION_CHAR = chr(255)

    def __init__(self, string):
        self.string = string

    # Get bwt
    def bwt(self):
        original = self.string + self.TERMINATION_CHAR
        permutations = []
        for i in range(0, len(original)):
            permutations.append((original[i:] + original[0:i], i))
        def cmpFn (x, y):
            if (x[0] == y[0]):
                return 0
            elif (x[0] < y[0]):
                return -1
            else:
                return 1
        permutations.sort(cmp=cmpFn)
        bwt = ''
        suffixArray = []
        for permutation in permutations:
            bwt += permutation[0][-1]
            suffixArray.append(permutation[1])
        return (bwt, suffixArray)

"""
Get rank of a character given an alphabet(ordered) and a frequency
map of all characters in the alphabet
"""
class BWTIndexCreator(object):
    
    def __init__(self, bwt, suffixArray):
        self.bwt = bwt
        self.suffixArray = suffixArray

    def getIndex(self):
        freq = {}
        for ch in self.bwt:
            if freq.has_key(ch):
                freq[ch] += 1
            else:
                freq[ch] = 1
        alphabet = freq.keys()
        alphabet.sort()
        cumulativeMap = CumulativeMap(alphabet, freq)
        bwtRanks = self.getBWTRanks()
        return (self.bwt, cumulativeMap, bwtRanks, self.suffixArray)

    def getBWTRanks(self):
        cumulative = {}
        for el in self.bwt:
            cumulative[el] = 0
        bwtRanks = []
        for el in self.bwt:
            bwtRanks.append(BWTRow(el, deepcopy(cumulative)))
            cumulative[el] += 1
        return bwtRanks

"""
A row in the bwt index
"""
class BWTRow(object):

    def __init__(self, el, ranks):
        self.el = el
        self.ranks = ranks

"""
Map for the cumulative counts of first column
"""
class CumulativeMap (object):
    
    def __init__(self, alphabet, freq):
        self.cumulativeMap = self.getCumulativeMap(alphabet, freq)

    def getCumulativeMap(self, alphabet, freq):
        ret = {}
        cumulative = 0
        for el in alphabet:
            ret[el] = (cumulative, cumulative + freq[el])
            cumulative += freq[el]
        return ret

    def getStart(self, el):
        if self.cumulativeMap.has_key(el):
            return self.cumulativeMap[el][0]
        else:
            return -1

    def getEnd(self, el):
        if self.cumulativeMap.has_key(el):
            return self.cumulativeMap[el][1]
        else:
            return -1

    def getPosition(self, el, elCount):
        return self.cumulativeMap[el][0] + elCount
		

def getBWTIndex(string):
    bwtCreator = BWTCreator(string)
    (bwt, suffixArray) = bwtCreator.bwt()
    indexCreator = BWTIndexCreator(bwt, suffixArray)
    index = indexCreator.getIndex()
    return index
