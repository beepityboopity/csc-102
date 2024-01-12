#####################
# Program 1
# Word Class
# ###################
# 9/11/2023
#####################

class Word:
    
    ORIENTATIONS = ["HR", "HL", "VD", "VU", "DRD", "DRU", "DLD", "DLU"]
    
    def __init__(self, word, orientation=None, location=None):
        self.word = word
        self.orientation = orientation
        self.location = location
        
    @property
    def word(self):
        return self._word
    @word.setter
    def word(self, value):
        self._word = value
        
    @property
    def orientation(self):
        return self._orientation
    @orientation.setter
    def orientation(self, value):
        self._orientation = value
        
    @property
    def location(self):
        return self._location
    @location.setter
    def location(self, value):
        self._location = value
          
    def __str__(self):
        return "{}/{}@{}" .format(self.word, self.orientation, self.location)
    