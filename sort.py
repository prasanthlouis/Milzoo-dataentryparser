import codecs
import fileinput
def uniquelines(lineslist):
    unique = {}
    result = []
    for item in lineslist:
        if item.strip() in unique: continue
        unique[item.strip()] = 1
        result.append(item)
    return result
f = open('newcopy.txt','r')
lines = f.readlines()
f.close()
f = open('newcopy.txt','w')
lines.sort()
for x in lines:
	x = x[:-1]
	f.write(x+'\n')
f.close()
file1 = codecs.open('newcopy.txt','r+','cp1251')
filelines = file1.readlines()
file1.close()
output = open("newcopy.txt","w")
output.writelines(uniquelines(filelines))
output.close()

        
