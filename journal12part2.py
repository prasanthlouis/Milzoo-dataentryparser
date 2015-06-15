import pyPdf
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from os import listdir
from os.path import isfile, join

flag=0
i=0
j=0
list=[]

title=""
authorx=""
author=""
quote="'"

mypath="C:\Users\Prasanth\Desktop\journal12\part2\\"
values={'Dr P R Varghese':34,'Amina S.':35,'Thomas Zachariah':36,'Ramesh Babu M.G.':38,'B. Sleema':39,'Rajkumar R.':40,'K. K. Hemalatha':41,'James T. J.':42,'Tresamma George':43,'Manju V. Subramanian':44,'Jeeja Tharakan':45,'N. D. Inasu':46,'Raju Thomas K.':47,'M. John George':48,'Savitha Nandanan':49,'Joseph Louis Olakkengil':50,'Sreeranjit kumar C.V.':51,'Ramya K.':52,'Usha M.':53,'Madhavan. S':54,'G. Muraleedhara Kurup':55,'Dhanalekshmy':56,'Radhadevi':57,'Jojo Joseph Vellanikaran':58,'P. A. SebastianSacred Heart College':59,
'Abdussalam A.K.':60,
'E.A.A. Shukkur':61,
'E.A.Jayson':62,
'Fab.Varghese P.P.':63,
'Francy C.F.':64,
'G. Girijan':65,
'Jain J.Therattil':66, 
'Jinsu Varghese':67,
'K. Azeez':68,
'K.R. Arathy':69,
'M.A.Mohammed-Aslam':70,
'P.A. Azeez':71,
'P.V. Jyothi':72,
'Sheela Devi D':73,
'Thomas K.M.':74,
'Zubair':75,
'Ms.Rima Joseph':76,
'Dr. Meera Jan Abraham':77,
'Jayasree S.Mercy College':78,
'Deepthi Venugopal':79
}
def getPDFContent(path):
    content = ""
    # Load PDF into pyPDF
    pdf = pyPdf.PdfFileReader(file(path, "rb"))
    # Iterate pages
    for i in range(0, pdf.getNumPages()):
        # Extract text from page and add to content
        content += pdf.getPage(i).extractText() + "\n"
    # Collapse whitespace
    content = " ".join(content.replace(u"\xa0", " ").strip().split())
    return content
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]

driver = webdriver.Firefox()

username = driver.find_element_by_name("admin_name")
password = driver.find_element_by_name("admin_password")
driver.find_element_by_name("submit").click()


print onlyfiles
for y in onlyfiles:
	

	x=getPDFContent(mypath+y).encode("ascii", "ignore")
	for val in values:
		if val in x:
			authorx+=val
	print authorx
	temptitle=x.split(":",1)[1]


	try:
		while(temptitle[i].islower() or temptitle[i].isdigit() or temptitle[i]==',' or temptitle[i]=='.' or temptitle[i]==' ' or temptitle[i+1].islower() or temptitle[i+1]=='.' or temptitle[i]=='&' or temptitle[i+2]==' ' or temptitle[i+1]==' ' or temptitle[i]=='-'):
			
			i+=1
	except:
		print 'except'

	while(temptitle[i].isupper() or temptitle[i]==' ' or temptitle[i]==',' or temptitle[i]=='(' or temptitle[i]==')' or temptitle[i]=='-' or temptitle[i]=='.' or temptitle[i]=='&' or temptitle[i]==':'):
		title+=str(temptitle[i])
		i+=1
	title = title[:-1]
	print title
	
	

	i-=1
	'''
	while(1):
		if(temptitle[i]==' ' and temptitle[i+1]=='b' and temptitle[i+2]=='y'):
			break
		else: 
			i+=1

	i+=4
	while(temptitle[i]!=','):
		author+=temptitle[i]
		i+=1
	print author
	f = open('myfile.txt','a')
	f.write(author+'\n') # python will convert \n to os.linesep
	f.close() 
	'''
	
	if 'Summary' in x:
			desc=x.split("Summary",1)[1] 
	

			
	
	driver.find_element_by_xpath("//select[@id='journal_name']/option[@value='28']").click()
	articlename=driver.find_element_by_name("article_name")
	articlename.send_keys(title)
	articledesc=driver.find_element_by_name("article_desc")
	articledesc.send_keys(desc)
	articlepdf=driver.find_element_by_name("article_pdf")
	articlepdf.send_keys(mypath+y)
	for vals in values:
		if vals in authorx:
			print str(values[vals])
			driver.find_element_by_xpath("//select[@id='article_author']/option[@value="+quote+str(values[vals])+quote+"]").click()	
	submit=driver.find_element_by_name("submit").click()
	
	title=""
	i=0
	author=""
	authorx=""

			

		
		
