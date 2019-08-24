import shutil
import re
import os

#shutil.copy('C:\\Users\\Owner\\Downloads\\Python Materials\\Python - humble bundle\\elegantscipy.epub', 'C:\\Users\\Owner\\Downloads\\Python Materials\\Python - humble bundle\\Test')


listOfFiles = os.listdir('C:\\Users\\Owner\\Downloads\\Python Materials\\Python - humble bundle')
stringOfFiles = ', '.join(listOfFiles)
#print(listOfFiles)
#print(stringOfFiles)

pdfsregex = re.compile(r'\w+\.pdf')
print(pdfsregex.findall(stringOfFiles))
allpdfs = pdfsregex.findall(stringOfFiles)


os.makedirs('C:\\Users\\Owner\\Downloads\\Python Materials\\Python - humble bundle\\PDFS', exist_ok=True)
for i in allpdfs:
    shutil.copy('C:\\Users\\Owner\\Downloads\\Python Materials\\Python - humble bundle\\'+i, 'C:\\Users\\Owner\\Downloads\\Python Materials\\Python - humble bundle\\PDFS\\'+i)
