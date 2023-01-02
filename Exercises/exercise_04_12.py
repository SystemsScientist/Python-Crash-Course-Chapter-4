# exercise_04_12.py, Chapter 4, Python Crash Course
#
# More Loops: All versions of foods.py in this section have
# avoided using for loops when printing to save space. Choose
# a version of foods.py, and write two for loops to print each
# list of foods.

# Reference foods2.py in the Examples directory

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy favorite foods are: ")
for food in my_foods[:]:
    print("\t- " + food.title())

print("\nMy friend's favorite foods are: ")
for food in friend_foods[:]:
    print("\t- " + food.title())

print("\n")



