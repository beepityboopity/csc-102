######################
# Program 2
# Grid Class
# ####################
# 9/18/2023
######################

# import libraries
from Location import Location
from Word import Word
from random import randint

# the Grid class
# a Grid has a size (the same for both width and height), a grid of letters, and Word instances that are within the Grid


class Grid:
    # class variables
    # the character representing a "blank" letter in the grid
    BLANK = "."
    # the max number of tries to position a word
    MAX_TRIES = 1000

    # the constructor
    def __init__(self, size=25):  # set the _size instance variable
        self.size = size
        self.grid = []
        self.words = []
        for x in range(self.size):  # initialize the grid
            self.grid.append([])
            for y in range(self.size):
                self.grid[x].append(Grid.BLANK)

    # getters/setters
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value <= 0:
            self._size = 25
        else:
            self._size = value

    @property
    def grid(self):
        return self._grid

    @grid.setter
    def grid(self, value):
        self._grid = value

    @property
    def words(self):
        return self._words

    @words.setter
    def words(self, value):
        self._words = value

    # tries to position a word at the specified orientation in the grid
    def position(self, word, orientation):
        # set the default min and max row and col
        min_row = 0
        max_row = self._size - 1
        min_col = 0
        max_col = self._size - 1

        # tweak the row and col values based on the orientation
        if orientation == "HR":
            max_col = self._size - len(word)
        elif orientation == "HL":
            min_col = self._size - 1
        elif orientation == "VD":
            max_row = self._size - len(word)
        elif orientation == "VU":
            min_row = self._size - 1
        elif orientation == "DRD":
            max_col = self._size - len(word)
            max_row = self._size - len(word)
        elif orientation == "DRU":
            max_col = self._size - len(word)
            min_row = self._size - 1
        elif orientation == "DLD":
            min_col = self._size - 1
            max_row = self._size - len(word)
        elif orientation == "DLU":
            min_col = self._size - 1
            min_row = self._size - 1

        # create the Word instance
        word = Word(word, orientation)

        # select a random location based on the min and max values
        loc = Location(randint(min_row, max_row), randint(min_col, max_col))
        # check if this location works up to the specified maximum number of tries
        tries = 0
        while not self._check(word, loc):
            # stop trying if we've reached the specified maximum number of tries
            if tries == Grid.MAX_TRIES:
                return
            # select a new random location
            loc = Location(randint(min_row, max_row), randint(min_col, max_col))
            # note the attempt
            tries += 1
        # update the word's location
        word.location = loc
        # position the word in the grid at the location
        self._position(word)
        # and add it to the list of words
        self._words.append(word)

    # checks if a word can be positioned as specified
    def _check(self, word, loc):
        # the starting row and col for the word
        row = loc.row
        col = loc.col

        # check if the word fits for the specified orientation
        for letter in word.word:
            # abort if we don't encounter a space or the appropriate letter
            if not self._grid[row][col] in [Grid.BLANK, letter]:
                return False
            # change the row and col based on the orientation
            if word.orientation == "HR":
                col += 1
            elif word.orientation == "HL":
                col -= 1
            elif word.orientation == "VD":
                row += 1
            elif word.orientation == "VU":
                row -= 1
            elif word.orientation == "DRD":
                col += 1
                row += 1
            elif word.orientation == "DRU":
                col += 1
                row -= 1
            elif word.orientation == "DLD":
                col -= 1
                row += 1
            elif word.orientation == "DLU":
                col -= 1
                row -= 1

        # otherwise, all the letters fit!
        return True

    # positions a word as specified
    def _position(self, word):
        # the starting row and col for the word
        row = word.location.row
        col = word.location.col

        # position the word
        for letter in word.word:
            # place the current letter
            self._grid[row][col] = letter
            # change the row and col based on the orientation
            if word.orientation == "HR":
                col += 1
            elif word.orientation == "HL":
                col -= 1
            elif word.orientation == "VD":
                row += 1
            elif word.orientation == "VU":
                row -= 1
            elif word.orientation == "DRD":
                col += 1
                row += 1
            elif word.orientation == "DRU":
                col += 1
                row -= 1
            elif word.orientation == "DLD":
                col -= 1
                row += 1
            elif word.orientation == "DLU":
                col -= 1
                row -= 1

    # prints the words
    def print_words(self):
        self.words.sort()
        for word in self._words:
            print(word)

    # prints the solution
    def print_solution(self):
        print(self.__str__(False))

    # return a string representation of the grid
    def __str__(self, fill=True):
        grid = ""
        for row in range(self._size):
            for col in range(self._size):
                # if no letter exists at row,col
                if self._grid[row][col] == Grid.BLANK and fill:
                    # add a random one
                    grid += "{:2}".format(chr(randint(65, 90)))
                else:
                    grid += "{:2}".format(self._grid[row][col])
            grid += "\n"
        # remove the trailing newline
        grid = grid.rstrip("\n")

        return grid

