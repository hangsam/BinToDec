import Validation
import conversion
import addition
import gates

while True:
        select= input("Enter 'd' for using decimal numbers or 'b' for using binary numbers  ")
        value = select.lower()
        if value == "d":
            while True:
                decimalNum1=input("Enter your first decimal number:- ")
                decimalNum1= Validation.validationDec(decimalNum1)
                
                decimalNum2=input("Enter your second decimal number:- ")
                decimalNum2= Validation.validationDec(decimalNum2)
                if decimalNum1+decimalNum2 > 255:
                    print("Plese enter number whose sum is less than 255")
                    continue
                else:
                    break
            binaryNum1 = conversion.convertDecToBin(decimalNum1)
            binaryNum2 = conversion.convertDecToBin(decimalNum2)
           

        elif value == "b":
            print("Enter binary number. Only 1 and 0 is accepted ")
            while True:
                binaryNum1= input("Enter your first binary number:- ")
                binaryNum1= Validation.validationBin(binaryNum1)

                binaryNum2=input("Enter your second binary number:- ")
                binaryNum2= Validation.validationBin(binaryNum2)

                binaryNum1 = int(binaryNum1)
                binaryNum2 = int(binaryNum2)

                a= conversion.convertBinToDec(binaryNum1)
                b= conversion.convertBinToDec(binaryNum2)

                if (a+b) > 255:
                    print("Invalid!!..The sum of the binary numbers cannot be more than 11111111.")
                    continue
                else:
                    break
            decimalNum1= conversion.convertBinToDec(binaryNum1)
            decimalNum2= conversion.convertBinToDec(binaryNum2)
        elif(value == ""):
            print("Empty input cannot get access in program")
            continue
        else:
            print("Please !! Enter correct input d or b")
            continue
        decimalAddition = (decimalNum1+decimalNum2)
            
        print("_____________________________________________________")
        print("********-- First Input Values --********")

        print("First Decimal Number. is: ", decimalNum1)
        print("First Binary Number. is: ", binaryNum1)
        print("_____________________________________________________")

        print("********-- Second Input Values --********")

        print("Second Decimal Number. is: ", decimalNum2)
        print("Second Binary No. is: ", binaryNum2)
        print("_____________________________________________________")

            

        print("*************-- Byte Adder --**************")
            
        binaryAddition = addition.binaryAdder(binaryNum1,binaryNum2)

        print("_____________________________________________________")
        print("*_* *_* *_* == OVERALL RESULT == *_* *_* *_*")
        print("_____________________________________________________")
            
        print("***** Decimal number    Binary number *****"  )           
        print("         ",decimalNum1,"             ",binaryNum1)
        print("        +",decimalNum2,"            +",binaryNum2)
        print("     ____________      _______________")
        print("         ",(decimalAddition),"            ",(binaryAddition))
        
        while True:
                continuous=input("Do you want to continue this program, 'Yes'? Type 'No' to exit:- ").lower()
                if continuous == "yes" or continuous == "no":
                        break
                if continuous == "":
                        print("EMPTY FIELD FOUND")
                        continue
                else:
                        print("Please enter the suitable value 'yes' or 'no'.")
                        continue
        if continuous== "yes":
            continue
        elif continuous== "no":
                print("Thank you for using it!!!")
                print("See you next time!!!")
                print("Samsuhang Nembang @2020 Copyright")
                break
            

