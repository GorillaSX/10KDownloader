#declare a class to managing all filing source
import filing_source  
class SourceManager(object):
    def __init__(self):
        self.filingSources = set() #a set used to store filing source

    def addNewSource(self,source):
        #print "add source to source list begin"
        if source is None:
            return 
        self.filingSources.add(source)
        #print "end add source to source list begin"

    def popSource(self):
        #print "start to pop a source"
        source = self.filingSources.pop()
        #print "end to pop a source"
        return resource
    
    def saveToLocal(self,dirpath):
        print "start to saving all filing to local"
        for source in self.filingSources:
            source.saveFilingToLocal(dirpath)
        print "end saving all filing to local"
