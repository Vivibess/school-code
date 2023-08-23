# BMI is calculated by taking weight divided by the square of your height
# the square can be expressed with the exponentiation operator (height**2) or by multiplying the variable with itself (height*height)
# for this exercise I will use the exponentiation operator

def bmi_calc(weight, height):
    # We only care about the first two decimals, so we multiply the float by 100, convert it to an integer, then divide by 100 again to get a float with 2 decimals exactly.
    # This can also be done using various string formatting methods such as {:.2f}.format(variable) or using f string formatting such as ("%.2f" % variable).
    # But I prefer to take the math approach here.
    # We could only choose to return an integer value in the event of the result being xx.0 with a simple if statement, but this is superfluous in my opinion and will be omitted.
    bmi = weight / (height ** 2)
    bmi = int(bmi * 100)
    bmi = bmi / 100
    return bmi
    
while True:
    try:
        weight = float(input("Please enter your weight in kilos (eg. 68.3)"))
        if weight >= 30 and weight <= 400:
            break
        else:
            print("That doesn't seem to be a realistic weight, please try again.")
    except ValueError:
        print("That doesn't seem to be a valid number, please try again.")

while True:
    try:
        height = float(input("Please enter your height in meters (eg. 1.72)"))
        if height >= 0.5 and height <= 2.5:
            break
        else:
            print("That doesn't seem to be a realistic height, please try again.")
    except ValueError:
        print("That doesn't seem to be a valid number, please try again.")

print("Your BMI is", bmi_calc(weight, height))
