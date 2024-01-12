###############################################################################
# Word Search
#
# Solution for the programming assignment Word Search (part 3).
# Requires Word.py and Grid.py.
###############################################################################

# import libraries
from Word import Word
from Grid import Grid
from sys import stdin
from random import sample, choice

# define constants
NUM_WORDS = 25              # how many words to randomly select
GRID_SIZE = 25              # the height/width of the grid
DISPLAY_SOLUTION = True     # display the solution?

######
# MAIN
######
# read the words from stdin
words = [ ]
file = open("animals.txt")
for line in file:
    # remove the trailing newline and convert to uppercase
    words.append(line.rstrip("\n").upper())

# grab a sampling of the specified number of words
words = sample(words, NUM_WORDS)

# initialize the grid
grid = Grid(GRID_SIZE)
# process the words
for word in words:
    # randomly select an orientation for the current word
    orientation = choice(Word.ORIENTATIONS)

    # position the word at the chosen orientation in the grid
    grid.position(word, orientation)

# display stats (i.e., "Successfully placed X of Y words.")
print("Successfully placed {} of {} words.\n".format(len(grid.words), len(words)))

# display the grid
print(grid)
print()

# display the words
grid.print_words()
print()

#grid.prettyprint_words()
#print()

# if specified, display the solution
if DISPLAY_SOLUTION:
    grid.print_solution()

