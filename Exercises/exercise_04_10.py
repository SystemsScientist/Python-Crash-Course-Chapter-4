# exercise_04_10.py, Chapter 4, Python Crash Course
#
# Slices: Using one of the programs you wrote in this chapter,
# add several lines to the end of the program that do the
# following:
#
#   - Print the message, The first three items in the list are:.
#     Then use a slice to print the first three items from that
#     program's list

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("\nHere's the roster of players: ")
for player in players[:]:
    print("\t- " + player.title())

print("\nThe first three players on the roster are: ");
for player in players[0:3]:
    print("\t- " + player.title())

#   - Print the message, Three items from the middle of the list
#     are:. Use a slice to print three items from the middle of
#     the list

print("\nThe middle three players on the roster are: ");
for player in players[1:4]:
    print("\t- " + player.title())

#   - Print the message, The last three items in the list are:.
#     Use a slice to print the last three items in the list

print("\nThe last three players on the roster are: ");
for player in players[2:6]:
    print("\t- " + player.title())

print("\n")


