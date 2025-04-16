# Password Generator
import random
import string

def generate_password(length=12, uppercase=True, numbers=True, special_chars=True):
    """
    Generates a random password with customizable options
    
    Parameters:
    length (int): Length of the password
    uppercase (bool): Include uppercase letters
    numbers (bool): Include numbers
    special_chars (bool): Include special characters
    
    Returns:
    str: Generated password
    """
    
    characters = string.ascii_lowercase
    

    if uppercase:
        characters += string.ascii_uppercase
    if numbers:
        characters += string.digits
    if special_chars:
        characters += string.punctuation
    

    if not characters:
        print("Error: No character types selected.")
        return None
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_strength(password):
    """Evaluates the strength of a password"""
    points = 0
    
    
    if len(password) >= 12:
        points += 3
    elif len(password) >= 8:
        points += 2
    elif len(password) >= 6:
        points += 1
    
    if any(c.isupper() for c in password):
        points += 1
    if any(c.islower() for c in password):
        points += 1
    if any(c.isdigit() for c in password):
        points += 1
    if any(c in string.punctuation for c in password):
        points += 1
    

    if points >= 6:
        return "Strong"
    elif points >= 4:
        return "Medium"
    else:
        return "Weak"

print("Welcome to the Password Generator!")
print("This program creates secure passwords according to your preferences.")

while True:
    print("\nWhat would you like to do?")
    print("1. Generate password")
    print("2. Check password strength")
    print("3. Quit")
    
    choice = input("Your choice (1-3): ")
    
    if choice == "1":
        try:
           
            length = int(input("Password length (recommended: at least 8): "))
            if length < 1:
                print("Length must be at least 1. Setting to default value 12.")
                length = 12
                
            upper = input("Use uppercase letters? (y/n): ").lower() == 'y'
            nums = input("Use numbers? (y/n): ").lower() == 'y'
            special = input("Use special characters? (y/n): ").lower() == 'y'
            
            
            password = generate_password(length, upper, nums, special)
            strength = password_strength(password)
            
            print(f"\nYour generated password: {password}")
            print(f"Strength: {strength}")
            
        except ValueError:
            print("Please enter a valid number for the length.")
            
    elif choice == "2":
        password = input("Enter the password to check: ")
        strength = password_strength(password)
        print(f"Password strength: {strength}")
        
    elif choice == "3":
        print("Goodbye!")
        break
        
    else:
        print("Invalid input. Please choose 1-3.")
