# exercise_04_06.py, Chapter 4, Python Crash Course
#
# Odd Numbers: Use third argument of the range() function
# to make a list of odd numbers from 1 to 20. Use a for
# loop to print each number.

odd_numbers = list(range(1,21,2))

for odd_number in odd_numbers:
    print("odd number: " + str(odd_number))



