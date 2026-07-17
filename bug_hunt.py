# bug_hunt.py

print("=== Bug Hunt Program ===")

try:
    age = int(input("Enter your age: "))

    years = 10

    future_age = age + years

    print(f"In {years} years you will be {future_age} years old.")

except ValueError:
    print("Invalid input. Please enter a number.")
