#####################
# Program 1
# Location Class
# ##################
# 9/11/2023
#####################

class Location:
    
    def __init__(self, row=0, col=0):
        self.row = row
        self.col = col
        
    @property
    def row(self):
        return self._row

    @row.setter
    def row(self, value):
        if value >= 0:
            self._row = value
        else:
            self._row = 0
        
    @property
    def col(self):
        return self._col

    @col.setter
    def col(self, value):
        if value >= 0:
            self._col = value
        else:
            self._col = 0
        
    def __str__(self):
        return "({},{})" .format(self.row, self.col)
