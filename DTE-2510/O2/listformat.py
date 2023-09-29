def items():
    stuff = []
    while True:
        thing = input("Enter an item (blank to quit): ")
        if thing == "":
            break
        else:
            stuff.append(thing)
    return stuff

def listformat(items):
    if len(items) == 0:
        print("You did not input any items.")
    elif len(items) == 1:
        print("The item is", items[0])
    else:
        # we will make use of string concatenation here
        string = "The items are"
        for i in range(0, len(items)):
            if i == len(items) - 1:
                string = string + " and " + items[i]
            else:
                # the comma is included up to and including the penultimate item as we use the oxford comma here
                string = string + " " + items[i] + ","
        print(string)

items = items()
listformat(items)