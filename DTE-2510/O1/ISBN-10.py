def calc_checksum(input):
    checksum = 0
    for i in range(len(str(input))):
        checksum += int(str(input)[i]) * (i+1)
    if checksum % 11 == 10:
        return "X"
    else:
        return checksum % 11

while True:
    try:
        #todo: change input validation to allow for leading zeroes.
        isbn_input = int(input("Please enter the first 9 digits of an ISBN\n"))
        if len(str(isbn_input)) == 9:
            break
        #todo: add check for leading zeroes
        else: 
            print("That's not a valid input, please try again.")
    except ValueError:
        print("That's not a valid input, please try again.")

print("The ISBN-10 number is", str(isbn_input) + str(calc_checksum(isbn_input)))