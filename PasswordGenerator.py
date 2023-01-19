import random
import string

print("hello, it is a Password Generator")

#input the length of password
length = int(input("\nEnter the length of password: "))

#define data
lower = string.ascii_lowercase #(abcdefg...z)
upper = string.ascii_uppercase #(ABCDEFG...Z)
num = string.digits #(01234...9)

#combine the data
all = lower + upper + num

#create our password list
random_list = []

for i in range(length):
    #use random to pick one random character from "all"
    temp = random.choice(all)

    #create the password adding the character temp to the list "random_list"
    random_list.append(temp)

#changing list to string
password = "".join(random_list)
print("Your password is: "+ password)