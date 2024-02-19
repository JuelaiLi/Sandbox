min_password_length = 8
max_password_length = 16

password = input("Enter a password: ")
while len(password) < min_password_length or len(password) > max_password_length:
    print("Invalid password")
    password = input("Enter a password: ")

print("*" * len(password))
