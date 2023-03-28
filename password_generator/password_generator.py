import random
import string 

def generate_password():
        
    pwd_length = input("How long do you want your password to be?: ")
    if not pwd_length.isdigit():
        print("Please enter a number!")
        generate_password()
    else:
        pwd_length = int(pwd_length)

    

        password = ""
        body = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!$%&()*+,-./:;<=>?@[\]^_{|}#~"
        lower = random.choice("abcdefghijklmnopqrstuvwxyz")
        number = random.choice("0123456789")
        upper = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        special = random.choice("!$%&()*+-/:;<=>?@[\]^_{|}#~")
        password += number + lower + upper + special 
        if pwd_length < 4:
            print("Password must be atleast 4 characters long!")
            generate_password()
        else:
            while len(password) < pwd_length:
                password += random.choice(body)

            print("Your generated password is: ", password)

generate_password()
def repeat():
    another_password = input("Would you like another password? (y/n) " )
    if another_password == "y":
        generate_password()
        repeat()
    elif another_password == "n":
        quit()
    else:
        print("Not a valid option!")
        repeat()

repeat()