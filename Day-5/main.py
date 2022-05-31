import random
import string

letters = list(string.ascii_lowercase)
symbols = ['!','@','#','$','%','^','&','*']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
password = []

print("Random password generator")
letter_count = int(input("How many letters? "))
symbol_count = int(input("How many symbols? "))
number_count = int(input("How many numbers? "))

for x in range(1, letter_count + 1):
    password.append(random.choice(letters))

for x in range(1, symbol_count + 1):
    password.append(random.choice(symbols))

for x in range(1, number_count + 1):
    password.append(random.choice(numbers))

random.shuffle(password)
print(f'New Password: {"".join(password)}')
