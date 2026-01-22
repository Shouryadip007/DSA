unit = input("Enter unit (C for Celsius, F for Fahrenheit): ").upper()
temperature = float(input("Enter temperature: "))

if unit == "C":
    converted_temperature = (temperature * 9/5) + 32
    print(f"{temperature} degrees Celsius is equal to {converted_temperature:.2f} degrees Fahrenheit.")
elif unit == "F":
    converted_temperature = (temperature - 32) * 5/9
    print(f"{temperature} degrees Fahrenheit is equal to {converted_temperature:.2f} degrees Celsius.") 
else:
    print("Invalid unit entered.")