# pasword genrator program
import random
import string

def generate_password(length=12):
    # Define the characters to use for the password
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Ensure the password contains at least one character from each category
    password = [
        random.choice(string.ascii_uppercase),  # At least one uppercase letter
        random.choice(string.ascii_lowercase),  # At least one lowercase letter
        random.choice(string.digits),           # At least one digit
        random.choice(string.punctuation)       # At least one special character
    ]
    
    # Fill the rest of the password length with random characters
    password += random.choices(all_characters, k=length-4)
    
    # Shuffle the password list to make it random
    random.shuffle(password)
    
    # Join the password list into a string
    return ''.join(password)

# Example usage
password = generate_password(12)
print(f"Generated password: {password}")

# string.ascii_letters: Includes all lowercase and uppercase letters.
# string.digits: Includes digits (0-9).
# string.punctuation: Includes special characters like !@#$%^&*().
# The random.choice() function ensures at least one character from each type.
# The password is shuffled for randomness and then joined into a single string.

