#Section 1
name = "Rosa"
age = 34
height = 5.5
is_student = False

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))

#Section 2
user_name = input("What is your name? ")
birth_year = int(input("In what year were you born? "))
user_years = 2026 - birth_year
print(f"{user_name}, you've had {user_years} trips around the sun so far.")

#Section 3
first_number = float(input("Enter your first number: "))
second_number = float(input("Enter your second number: "))
product = first_number * second_number
print(f"The product of {first_number} and {second_number} is {product}.")

#Section 4
item = "Pencils"
price = 0.25
quantity = 54
sub_total = price * quantity
tax = sub_total * 0.06
total = sub_total + tax

print("______________________________________")
print()
print("---------------RECEIPT----------------")
print("_______________________________________")
print()
print(f"      Item:         {item}")
print(f"      Price:        ${price}")
print(f"      Quantity:     {quantity}")
print(f"      Subtotal:     ${sub_total:.2f}")
print(f"      Tax:          ${tax:.2f}")
print("--------------------------------------")
print(f"      Total:        ${total:.2f}")
print("______________________________________")

#Section 5
profile_name = input("What's your name? ")
home_town = input("What city are you from? ")
hobby = input("What's your hobby? ")
fun_fact = input("Tell me a fun fact about yourself: ")
profile_birth_year = int(input("In what year were you born? "))
profile_age = 2026 - profile_birth_year

print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print(f"    PROFILE:  {profile_name}")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print(f"Hometown:    {home_town}")
print(f"Hobby:       {hobby}")
print(f"Fun fact:    {fun_fact}")
print(f"Age:         {profile_age}")
