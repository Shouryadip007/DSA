import math

h = float(input("Enter the height of the right triangle: "))
b = float(input("Enter the base of the right triangle: "))

hypotenuse = math.sqrt(pow(h, 2) + pow(b, 2))

print(f"Hypotenuse of the right triangle: {round(hypotenuse, 2)} cm")