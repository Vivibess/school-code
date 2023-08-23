def is_palindrome(number):
    number = str(number)
    if number == number[::-1]:
        return number + " is a palindrome"
    else:
        return number + " is not a palindrome"

while True:
    try:
        number = int(input("Please enter a 3 digit number\n"))
        if number > 99 and number < 1000:
            break
        else:
            print("That's not a 3 digit number, please try again.")
    except ValueError:
        print("That's not a number at all, please try again.")

print(is_palindrome(number))