import math

# Decimal to binary

def dec_to_binary(num):
    #print(int(math.log2(num)))
    bin = ""
    temp_num = int(num)
    if temp_num % 2 == 1:
        bin = "1" + bin
        temp_num -= 1
    else: 
        bin = "0" + bin
    for i in range(int(math.log2(num)), 0, -1):
        #print(2**i)
        print(i)
        if temp_num % 2**(i+1) == 0:
            print(2**(i+1))
            #print(temp_num % 2**(i+1) == 0)
            bin = "1" + bin

        elif temp_num // 2**i == 0:
            bin = "0" + bin
        
        #print(bin)
        #print(2**(i+1))
        #print("Temp_num %", 2**i+1, "is")
        #print(temp_num % 2**i+1)

num = 64

dec_to_binary(num)