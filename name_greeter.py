# name_greeter.py

full_name = input("Enter your first and last name: ")

parts = full_name.split()

if len(parts) >= 2:
    first_name = parts[0]
    last_name = parts[1]

    print(f"\nHello, {first_name}!")
    print(f"Your last name is {last_name}.")
    print(f"Welcome, {first_name} {last_name}!")
else:
    print("Please enter both your first and last name.")
