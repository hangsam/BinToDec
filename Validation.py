def validationBin(number):
            while True:
                length = len(number)
                num1 = 0
                if (number == ""):
                    print("Empty field found!! Please enter the valid decimal number between 0 to 9")
                    number=input("please! enter valid number 0 or 1: ")
                    continue
                elif (length > 8):
                    print("Error!!...The length of binary number cannot exceed 8.")
                    number=input("please! enter number less than 8 bit, valid number 0 or 1: ")
                    continue
                else:
                    try:
                        num1 = int(number)
                        x = list(map(int,str(num1)))
                        y = set(x)
                        if y == {0} or y == {1} or y == {0,1}:
                            break
                        else:
                            print(" Invalid!! The input values must be either 1 or 0 number")
                            number=input("please! enter valid number 0 or 1: ")
                            continue
                    except:
                        print("Special characters or Alphabets found!! Please Enter the valid decimal number between 0 to 255")
                        number=input("please! enter valid number 0 or 1: ")
                        continue
                    
            return number


def validationDec(number):
        while True:
            if (number == ""):
                    print("Empty field found!! Please enter the valid decimal number between 0 to 255")
                    number=input("please! enter valid number 0 to 255: ")
                    continue
            try:
                number = int(number)
            except:
                print("ERROR!!!...Special characters or Alphabets found!! Please Enter the valid decimal number between 0 to 255")
                number = input("Please!! enter valid number 0 to 255:- ")
                continue
            if (number < 0 or number > 255):
                print("ERROR!!!...values that are negative and greater than 255 are not valid decimal number")
                number = input("Please!! enter valid number 0 to 255:-")
                continue
            else:
                break            

        return number
           


