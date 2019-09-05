#program that finds max int of inputs until negative int is input
number = 0
highest_value = 0

while number >= 0:
    number = int(input("Enter a number"))
    if number > highest_value:
        highest_value = number

print(highest_value)