import fileinput
f1=open("listofauthors.txt","r")
contents=f1.readlines()
f1.close()
f1=open("newcopy.txt","w")
with open("myfile.txt","r")as f:
	content=f.readlines()
for li in content:
	print li
	if li in contents:
		
		continue
	else:
		f1.write(li)
f1.close()
