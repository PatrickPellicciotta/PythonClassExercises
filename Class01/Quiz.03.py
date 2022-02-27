'''
QUIZ #3
Name: Patrick Pellicciotta
ID: 2210211

Follow the instructions in the comments below. Then upload this file, with your answers, to Omnivox.
'''
# 1. In a new line, with a new command, add a string to this list
games = ["Gloomhaven", "Radlands", "Ethnos", "Res Arcana", "Spirit Island", "Bloc by Bloc"]

games.append("League Of Legends")

# 2. Loop through the list and print out all string longer than 7.

for game in games:
    if len(game) > 7:
        print(game)



# 3. Create a function that takes in one number and counts backwards from that number to 0 (printing out each number as it goes)

# I put in two -1 so that it would count down to 0

def count_backwards(num):
    for i in range(num, -1, -1):
        print(i)

# 4. Create a function that takes in a string and returns a list with every other letter in that string

def every_second_letter(string):
    new_list = []
    for i in range(0, len(string), 2):
        new_list.append(string[i])

    return new_list

# 5. Call the functions you created in questions 3 and 4

count_backwards(10)

print(every_second_letter("Portugal"))