def dumb_sentence(name='Lukasz', surname='Ziobro', city='Krakow'):
    print(name,surname,city)

dumb_sentence()


#------------------------------------------------------------------

def printEveryting(*args):
    for word in args:
        print(word, end=' ')

printEveryting("Lukasz", "Ziobro", "Krakow")

#------------------------------------------------------------------

def addNumber(*args):
    suma = 0
    print("Your numbers are: ", end=' ')
    print(*args,sep=', ')
    for number in args:
        suma = suma + number
    print("Your sum is: " + str(suma))

addNumber(3,4,5,10)

#------------------------------------------------------------------

numbers=[1,2,3,4]

def listSum():
    suma=0
    for i in numbers:
        suma=suma + i
    print(suma)

listSum()

#===========================

def aaa(number, separator):
    print(separator.join(str(i) for i in range(number)))

aaa(4,'-')

print("-1-".join("a" "b" "c"))

for element in enumerate(range(10, 15)):
    print(element)

#===========================

def addNumberInput():
    elements = int(input("How many numbers you want to add? "))
    print("You want to add " + str(elements) + " numbers.")
    suma = 0
    for i in range(1, elements + 1):
        x = int(input("Please provide " + str(i) + " element: "))
        suma = suma + x
    print("Your sum is: " + str(suma))

addNumberInput()