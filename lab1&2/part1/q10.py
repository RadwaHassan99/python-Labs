string = input("Enter a string: ")

num_digits = 0
num_letters = 0


for char in string:
    if char.isdigit():
        num_digits += 1
    elif char.isalpha():
        num_letters += 1

print("Number of digits:", num_digits)
print("Number of letters:", num_letters)
