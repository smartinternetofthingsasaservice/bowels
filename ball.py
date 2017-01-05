import numpy
import operator

class ball:
    pos = (8, 8)
    impuls = (1, 1)
        
    def __init__(self):
        pass
    
    def move(self, field):
        field[self.pos] = 0
        newpos = tuple(map(operator.add, self.pos, self.impuls))
        
        #TODO collision detection 
        field[newpos] = 1
        self.pos = newpos
        pass

