# exercise_04_07.py, Chapter 4, Python Crash Course
#
# Threes: Make a list of the multiples of 3 from 3 to 30. 
# Use a for loop to print the numbers in your list.

threes = list(range(3,31,3))

for three in threes:
    print("Every Third Number: " + str(three))



