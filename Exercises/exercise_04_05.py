# exercise_04_05.py, Chapter 4, Python Crash Course
#
# Summing a Million: Make a list of the numbers from one 
# to one million, and then use min() and max() to make
# sure your list actually starts at one and ends at one
# million. Also, use the sum() function to see how quickly
# Python can add a million numbers.

list = []

for integer in range(1,1000001):
    list.append(integer)

print("min: " + str(min(list)))
print("max: " + str(max(list)))
print("sum: " + str(sum(list)))



