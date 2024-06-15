# A software company sells a package that retails for $99.
# Quantity discounts are given according to the following table:
#       Quantity        Discount
#       10-19           20%
#       20-49           30%
#       50-99           40%
#       100 or more     50%
# Write a program that asks the user to enter the number of packages purchased.
# The program should then display the amount of the discount (if any) and the
# total amount of the purchase after the discount.

# variables
twenty_percent = 0.2
thirty_percent = 0.3
forty_percent = 0.4
fifty_percent = 0.5
price_per_package = 99

# ask the user for the number of packages purchased and cast the input to an int
packages_purchased = int(input("How many software packages did you purchase?\n"))

# input validation for if the user enters a number less than 1
if (packages_purchased < 1):
    print("\nHmm... There must be some mistake. Did you purchase at least 1 software package?")
    packages_purchased = int(input("If yes, enter the number of software packages you purchased here: \n"))

# display the discount amount and total purchase price after the discount
if (packages_purchased >= 1 and packages_purchased <= 9):
    total_without_discount = packages_purchased * price_per_package
    print(f"\nYour total is ${total_without_discount:.2f}")
    print("You will be eligible for a discount starting at 20% if you purchase 10 or more packages!")
    
elif (packages_purchased >= 10 and packages_purchased <= 19):
    amount_saved = packages_purchased * price_per_package * twenty_percent
    print(f"\nYou've earned a {twenty_percent*100:.0f}% discount and saved ${amount_saved:.2f}!")
    total_after_discount = (packages_purchased * price_per_package) * (1 - twenty_percent)
    print(f"Your total after the discount is ${total_after_discount:.2f}")

elif (packages_purchased >= 20 and packages_purchased <= 49):
    amount_saved = packages_purchased * price_per_package * thirty_percent
    print(f"\nYou've earned a {thirty_percent*100:.0f}% discount and saved ${amount_saved:.2f}!")
    total_after_discount = (packages_purchased * price_per_package) * (1 - thirty_percent)
    print(f"Your total after the discount is ${total_after_discount:.2f}")

elif (packages_purchased >= 50 and packages_purchased <= 99):
    amount_saved = packages_purchased * price_per_package * forty_percent
    print(f"\nYou've earned a {forty_percent*100:.0f}% discount and saved ${amount_saved:.2f}!")
    total_after_discount = (packages_purchased * price_per_package) * (1 - forty_percent)
    print(f"Your total after the discount is ${total_after_discount:.2f}")

elif (packages_purchased >= 100):
    amount_saved = packages_purchased * price_per_package * fifty_percent
    print(f"\nYou've earned a {fifty_percent*100:.0f}% discount and saved ${amount_saved:.2f}!")
    total_after_discount = (packages_purchased * price_per_package) * (1 - fifty_percent)
    print(f"Your total after the discount is ${total_after_discount:.2f}")