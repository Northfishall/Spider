import SpiderLib
import MongoDB

def GetPage(index):
    url = "http://www.oneniceapp.com/sneakerweb/productlist"
    web = SpiderLib.visitByLocalNet(url)
    #f = open('d://Nice.txt', 'wb')
    #f.write(web.data)
    SpiderLib.getNiceTextData(web,index)



#GetPage()
