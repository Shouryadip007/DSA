# variable : string , integer , float , boolean

#string
name = "Deep"
movie = "Inception"
friend = "Neo"

#integer
age = 21
height = 175  
no_of_students = 50

#float
pi = 3.14
temperature = 36.6
gpa = 8.5

#boolean
is_student = True
is_raining = False
is_valid = True

# typecasting
age_str = str(age)          # integer to string
height_float = float(height) # integer to float
gpa_int = int(gpa)          # float to integer



### Input from user and calculating area and perimeter of rectangle
"""
height = float(input("Enter height of rectangle in cm: "))
width = float(input("Enter width of rectangle in cm: "))

print(f"Area of rectangle: {height * width} sq.cm")
print(f"Perimeter of rectangle: {2 * (height + width)} cm")

"""

### Shopping Bill
"""
item = input("Enter item name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

total_price = price * quantity

print(f"You have purchased {item}")
print(f"Total price to be paid: ${total_price} ")

"""


### Compund Interest Calculation
"""
principal = float(input("Enter principal amount: "))    
rate = float(input("Enter rate of interest (in %): "))
time = float(input("Enter time (in years): "))
amount = principal * (1 + rate / 100) ** time
ci = amount - principal

print(f"Compound Interest after {time} years: ${ci}")
print(f"Total amount after {time} years: ${amount}")

"""


# Arithmetic Operations and augmented assignment operators
"""
a = 10

a = a + 5   # addition
a += 5      # augmented assignment for addition
print(a)

a = a - 5   # subtraction
a -= 5      # augmented assignment for subtraction 
print(a)

a = a * 5   # multiplication
a *= 5      # augmented assignment for multiplication
print(a)

a = a / 5   # division
a /= 5      # augmented assignment for division
print(a)

a = a % 5   # modulus
a %= 5      # augmented assignment for modulus
print(a)

a = a ** 5  # exponentiation
a **= 5     # augmented assignment for exponentiation
print(a)

"""

## some math functions 
"""
x = 3.25
y = -5
z = 7

result = round(x)          # rounds to nearest integer
print(result)

result = abs(y)            # returns absolute value
print(result)

result = pow(z, 3)        # z raised to the power 3
print(result)

result = max(x, y, z)     # returns the maximum value
print(result)

result = min(x, y, z)     # returns the minimum value
print(result)

"""

# using math module functions
"""
import math 

print(math.pi)
print(math.e)
print(math.sqrt(16))        # square root
print(math.ceil(4.2))       # rounds up
print(math.floor(4.7))      # rounds down
print(math.factorial(5))    # factorial of a number

"""