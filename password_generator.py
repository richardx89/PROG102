import random
import string

def password_generator(lenght):
    #define data (types of characters)
    lower = string.ascii_lowercase #(abcdefg...z)
    upper = string.ascii_uppercase #(ABCDEFG...Z)
    num = string.digits #(01234...9)

    #combine the data (all the characters)
    all = lower + upper + num

    #create our random characters list
    random_list = []

    #filling random_list
    for i in range(length):
        #use random.choise to pick one random character from "all"
        temp = random.choice(all)

        #create the password adding the character "temp" to the list "random_list"
        random_list.append(temp)

    #changing list to string
    password = "".join(random_list)
    return password

#To encrypt the password
def password_encryption(password):
    password_encrypt = password[::-1]
    return password_encrypt     
#To save the encrypted password in a file .txt
def save_password(password_encrypted):
    with open("pass.txt","w") as file:
        file.write(password_encrypted)
#It is to recover the last password created
def password_recovery():
    with open("pass.txt", "r") as file:
        password = file.read()
        recovered = password[::-1]
        return recovered


print("hello, it is a Password Generator\nFor password recovery press 1\nTo create a new password press 2")
option = int(input())

if option == 1:
    print(f"Your password is {password_recovery()}")
elif option == 2:
    length = 0
    #validation for the input
    while length < 3 or length > 13:
    #input the length of password
        length = int(input("\nEnter a valid length of password, it must be a value between 3 and 13: "))

    key = password_generator(length)
    key_encrypted = password_encryption(key)
    save_password(key_encrypted)
    print(f"Your password is {key}")


