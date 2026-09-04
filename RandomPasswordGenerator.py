# random password generator
import random
import string

password = ""

# randomly chosen length in range, wider range = more secure password
length = random.randint(16, 64)

# list of characters that can be included in password
character = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890?!@#$%&*+-=/"

# pick a number of random characters equal to randomly chosen length
for i in range(length):
    password += random.choice(character)

print("Randomly generated password:", password)
    
