def dumb_sentence(name='Lukasz', surname='Ziobro', city='Krakow'):
    print(name,surname,city)

dumb_sentence()


#------------------------------------------------------------------

def printEveryting(*args):
    for word in args:
        print(word, end=' ')

printEveryting("Lukasz", "Ziobro", "Krakow")
print('\n')

#------------------------------------------------------------------

def addNumber(*args):
    suma = 0
    print("Your numbers are: ", end=' ')
    print(*args,sep=', ')
    for number in args:
        suma = suma + number
    print("Your sum is: " + str(suma))

addNumber(3,4,5,10)


