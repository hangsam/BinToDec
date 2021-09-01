#sum = xor(xor(b1,b2),carry)
#carry = or(and(b1,b2),and(xor(b1,b2)carry))

from gates import *
def binaryAdder(num1, num2):
    lst1 = ["0", "0", "0", "0", "0", "0", "0", "0"]
    lst2 = ["0", "0", "0", "0", "0", "0", "0", "0"]
    carry = 0
    i = 7
    print(num1)
    print("-")
    print(num2)
    while (i>0):

        r1 = int(num1) % 10
        r2 = int(num2) % 10

        #For sum
        Xor1 = xorGate(r1,r2)
        sum_ = xorGate(Xor1,carry)

        #For carry
        and1 = andGate(r1, r2)
        and2 = andGate(Xor1, carry)
        carry = orGate(and1, and2)

        lst1[i] = str(sum_)
        lst2[i] = str(carry)
        i = i - 1
        num1 = int(num1) // 10
        num2 = int(num2) // 10
    return ("".join(lst1))

