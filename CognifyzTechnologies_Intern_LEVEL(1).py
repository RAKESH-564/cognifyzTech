# ===================================TASK-1 {String Reversal} =================
# # Function to reverse a string
# def reverse_string(input_string):
#     return input_string[::-1]

# # Taking input from the user
# input_string = input("Enter a string: ")

# # Calling the function and printing the reversed string
# reversed_string = reverse_string(input_string)
# print("Reversed string:", reversed_string)

# ==================================TASK-2 {Temperature Conversion}================

# def convert_celsius_to_fahrenheit(celsius):
#     fahrenheit = (celsius * 9/5) + 32
#     return fahrenheit

# # Function to convert Fahrenheit to Celsius
# def convert_fahrenheit_to_celsius(fahrenheit):
#     celsius = (fahrenheit - 32) * 5/9
#     return celsius


# temperature = float(input("Enter the temperature: "))
# unit = input("Is given temp is celsius or farenheit? (C/F): ").upper()

# # Checking the unit and converting the temperature
# if unit == "C":
#     # Convert Celsius to Fahrenheit
#     result = convert_celsius_to_fahrenheit(temperature)
#     print(f"{temperature}°C is equal to {result}°F.")
# elif unit == "F":
#     # Convert Fahrenheit to Celsius
#     result = convert_fahrenheit_to_celsius(temperature)
#     print(f"{temperature}°F is equal to {result}°C.")
# else:
#     print("Please enter either 'C' for Celsius or 'F' for Fahrenheit.")

# =========================================TASK-3 {: Email Validator}==========================
# def is_valid_email(email):
#     # Check if the email contains exactly one '@' symbol
#     if email.count('@') != 1:
#         return False
    
#     #checking if mail id cannot start with - or @
#     if email[0]=='-' or email[0]=='@':
#         return False

#     # Split the email into local part and domain part
#     local_part, domain_part = email.split('@')

#     #checking punctuation marks are comming consecutively or not
#     if '!!' in email: 
#         return False
    
#     #checking if fullstop is having full stop or not
#     if not '.' in domain_part: 
#         return False

#     #checking length of local name is less than 64 or not
#     if not len(local_part)<=64:
#         return False
    
#     #checking '_' not allowed in domain part
#     if '_' in domain_part:
#         return False

#     # Check if the local part and domain part are non-empty
#     if not local_part or not domain_part:
#         return False

#     # Check if the local part contains only alphanumeric characters and some special characters
#     if not all(char.isalnum() or char in ['.', '_', '-','!','#','$','%','&',"'",'*','+','/','=','?','^','{','}','|','~',','] for char in local_part):
#         return False

#     # Check if the domain part contains at least one '.' and only alphanumeric characters
#     if '.' not in domain_part or not all(char.isalnum() or char == '.' for char in domain_part):
#         return False

#     # Check if the email ends with a valid top-level domain (TLD)
#     if not domain_part.split('.')[-1].isalpha():
#         return False
    
#     # check if the total length of an email address must not exceed 254 characters
#     if not len(email) <= 254:
#         return False
    
#     # Check if '@' symbol is more than 6 characters from the end
#     at_index = email.find('@')
    
#     if not at_index != -1 and (len(email) - at_index) > 6:
#         return False
    
#     # checking if spaces in between
#     if ' ' in email:
#         return False

#     return True

# # Get email input from the user
# user_email = input("Enter a sample email to check whether the email is valid or not ?:: ")

# # Check if the email is valid
# if is_valid_email(user_email):
#     print("Valid.")
# else:
#     print("Invalid.")


# ==================================================TASK-4 {: Calculator Program}======================
# Function for addition
# def add(num1, num2):
#     return num1 + num2

# # Function for subtraction
# def subtract(num1, num2):
#     return num1 - num2

# # Function for multiplication
# def multiply(num1, num2):
#     return num1 * num2

# # Function for division
# def divide(num1, num2):
#     if num2 != 0:  # Checking if denominator is zero
#         return num1 / num2
#     else:
#         return "Error! Division by zero."

# # Function for modulus
# def modulus(num1, num2):
#     return num1 % num2

# # Main program
# print("Basic Calculator")

# # Get two numbers and an operator from the user
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# operator = input("Enter the operator (+, -, *, /, %): ")

# # Perform the operation based on the operator
# if operator == "+":
#     result = add(num1, num2)
#     print(f"The result of {num1} + {num2} is: {result}")
# elif operator == "-":
#     result = subtract(num1, num2)
#     print(f"The result of {num1} - {num2} is: {result}")
# elif operator == "*":
#     result = multiply(num1, num2)
#     print(f"The result of {num1} * {num2} is: {result}")
# elif operator == "/":
#     result = divide(num1, num2)
#     print(f"The result of {num1} / {num2} is: {result}")
# elif operator == "%":
#     result = modulus(num1, num2)
#     print(f"The result of {num1} % {num2} is: {result}")
# else:
#     print("Invalid operator! Please enter +, -, *, /, or %.")
# ==============================================TASK-5 {: Palindrome Checker}======================
# Function to check if a string is a palindrome
def is_palindrome(string):
    # Convert the string to lowercase to avoid case sensitivity
    string = string.lower()

    # Remove spaces to handle phrases with spaces
    string = string.replace(" ", "")

    # Check if the string is equal to its reverse
    if string == string[::-1]:
        return True
    else:
        return False

# Main program
input_string = input("Enter a word or phrase: ")

# Check if the input string is a palindrome
if is_palindrome(input_string):
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")
# ========================================================================================================





