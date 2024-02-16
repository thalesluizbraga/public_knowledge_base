# Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations:
# 25 cents, 10 cents, and 5 cents.
 
# In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time
# informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in 
# change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an
# accepted denomination.

def counter(amount_rule, amount_due):

    while amount_due < 50:
            amount_owed = amount_rule - amount_due
            coin = int(input('Insert a coin: '))
        
            if coin not in [25,10,5]:
                print('Moeda nao aceita, insira outra')
            else:
                amount_due += coin
                if amount_due > amount_rule:
                    print(f'Amount Due: {amount_rule}')
                    print(f'Amount Owed: {amount_owed}')
                else:
                    print(f'Amount Due:{amount_due}')
        
    
if __name__ == '__main__':
    amount_due = 0
    amount_rule = 50
    counter(amount_rule, amount_due)

