import os

laby = []  # We create a empty list

with open("ressource/labyrinthe.txt") as levels:
    for line in levels:  # For every line in our file
        level = []  # We create a another list
        for x in line:
            if x != '\n':
                level.append(x)
            laby.append(level)



