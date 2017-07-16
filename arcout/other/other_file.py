"""lista = ["a","b","c","d","e","f","g","h",]
lista_length=lista.__len__() -2
lista.remove(lista[2])
print(lista)
del lista[2:lista_length]
print(lista)"""
"""
from tqdm import *
import re
arctest = open("C:\\Users\luq\Desktop\\arctest-c.txt", "r+")
#arctest_cleaned = open("C:\\Users\luq\Desktop\\swiss_dd_cleaned.txt", "w")

def remove_swiss_dd(comma_string):
    try:
            for line in comma_string.readlines():
              splitted_string = line.split(',')
              print(str(splitted_string[4]))
              if re.match(r'^SWISS-DD', str(splitted_string[4])):
              #if splitted_string[4].startswith('"SWISS-DD"'):
                print("SWISS-DD ACCOUNT")
              else:
                  print("Other ACCOUNT")
                  #log_file.write("User account deleted: {}" .format(line))
    except AttributeError:
        print("Please provide string separated by comma as argument.")

remove_swiss_dd(arctest)
"""
import re
tekst = '"26558731","Windows","S","login_1","SWISS-DD-2"'
lista = ["SSISS-DD","SWISS-DD","SWISS-DD-2","SWISS-DD","SWISS-DD-3","SWISS-DS"]
for x in lista:
    if str(x).startswith("SWISS-DD"):
        print(x)

a=tekst.split(',')
print(a)
x=a[4]
print(x)
#if str(x).startswith('"SWISS-DD"'):
if re.match(r'^SWISS-DD', str(a[4])):
    print("ok")