
marks = int(input("Enter your marks: "))

if marks <0:
    print("Invalid marks entered.")
    exit()
elif marks >= 90:
    grade = 'A'
elif marks >= 80:
    grade = 'B'
elif marks >= 70:
    grade = 'C'
elif marks >= 60:
    grade = 'D'
elif marks >= 50:
    grade = 'E'
else:
    grade = 'F'

print(f"Your grade is: {grade}")