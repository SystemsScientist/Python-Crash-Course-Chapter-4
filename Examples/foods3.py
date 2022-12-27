# foods3.py, Chapter 4, Python Crash Course
# program adds foods to two different lists
# and then prints both lists. However, this
# program doesn't do what is expected.

my_foods = ['pizza', 'falafel', 'carrot cake']

# This doesn't work
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are: ")
print(my_foods)

print("\nMy friend's favorite foods are: ")
print(friend_foods)



