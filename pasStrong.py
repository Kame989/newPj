import string
'''  Generates a strong password with a mix of uppercase, lowercase,
    digits, and special characters.'''
pw = input().strip() #input as string

'''
string.ascii_letters → 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

string.digits → '0123456789'

'''
has_upper = has_lower = has_digit =has_special = False

for c in pw:
    if c.isupper( ):
        has_upper = True
    elif c.islower( ):
        has_lower= True
    elif c.isdigit( ):
        has_digit = True
    elif c in string.punctuation:
        has_special = True

if len(pw) >= 3 and len(pw) <=20 and has_upper and has_lower and has_digit and has_special:
    print("Valid")
else:
    print("Invalid")
