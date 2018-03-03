#define a class used to download wanted filing
import filing_source
import source_manage
import html_downloader
import html_parser
import os
class FilingDownloader(object):
    def __init__(self,cik,ty):
        #a parser used to get filing url 
        self.parser = html_parser.HtmlParser(ty,cik)
        #a source manager used to store filing url
        self.sourceManager = source_manage.SourceManager()
        self.ty = ty
        self.cik = cik
        
    def start(self):
        #crawler filing url and put to the source manager
        self.parser.parse(self.sourceManager)
        #make a directory used to store the filing file
        companyName = self.parser.getCompanyName()
        dirpath = './'+companyName+'/'+ self.ty
        isExists = os.path.exists(dirpath)
        if not isExists:
            os.makedirs(dirpath)
        dirpath = dirpath + '/'
        #download filing to the created directory
        self.sourceManager.saveToLocal(dirpath)

if __name__ == "__main__":
    fildingdownloader = FilingDownloader("0000320193","8-K")
    fildingdownloader.start()
