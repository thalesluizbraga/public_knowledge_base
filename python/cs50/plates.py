# In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car, with 
# your choice of letters and numbers instead of random ones. Among the requirements, though, are:

# “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an 
# acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”
# In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of 
# the requirements or Invalid if it does not. Assume that any letters in the user’s input will be uppercase. 
# Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it 
# does not. Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call 
# (e.g., one function per requirement).

# def main():
    # plate = input("Plate: ")
    # if is_valid(plate):
        # print("Valid")
    # else:
        # print("Invalid")

# def is_valid(s):
    # ...
 
# main()


def len_plate(plate):
    if len(plate) <= 6:
        return plate
    
def contains_letter(plate):
    count = 0
    for i in plate:
        if i.isalpha():
            count += 1
            if count >= 2:
                return plate
            
def starts_with_letter(plate):
    if plate[0:1].isalpha():
        return plate
    else:
        return 'Invalid'

def numbers_at_the_end(plate):
    if plate[-1].isdigit() and int(plate[-2]) != 0:
        return 'Valid'
    
    return 'Invalid'

def punctuation(plate):
    marks = ['.', '!', '?', '...']
    for char in plate:
        if char in marks:
            return 'Invalid'
    return 'Valid'


if __name__ == '__main__':
    plate = input('Input a plate:').upper().strip()
    if len_plate(plate) == 'Invalid' \
    or contains_letter(plate) == 'Invalid' \
    or starts_with_letter(plate) == 'Invalid' \
    or numbers_at_the_end(plate) == 'Invalid' \
    or punctuation(plate) == 'Invalid':    
        print('Invalid')
    
    else:
        print('Valid')