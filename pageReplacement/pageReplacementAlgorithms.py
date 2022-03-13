class FIFO:
    NAME='FIFO'
    oldest=0
    def replace(self,_pageReplacer):
        self.oldest=_pageReplacer.frameSize-1
        for i in range(len(_pageReplacer.referenceString)):
            if _pageReplacer.referenceString[i] in _pageReplacer.ram:
                _pageReplacer.hit()
            else:
                _pageReplacer.fault()
                _pageReplacer.ram[self.oldest]=_pageReplacer.referenceString[i]
                self.oldest=_pageReplacer.frameSize-1 if self.oldest==0 else self.oldest-1
            _pageReplacer.saveRamState(i)

class LRU:
    NAME="LRU"
    valueIndexMap={}
    def replace(self,_pageReplacer):
        for i in range(len(_pageReplacer.referenceString)):
            if _pageReplacer.referenceString[i] in _pageReplacer.ram:
                _pageReplacer.hit()
            else:
                _pageReplacer.fault()
                if (0 in _pageReplacer.ram):
                    _pageReplacer.ram.reverse()
                    _pageReplacer.ram[_pageReplacer.ram.index(0)]=_pageReplacer.referenceString[i]
                    _pageReplacer.ram.reverse()
                else:
                    leastRecentlyUsed=min(self.valueIndexMap, key=self.valueIndexMap.get)
                    del self.valueIndexMap[leastRecentlyUsed]
                    _pageReplacer.ram[_pageReplacer.ram.index(leastRecentlyUsed)]=_pageReplacer.referenceString[i]
            self.valueIndexMap[_pageReplacer.referenceString[i]]=i
            _pageReplacer.saveRamState(i)

class Optimial:
    NAME="Optimal"
    def getFarthest(self,ram,referenceString):
        for i in range(len(ram)):
            if ram[-(i+1)] not in referenceString:
                return -(i+1)
        temp=float('-inf')
        for i in range(len(ram)):
            if(referenceString.index(ram[i])>temp):
                temp=referenceString.index(ram[i])
        return ram.index(referenceString[temp])
            
        
    def replace(self,_pageReplacer):
        for i in range(len(_pageReplacer.referenceString)):
            if _pageReplacer.referenceString[i] in _pageReplacer.ram:
                _pageReplacer.hit()
            else:
                _pageReplacer.fault()
                if (0 in _pageReplacer.ram):
                    _pageReplacer.ram.reverse()
                    _pageReplacer.ram[_pageReplacer.ram.index(0)]=_pageReplacer.referenceString[i]
                    _pageReplacer.ram.reverse()
                else:
                    farthest=self.getFarthest(_pageReplacer.ram,_pageReplacer.referenceString[i:])
                    _pageReplacer.ram[farthest]=_pageReplacer.referenceString[i]
            _pageReplacer.saveRamState(i)


    
