#program that finds max int of inputs until negative int is input
#after you insert a number, if its higher than the current number it becomes max_int
#max int starts at 0.
num_int = int(input("Input a number: "))    # Do not change this line
max_int = 0
# Fill in the missing code
while num_int >= 0:
    num_int = int(input("Input a number: "))
    if num_int > max_int:
        max_int = num_int

print("The maximum is", max_int)    # Do not change this line