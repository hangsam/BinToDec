def convertDecToBin(num):
    i = 7
    st = ["0", "0", "0", "0", "0", "0", "0", "0"]
    while (num > 0):
        r = num % 2
        st[i] = str(r)
        i = i-1
        num = int(num / 2)
    return "".join(st)
    
def convertBinToDec(num):
    i = 0
    value = 0
    while (num > 0):
        r = num%10
        value += r*(2**i)
        i = i+1
        num = int(num / 10)
    return value


