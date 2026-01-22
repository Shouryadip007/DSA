age = int(input("Enter your age: "))

if age >= 18 and age < 40:
    print("You are an adult.")

elif age >= 40:
    print("You are expired.")

elif age == 0:
    print("You are not born yet.")

else:
    print("You are a minor.")