#PROG 1700 – Tech Check #1
#Variables, Operators, Input/Output & Casting

# Restaurant Bill 
# You will create a console-based Python program that will calculate the amount of the tip, the tax, and the 
# total amount of a restaurant bill. The program will prompt the user to input the original amount of the bill. 
# The program will then output the amount of the tax (15% of the original amount) and a tip (20% of the original amount). 
# Finally, the program will output the new total of the bill.

"""

I was going to implement a error handling function to this but for the sake of simplicity I did not, also assuming the user will not have the ability to enter a negative number or letters into a restaurant bill calculator/pin pad.

but I would have done something like this as I see it as good practice to follow error handling.

total = input("Enter your bill total: ")
try:
    total = float(total)
except ValueError:
    print("Invalid Entery! Please enter a number.")
    return

basicly just taking the try func for this part of code because it is an input that could cause an error, if there is an error it moves it to the except block and in this case is executing only if a ValueError is raised. so a "abc" is entered into a float var. 
then it prints out the error message and makes the user enter a number.

"""


def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    # set your variables to 0 to get clean caclulations and also setting our NS tax to 15%
    total   = 0
    tip     = 0
    tax     = 0.15
    
    # sending a nice little thank you message to the user
    text = input("Thank you for your stay at our restaurant! | Press Enter To Continue:")
    print()

    # asking the user for thir bill total
    total = input("Enter your bill total: ")
    print()

    # asking the user for thir bill total
    tip = input("What percentage of tip would you like to leave? (Ex. 15 for 15%): ")

    # calcs for Tip Amount, Tax Amount, and Total Cost
    tipAmount = float(total) * (float(tip) / 100)
    taxAmount = float(total) * float(tax)
    totalcost = float(tipAmount) + float(total) + float(taxAmount)

    # printing our vals out to the user so they can see their full bill broken down for them
    print()
    print(f"Your Tip Amount is $""{:.2f}".format(tipAmount))
    print(f"Your Tax Amount is $""{:.2f}".format(taxAmount))
    print(f"The Total Cost is $""{:.2f}".format(totalcost))
    print()

    # YOUR CODE ENDS HERE

main()