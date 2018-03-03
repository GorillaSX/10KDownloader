#declare a class used to parse html get all filing source and pass to source manager
import html_downloader 
import filing_source
import source_manage
from lxml import etree
class HtmlParser(object):
    def __init__(self,ty,cik): 
        self.ty = ty          #ty is the type of the filing
        self.cik = cik
        self.baseaddress = "https://www.sec.gov"
        #a downloader used to download html
        self.downloader = html_downloader.HtmlDownloader()
        #the first page of filing list
        self.filingListUrl = self.baseaddress + "/cgi-bin/browse-edgar?action=getcompany&CIK=" + self.cik + "&type=" + self.ty + "&dateb=&owner=exclude&count=100"
        

    def putSourceToManager(self,url,sourceManager):
        #parsing the url
        html = self.downloader.download(url)
        html = etree.HTML(html)
        filingUrl = html.xpath('//td/a[@id="documentsbutton"]/@href')
        for url in filingUrl:
            url = self.baseaddress + url
            html = self.downloader.download(url)
            html = etree.HTML(html)
            condition = '//tr[td="'+self.ty+'"]//a/@href'
            address = html.xpath(condition)
            #verify the address
            if len(address) != 0:
                if address[0][-1] != '/':
                    filingaddress = self.baseaddress + address[0]
                    #get the filing date
                    date = html.xpath('//div[div="Filing Date"]/div')
                    date = date[1].text
                    date = date.replace('-','')
                    filingsource = filing_source.FilingSource(filingaddress,date,self.ty)
                    #put the filing source to manager
                    sourceManager.addNewSource(filingsource)

    def getCompanyName(self):
        html = self.downloader.download(self.filingListUrl)
        html = etree.HTML(html)
        companyName = html.xpath('//span[@class="companyName"]')
        companyName = companyName[0].text
        companyName = companyName.strip()
        companyName = companyName.replace(' ','_')
        return companyName
    
    def parse(self,sourceManager):
        print "start parsing ..."
        #parse the first filing list page
        self.putSourceToManager(self.filingListUrl,sourceManager)
        html = self.downloader.download(self.filingListUrl)
        html = etree.HTML(html) 
        #parse the remain filing list page 
        while True:
            nextpage = html.xpath('//input[@type="button" and @value="Next 100"]/@onclick')
            if len(nextpage) == 0:
                break
            nextpage = nextpage[0]
            nextpage = nextpage[17:-1]
            nextpage = self.baseaddress + nextpage
            print nextpage
            self.putSourceToManager(nextpage,sourceManager)
            html = self.downloader.download(nextpage)
            html = etree.HTML(html)

        print "end parsing"



