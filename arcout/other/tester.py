import re
tekst = '"26558731","Windows","S","login_1","SWISS-DD-2"'
x = tekst.split(',')
strs = x[4]

match = re.search(r'\bSWISS-DD\b',strs)
if match:
    print("Found")
else:
     print("Not Found")