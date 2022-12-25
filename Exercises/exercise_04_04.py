# exercise_04_04.py, Chapter 4, Python Crash Course
#
# One Million: Make a list of the numbers from one to one
# million, and then use a for loop to print the numbers.
# (If the output is taking too long, stop it by pressing
# CTRL-C or by closing the output window.)

list = []

for integer in range(1,1000001):
    list.append(integer)

print(list)



