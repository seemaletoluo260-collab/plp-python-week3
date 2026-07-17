# ticket_checker.py

print("=== Ticket Checker ===")

age = int(input("Enter your age: "))

student = input("Are you a student? (yes/no): ").lower()

is_student = student == "yes"

if age < 12:
    print("Child Ticket")

elif age >= 60:
    print("Senior Ticket")

elif is_student:
    print("Student Ticket")

else:
    print("Adult Ticket")
