import sys

# 1. Ask the user for their name
name=input("Hello, what is your name?")

# 2. Ask for their role (e.g., "QA Engineer")
role= input("What is your role? ")

# 3. Print a greeting using an f-string:
#    "Welcome, {name}! Your role is {role}."
print(f"Welcome, {name}! Your role is {role}.")

# 4. Print the current Python version (hint: import sys)
print(sys.version)

