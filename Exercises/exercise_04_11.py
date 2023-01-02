# exercise_04_11.py, Chapter 4, Python Crash Course
#
# My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
# (page 60). Make a copy of the list of pizzas, and call it friend_pizzas.

favorite_pizzas = ['pepperoni', 'cheese', 'vegetarian']
friend_pizzas = favorite_pizzas[:]

print("\nMy favorite pizzas are: ")
for pizza in favorite_pizzas[:]:
    print("\t- " + pizza.title())

print("\nMy friend's favorite pizzas are: ")
for pizza in friend_pizzas[:]:
    print("\t- " +pizza.title())

# Then, do the following:
#   - Add a new pizza to the original list.

favorite_pizzas.append('meat lovers')

#   - Add a different pizza to the list friend_pizzas.

friend_pizzas.append('sausage')

#   - Prove that you have two separate lists. Print the message. "My
#     favorite pizzas are:", and then use a for loop to print the
#     first list. Print the message, "My Friend's favorite pizzas are:",
#     and then use a for loop to print the second list. Make sure each
#     new pizza is stored in the appropriate list.

print("\nMy updated favorite pizzas are: ")
for pizza in favorite_pizzas[:]:
    print("\t- " + pizza.title())

print("\nMy updated friend's favorite pizzas are: ")
for pizza in friend_pizzas[:]:
    print("\t- " + pizza.title())

print("\n")



