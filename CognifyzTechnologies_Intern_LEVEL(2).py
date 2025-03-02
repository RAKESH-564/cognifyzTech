# =============================================TASK-1{Guessing Game}=======================================
# import random

# # Generate a random number between 1 and 100
# secret_number = random.randint(1, 100)

# print("welcome to number guessing game: ")
# print("I have selected a number between 1 and 100. Try to guess it!")

# while True:
#     # Taking user input
#     guess = int(input("Enter your guess: "))
    
#     # Checking if the guess is correct
#     if guess < secret_number:
#         print("Too low! Try again.")
#     elif guess > secret_number:
#         print("Too high! Try again.")
#     else:
#         print("Congratulations! You guessed the correct number.")
#         break
# ===========================================TASK-2{Number Guesser}==============================================
# import random

# # Ask the user for the range
# low = int(input("Enter the lower value : "))
# high = int(input("Enter the upper value: "))

# # Generate a random number within the specified range
# secret_number = random.randint(low, high)

# print(f"I have selected a number between {low} and {high}. Try to guess it!")

# while True:
#     # Taking user input
#     guess = int(input("Enter your guess: "))
    
#     # Checking if the guess is correct
#     if guess < secret_number:
#         print("Too low! Try again.")
#     elif guess > secret_number:
#         print("Too high! Try again.")
#     else:
#         print("Congratulations! You guessed the correct number.")
#         break
# ========================================================TASK-3{Password Strength Checker}==============================
# import re

# def check_password_strength(password):
#     # Checking length
#     if len(password) < 8:
#         return "Weak: Password should be at least 8 characters long."
    
#     # Checking uppercase letters
#     if not any(char.isupper() for char in password):
#         return "Weak: Password should have at least one uppercase letter."
    
#     # Checking lowercase letters
#     if not any(char.islower() for char in password):
#         return "Weak: Password should have at least one lowercase letter."
    
#     # Checking digits
#     if not any(char.isdigit() for char in password):
#         return "Weak: Password should have at least one number."
    
#     # Checking special characters
#     if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
#         return "Weak: Password should have at least one special character."
    
#     return "Strong: Your password is strong!"

# # Taking user input
# user_password = input("Enter your password: ")

# # Checking password strength
# print(check_password_strength(user_password))
# ====================================================================TASK-4{Fibonacci Sequence}========================
# def fibonacci(n):
#     # First two terms of Fibonacci sequence
#     a, b = 0, 1
    
#     # List to store the sequence
#     sequence = []
    
#     for _ in range(n):
#         sequence.append(a)  # Add the current term to the list
#         a, b = b, a + b  # Move to the next terms
    
#     return sequence

# # Taking user input
# num_terms = int(input("Enter the number of terms: "))

# # Checking if the input is valid
# if num_terms <= 0:
#     print("Please enter a positive integer.")
# else:
#     print("Fibonacci sequence:", fibonacci(num_terms))
# ===================================================================TASK-5{File Manipulation}==============================
def count_words(filename):
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            text = file.read()
        
        # Convert text to lowercase and split into words
        words = text.lower().split()
        
        # Dictionary to store word counts
        word_count = {}
        
        # Count occurrences of each word
        for word in words:
            word = word.strip(".,!?()[]{}:;\"'")  # Remove punctuation
            if word:
                word_count[word] = word_count.get(word, 0) + 1
        
        # Sort words alphabetically
        sorted_words = sorted(word_count.items())
        
        # Display word counts
        for word, count in sorted_words:
            print(f"{word}: {count}")
    
    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")

# Taking filename input from user
filename = input("Enter the filename: ")
count_words(filename)
# =================================================================================
