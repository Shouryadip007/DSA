# Weight conversion calculator

weight = float(input("Enter weight: "))
unit = input("Enter unit (K for kilograms, L for pounds): ").upper()

if unit == "K":
    converted_weight = weight * 2.20462
    print(f"{weight} kilograms is equal to {converted_weight:.2f} pounds.")

elif unit == "L":
    converted_weight = weight / 2.20462
    print(f"{weight} pounds is equal to {converted_weight:.2f} kilograms.")

else:
    print("Invalid unit entered.")