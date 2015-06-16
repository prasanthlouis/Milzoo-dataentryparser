import pyPdf
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from os import listdir
from os.path import isfile, join

flag=0
i=0
j=0
flagtit=0
list=[]
title=""
authorx=""
author=""
quote="'"
desc=""

mypath="C:\Users\Prasanth\Desktop\journal14\part3\\"
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
'Dr. Meera Jan Abraham St.Teresas College':77,
'Jayasree S.Mercy College':78,
'Deepthi Venugopal St.Aloysius College':79,
'Indu M.S.':80,
'Saritha Francis':81, 
'Jose Jacob':82,
'Mohammed-Aslam M. A.':83, 
'A. K. Abdussalam':84,
'Rose Anitha':85,
'Varghese P.R':86,
'A. Dalie Dominic':89,
'A.K.Abdussalam':90,
'Ambily C.B':91,
'Anu S':92,
'Gayathri Elayidam U.':93,
'K. Madhusudhanan':94,
'K. Raju Thomas':95,
'K.A. Rasheed':96,
'M. Zubair ':97,
'M.A. Mohammed-Aslam':98,
'Mohammed-Aslam M. A .':99,
'P.R.Varghese' :100,
'Ruby Thomas' :101,
'S. Smitha':102,
'Sabari S' :103,
'Saji K.G.':104,
'Sreelatha B.Nair':105,
'Suresh Mohan Ghosh':106,
'Swapana Johny':107




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
'''
driver = webdriver.Firefox()

username = driver.find_element_by_name("admin_name")
password = driver.find_element_by_name("admin_password")
driver.find_element_by_name("submit").click()
'''

for y in onlyfiles:
		

	x=getPDFContent(mypath+y).encode("ascii", "ignore")
	f=open("contents.txt","a")
	f.write(x+'\n') # python will convert \n to os.linesep
	f.close() 
	'''
	#use this after adding authors
	for val in values:
		if val in x:
			authorx+=val
	print authorx
	
	temptitle=x.split(":",1)[1] 
	while(flagtit==0):
		try:
			while(temptitle[i].islower() or temptitle[i].isdigit() or temptitle[i]==',' or temptitle[i]=='.' or temptitle[i]==' ' or temptitle[i+1].islower() or temptitle[i+1]=='.' or temptitle[i]=='&' or temptitle[i+2]==' ' or temptitle[i+1]==' ' or temptitle[i]=='-'):
				
				i+=1
		except:
			print 'except'

		while(temptitle[i].isupper() or temptitle[i]==' ' or temptitle[i]==',' or temptitle[i]=='(' or temptitle[i]==')' or temptitle[i]=='-' or temptitle[i]=='.' or temptitle[i]=='&' or temptitle[i]==':' or temptitle[i]=='p'):
			title+=str(temptitle[i])
			i+=1
		title = title[:-1]
		if title=='RESEARCH PAPER ISSN' or title=='ISSN':
			title=""
			continue
		else:
			break
	
	
	
	i-=1
	'''
	'''
	while(1):
		if((temptitle[i]=='I' and temptitle[i+1]=='n' and temptitle[i+2]=='t') or ((temptitle[i]=='A' and temptitle[i+1]=='b' and temptitle[i+2]=='s'))):		
			break
		else: 
			authorx+=str(temptitle[i])
		
			i+=1
	if 'and' in authorx:
		authorx=re.sub(r"\band\b",",",authorx)
	list=authorx.split(',')	
	f = open('myfile.txt','a')
	for lis in list:
		f.write(lis+'\n') # python will convert \n to os.linesep
	f.close() 
	'''
	'''
	if 'Abstract' in x:
		if 'Key words' in x:
			desc=re.findall(r'Abstract(.*?)Key words',x)
		else:
			desc=re.findall(r'Abstract(.*?)Introduction',x)
		flag=1
	if(flag==0):
		if 'Introduction' in x:
			desc=re.findall(r'Introduction(.*?)Abstract',x)
			flag=1
	
	
	print desc
	'''
	'''
	driver.find_element_by_xpath("//select[@id='journal_name']/option[@value='29']").click()
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
	
	'''
	
	
	
	title=""
	i=0
	author=""
	authorx=""
	flag=0
	desc=""

			

		
		
