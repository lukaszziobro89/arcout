separator = ", "

def listLessThenInput():
    number = int(input("Please give number: "))
    print(separator.join(str(i) for i in range(number)))

def listLessThenArgument(number):
    print(separator.join(str(i) for i in range(number)))

def listLessThenSeparator(number, separator):
    print(separator.join(str(i) for i in range(number)))



listLessThenInput()
listLessThenArgument(7)
listLessThenSeparator(5, " | ")
