# magicians5.py, Chapter 4, Python Crash Course
# program uses a for loop to print a list of names
# of magicians. 
#
# In addition, the program produces a logical error
#

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
print("I can't wait to see your next trick, " + magician.title() + ".\n")



