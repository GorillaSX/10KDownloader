#declare a class used to store the  filing url and associate information
import html_downloader 
class FilingSource(object):
    def __init__(self,address,date,tp):
        self.address = address  
        self.date = date     #filing date
        self.tp = tp #tp is type of the filing
    
    def downloadFiling(self):
        print "start download filing"
        downloader = html_downloader.HtmlDownloader()
        filing = downloader.download(self.address)
        print "end download filing"
        return filing
    
    def saveFilingToLocal(self,dirpath):
        print "start to save filing to local"
        #download filing
        filing = self.downloadFiling()
        #generate file name
        filename = dirpath + self.tp + '_'+ self.date
        #open a file
        f = open(filename,'w')
        f.write(filing)
        f.close()
        print "end save filing to local"


 
        




