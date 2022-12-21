# exercise_04_02.py, Chapter 4, Python Crash Course
#
# Animals: Think of at least three different animals
# that have a common characteristic. Store the names
# of these animals in a list, and then use a for loop
# to print out the name of each animal.

animal_list = ['dog', 'pig', 'cat']
for animal in animal_list:
    print(animal.title())

# - Modify your program to print a statement about each
#   animal, such as "A dog would make a great pet."

animal_list = ['dog', 'pig', 'cat']
for animal in animal_list:
    print("A " + animal.title() + " would make a great pet.")

# - Add a line at the end of your program stating what
#   these animals have in common. You could print a 
#   sentence such as "Any of these animals would make a 
#   great pet!"

animal_list = ['dog', 'pig', 'cat']
for animal in animal_list:
    print("A " + animal.title() + " would make a fantastic pet.")

print("Any of these animals would make an awesome pet!")



