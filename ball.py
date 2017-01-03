
class ball:
    pos = (8,8)
    impuls = (1,1)
    
    def __init__(self):
        pass
    
    def move(self, field):
        field[self.pos] = 0
        newpos = self.pos + self.impuls
        pass

