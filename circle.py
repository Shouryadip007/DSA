import math

r = float(input("Enter the radius of the circle: "))

area = math.pi * pow(r, 2)
circumference = 2 * math.pi * r

print(f"Area of the circle: {round(area, 2)} cm^2")
print(f"Circumference of the circle: {round(circumference, 2)} cm")