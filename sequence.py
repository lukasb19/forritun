#Design an algorithm that generates the first n numbers in the following sequence:
# ; 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …
#The way the algorithm works is you add the current number with the last 2 numbers in the algorithm
#That way you get the next number

n = int(input("Enter the length of the sequence: ")) # Do not change this line

if n == 1:
    print(1)
elif n == 2:
    print(1)
    print(2)
elif n == 3:
    print(1)
    print(2)
    print(3)
current_int = 3
previous_int = 2
last_int = 1
n -= 3             #withdraw 3 from n because I already set the first 3 numbers in the sequence

if n > 0:
    print(last_int) 
    print(previous_int) 
    print(current_int)
for i in range(n):
    #I add last 2 ints to the current int, make that the current int
    #then i make the last int be previous int, and previous int be current int before it was changed
    current_int, previous_int, last_int = current_int + previous_int + last_int, current_int, previous_int
    print(current_int)
