import sys
import random
import string

password =[]
char_left = -1

def update_char_left(num_of_char):
    global char_left

    if num_of_char < 0 or num_of_char > char_left:
        print("Number of characters out of range ( 0 -", password_length,")")
    else:
        char_left-= num_of_char
        print("Characters left:",char_left)

password_length = int(input("\nWelcome to password generator \nHow many characters do you want your password to have? "))

if password_length < 5:
    print("The password has to be at least 5 characters long.")
    sys.exit(0)
else:
    char_left = password_length

lc_lett = int(input("How many lowercase letters? "))
update_char_left(lc_lett)

up_lett = int(input("How many uppercase letters? "))
update_char_left(up_lett)

sp_char = int(input("How many special characters? "))
update_char_left(sp_char)

dig = int(input("How many digits? "))
update_char_left(dig)

if char_left > 0:
    print("Not all characters were defined. They are considered as lowercase letters.")
    lc_lett += char_left
    
for i in range(password_length):
    if lc_lett > 0:
        password.append(random.choice(string.ascii_lowercase))
        lc_lett -= 1
    if up_lett > 0:
        password.append(random.choice(string.ascii_uppercase))
        up_lett -= 1
    if sp_char > 0:
        password.append(random.choice(string.punctuation))
        sp_char -= 1
    if dig > 0:
        password.append(random.choice(string.digits))
        dig -= 1

random.shuffle(password)

print("\nGenerated password:\n"+"".join(password),"\n")
