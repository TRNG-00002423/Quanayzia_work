


#1. Declare variables of each primitive type: int, float, str, bool, NoneType.

age = 28         
price= 19.99      
name= "Alice"      
is_active = True       
result = None       

#2. Print each variable, its value, and its type using f-strings.
print(f"  age         = {age:<10} (type: {type(age).__name__})")
print(f"  price       = {price:<10} (type: {type(price).__name__})")
print(f"  name        = {name:<10} (type: {type(name).__name__})")
print(f"  is_active   = {is_active:<10} (type: {type(is_active).__name__})")
print(f"  result      = {str(result):<10} (type: {type(result).__name__})")

#3 Demonstrate:
    # Integer division (//) vs. regular division (/)
    # String multiplication ("abc" * 3)
    # Boolean arithmetic (True + True + False)
    # The 0.1 + 0.2 floating-point precision issue

op1=17
op2=5

print("Operators Demo:")
print(f"{op1}//{op2}={op1//op2:<10} (floor division)")
print(f"{op1}/{op2}={op1/op2:<10} (true division)")
print(f'"QA " * 3= {"QA "*3}')
print(f"True + True = {True + True}")

print("Precision Gotcha:")
print(f" 0.1 + 0.2  = { 0.1 + 0.2}       (not exactly 0.3!)")





