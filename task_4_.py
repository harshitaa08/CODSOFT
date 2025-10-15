# Password Generator Application
# Internship Task 4 - CODSOFT
# Created by: Harshita Shukla

# This Python program generates strong and random passwords
# based on the user's desired length and complexity.

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("====== PASSWORD GENERATOR ======")

while True:
    try:
        length = int(input("Enter the desired password length: "))
        if length < 4:
            print("Password length should be at least 4 characters for better security.")
            continue
    except ValueError:
        print("Please enter a valid number.")
        continue

    password = generate_password(length)
    print("\nGenerated Password:", password)

    again = input("\nDo you want to generate another password? (yes/no): ").lower()
    if again != 'yes':
        print("\nThank you for using the Password Generator!")
        break
