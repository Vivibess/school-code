import math
# importing math is unnecessary if using bin(), we do not use it so we import math for the log2 function

# Decimal to binary
# I wanted to do this assignment without making use of the built-in bin() function, just for fun.
# You could easily solve this by doing bin(num) and removing the prefix '0b' and returning that.

def dec_to_binary(num):
    # decimal 0 is binary 0
    if num == 0:
        return "0"
    bin = ""
    temp_num = int(num)

# the first bit can only be 1 or 0, so we check if the number is odd, if it is then the first bit is 1. we append this later
    if temp_num % 2 == 1:
        first_bit = "1"
        temp_num -= 1
    else:
        first_bit = "0"

# range here is log2 of the input as we then get how many powers of 2 the number fits into, which is what binary is.
    for i in range(int(math.log2(num)), 0, -1):
        bin =  bin + str(temp_num // 2**i)
        if temp_num > 0:
            temp_num %= 2**i

# appending the first bit
    bin = bin + first_bit 
    return bin

# standard input validation
while True:
    try:
        num = int(input("Please enter a number between 0 and 15\n"))
        if num >= 0 and num <= 15:
            break
        else:
            print("That's not a number within the specified range, please try again.")
    except ValueError:
        print("That is not a valid input, please try again.")

# giving the user the output as specified in the assignment outline
print("The binary number for", num, "is", dec_to_binary(num))