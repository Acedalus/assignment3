print("ISQA 3900 Lumber Price Calculator")
answer = "y"
while answer == "y":
    print("Please input how much feet of board and of what board type you want (common or rare)")
#print("Enter number of board feet:  ")
    #while True:
    quantity = int(input("Enter amount of board feet desired: "))
    if quantity > 0:
        amount = quantity
    else:
        print("Try entering your amount again.")

        #quantity = int(input("Enter number of board feet: "))

#quantity = input("Enter number of board feet:  ")
    print(quantity)
    #while wType != 1 or wType != 2:
    wType = int(input("Enter 1 for common wood or 2 for rare wood"))
    if wType == 1 or wType == 2:
        cost = wType

    else:
        print("Try selecting the type again.")

        #wType = int(input("Enter 1 for common wood or 2 for rare wood"))

    totalPrice = cost * quantity
    tenPercent = totalPrice / 10
    if totalPrice <= 10000:
        print("The total price is:")
        print(totalPrice)
    elif totalPrice > 10000 and totalPrice < 50000:
#    tenPercent = totalPrice / 10
        ten = totalPrice - tenPercent
        print("The total price is: ")
        print(ten)
    elif totalPrice > 50000:
        twenty = totalPrice - (tenPercent + tenPercent)
        print("The total prince is:")
        print(twenty)
        #print("Do you want to continue? (y/n): ")
    answer = input("Do you want to continue? (y/n): ")
    if answer == "y":#answer.equals(string('y')):
        pass
    elif answer == "n":#answer.equals(string('n')):
        break
    else:
        print("That's neither a yes or a no, try again please")
        answer = string(input())
print("exit")

#wType = input("Enter 1 for common wood or 2 for rare wood")
