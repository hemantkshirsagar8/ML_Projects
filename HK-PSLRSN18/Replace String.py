import os
texttofind = 'text want to replace'
texttoreplace='replace with'
sourcepath = os.listdir('Source path paste here')
for file in sourcepath:
    inputfile ='Source Path paste here '+file
    print ('Conversion is ongoing for:' +inputfile)
    with open(inputfile,'r') as inputfile:
        filedata = inputfile.read()
        freq=0
        freq=filedata.count(texttofind)
    destinationpath='Destination Path'+file
    filedata= filedata.replace(texttofind,texttoreplace)
    with open(destinationpath,'w') as file:
            file.write(filedata)
    print ('Total %d record Replace'%freq) 
    