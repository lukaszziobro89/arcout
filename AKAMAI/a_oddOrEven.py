#odd - nieparzysty
#even - parzysty

def oddEvenUser():
    try:
        number = int(input("Please give number: "))
        if number % 2 == 1:
            print("Number you provided ({}) is odd.".format(number))
        else:
            print("Number you provided ({}) is even.".format(number))
    except ValueError:
        print("You did not provided integer number.")

def oddEvenInput(input_number):
    if type(input_number) != int:
        print("You did not provided integer number.")
    else:
            if input_number % 2 == 1:
                print("Number you provided ({}) is odd.".format(input_number))
            else:
                print("Number you provided ({}) is even.".format(input_number))


oddEvenInput(6)