import secrets
import string

lower_letters = string.ascii_lowercase
upper_letters = string.ascii_uppercase
numbers = string.digits
specials = string.punctuation

def main():
    length = get_length()
    global charset
    charset = get_charset()
    password = get_password(length, charset)

    print(f"=" * 50)
    print(f"Your password is: {password}")
    print(f"=" * 50)
            

def get_length():
    while True:
        try:
            length = int(input("Length of password (Atleast four): "))
            if length <= 3:
                raise ValueError
            return length
        except ValueError:
            print("Invalid length!")
            continue

def validate_yes_no(prompt):
    while True:
        try:
            result = input(prompt).strip().lower()
            if result not in ['yes', 'y', 'no', 'n']:
                raise ValueError
            return result 
        except ValueError:
            print("Invalid Input!")
            continue

def get_charset():
    charset = lower_letters
    want_upper = validate_yes_no("Include upper case letters? (y/n): ")
    want_number = validate_yes_no("Include numbers? (y/n): ")
    want_special = validate_yes_no("Include special characters? (y/n): ")

    if want_upper in ['yes', 'y']:
        charset += upper_letters
    if want_number in ['yes', 'y']:
        charset += numbers
    if want_special in ['yes', 'y']:
        charset += specials
    return charset

def get_count():
    count = 0
    default_pwd = "" 

    if upper_letters in charset:
        default_pwd += secrets.choice(upper_letters)
        count += 1
    if numbers in charset:
        default_pwd += secrets.choice(numbers)
        count += 1
    if specials in charset:
        default_pwd += secrets.choice(specials)
        count += 1
    if lower_letters in charset:
        default_pwd += secrets.choice(lower_letters)
        count += 1
        
    return [default_pwd, count]
    
def get_password(n, charset):
    ls = get_count()
    pwd = ls[0]
    for _ in range(n-int(ls[1])):
        char = secrets.choice(charset)
        pwd += char
    return pwd

if __name__ == '__main__':
    main()