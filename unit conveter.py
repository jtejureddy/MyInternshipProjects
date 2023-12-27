def temperature_converter():
  try:
    choice = input("Enter 'C' to convert from Celsius to Fahrenheit, or 'F' to convert from Fahrenheit to Celsius: ")
    if choice.upper() == 'C':
      celsius = float(input("Enter temperature in Celsius: "))
      fahrenheit = (celsius * 9/5) + 32
      print(f"{celsius} Celsius = {fahrenheit:.2f} Fahrenheit")
    elif choice.upper() == 'F':
      fahrenheit = float(input("Enter temperature in Fahrenheit: "))
      celsius = (fahrenheit - 32) * 5/9
      print(f"{fahrenheit} Fahrenheit = {celsius:.2f} Celsius")
    else:
      print("Invalid choice. Please enter 'C' or 'F'.")
  except ValueError:
    print("Invalid input. Please enter a numerical value.")

def length_converter():
  try:
    choice = input("Enter 'm' to convert from meters to feet, or 'f' to convert from feet to meters: ")
    if choice.lower() == 'm':
      meters = float(input("Enter length in meters: "))
      feet = meters * 3.281
      print(f"{meters} meters = {feet:.2f} feet")
    elif choice.lower() == 'f':
      feet = float(input("Enter length in feet: "))
      meters = feet / 3.281
      print(f"{feet} feet = {meters:.2f} meters")
    else:
      print("Invalid choice. Please enter 'm' or 'f'.")
  except ValueError:
    print("Invalid input. Please enter a numerical value.")

def weight_converter():
  try:
    choice = input("Enter 'kg' to convert from kilograms to pounds, or 'lb' to convert from pounds to kilograms: ")
    if choice.lower() == 'kg':
      kilograms = float(input("Enter weight in kilograms: "))
      pounds = kilograms * 2.205
      print(f"{kilograms} kilograms = {pounds:.2f} pounds")
    elif choice.lower() == 'lb':
      pounds = float(input("Enter weight in pounds: "))
      kilograms = pounds / 2.205
      print(f"{pounds} pounds = {kilograms:.2f} kilograms")
    else:
      print("Invalid choice. Please enter 'kg' or 'lb'.")
  except ValueError:
    print("Invalid input. Please enter a numerical value.")

while True:
  print("\nChoose a converter:")
  print("1. Temperature Converter")
  print("2. Length Converter")
  print("3. Weight Converter")
  print("4. Exit")

  choice = input("Enter your choice: ")

  if choice == '1':
    temperature_converter()
  elif choice == '2':
    length_converter()
  elif choice == '3':
    weight_converter()
  elif choice == '4':
    break
  else:
    print("Invalid choice. Please try again.")
