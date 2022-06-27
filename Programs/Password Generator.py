import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
signs = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

password_list = []
print("Welcome to the Password Generator!")
nr_letters = int(input("How many letters would you in your password? "))
nr_sings = int(input("How many symbols would you in your password? "))
nr_numbers = int(input("How many numbers would you in your password? "))

for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

for char in range(0, nr_sings):
    password_list.append(random.choice(signs))

for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
password = ""
for char in password_list:
    password += char
print(f"Your password is: {password}")