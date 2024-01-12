###############################################################################
# Word Search
# ######################
#
# A main program to test implementation of the Location and Word classes.
# Requires Location.py and Word.py.
###############################################################################

# import libraries
from Location import Location
from Word import Word
from sys import stdin
from random import sample, choice, randint

# define constants
NUM_WORDS = 5  # how many words to randomly select from the input
GRID_SIZE = 10  # the height/width of the "fictitious" grid

######
# MAIN
######
# read the words from stdin
words = [ ]
# change the file name to test for a different file
fileName = "words.txt"
file = open(fileName, "r")
for line in file:
    # remove the trailing newline and convert to uppercase
    words.append(line.rstrip("\n").upper())

# grab a sampling of the specified number of words
words = sample(words, NUM_WORDS)

# inintialize a list of Word instances
word_objects = [ ]
# for each word, randomly pick an orientation and Location
for word in words:
    # randomly pick an orientation
    orientation = choice(Word.ORIENTATIONS)

    # randomly pick a Location (within the grid)
    row = randint(0, GRID_SIZE - 1)
    col = randint(0, GRID_SIZE - 1)
    location = Location(row, col)

    # append an Word instance of this word
    word_objects.append(Word(word, orientation, location))
    
# display the words
for word in word_objects:
    print(word)

