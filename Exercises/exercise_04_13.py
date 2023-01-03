# exercise_04_13.py, Chapter 4, Python Crash Course
# 
# Buffet: A buffet-style restaurant offers only five basic foods.
# Think of five simple foods, and store them in a tuple.

buffet_foods = ("sushi", "pasta", "fruit", "burgers", "tacos")

#   - Use a for loop to print each food the restaurant offers.

print("\nBuffet Menu: ")
for food in buffet_foods:
    print("\t- " + food.title())

#   - Try to modify one of the items, and make sure that Python
#     rejects the change

# buffet_foods[0] = "Cake"

#   - The restaurant changes its menus, replacing two of the 
#     items with different foods. Add a block of code that
#     rewrites the tuple, and then use a for loop to print
#     each of the items on the revised menu.

buffet_foods = ("sushi", "pasta", "cake", "tamales", "tacos")
print("\nRevised Buffet Menu: ")
for food in buffet_foods:
    print("\t- " + food.title())

print("\n")


