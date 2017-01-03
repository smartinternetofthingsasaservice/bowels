import sys, time, numpy
from constants import constants
from ball import ball
from output import output

def main(argv):
    print('This is Bowel!')
    
    gameBall = ball()
    cmdOut = output()
    
    
    field = numpy.zeros((constants.SIZE,constants.SIZE))
    
    while True:
        
        gameBall.move(field)
        cmdOut.update(field)
        time.sleep(1)

if __name__ == "__main__":
    main(sys.argv)
