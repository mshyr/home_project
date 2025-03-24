import random
import string

num_passwords = int(input("How many passwords do you want to generate? ")) 
password_length = int(input("Enter the length of each password: "))
characters = string.ascii_letters + string.digits + string.punctuation

for i in range(num_passwords):
    password = ''.join(random.choice(characters) for _ in range(password_length))
    print("Strong Password", ":", password)
