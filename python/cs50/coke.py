# Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations:
# 25 cents, 10 cents, and 5 cents.
 
# In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time
# informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in 
# change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an
# accepted denomination.

count = 50
print('Amount Due:',count)


while count > 0:
    coin = int(input('Insert Coin:'))
    amount_due = count - coin
    invalid_coin = 0

    if amount_due <= 0:
        change_owed = abs(amount_due)
        print('Change Owed:',change_owed)
        break

    else:
        if coin in [25,10,5]:
            count -= coin
            print('Amount Due:', count)
        else:
            print('Amount Due:', count)



