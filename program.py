# by github.com/mm40

from tape import Tape

class Program:
    def __init__(self, dataTape, code={}):
        self._code = code
        self._dataTape = dataTape

    def __str__(self):
        return 'code = ' + str(self._code)

    def textLineToCode(self, line):
        # input string is in format :
        # (qi, aj) = (qi', aj', r) 
        # where qi = current state, aj = value of the field at which the head points on the tape
        # qi' = new state to which to go to
        # aj' = new value that is written in the field at which the head points on the tape
        # r = either 1 or -1 : direction to which the head moves
        left = line.strip().split("=")[0].strip()
        qi = int(left.split(",")[0].strip()[1:].strip()[1:])
        aj = left.split(",")[1].strip()[:-1].strip()

        right = line.strip().split("=")[1].strip()
        # qip is not int, because it can also be q+ and q-
        qip = right.split(",")[0].strip()[1:].strip()[1:]
        ajp = right.split(",")[1].strip()
        r = int(right.split(",")[2].strip()[:-1].strip())

        self._code[(qi, aj)] = (qip, ajp, r)

    def initialize(self):
        self._state = 0
        self._current = (self._state, self._dataTape.getCurrentValue())
        self._next = self._code[self._current]

        return (self._current, self._next)

    def executeLine(self):
        # Executes a line of code. Returns -1 for negative outcome, 1 for positive outcome, and 0 if program hasn-t ended
        c = self._current
        n = self._next
        t = self._dataTape

        self._state = n[0]
        t.setCurrentValue(n[1])
        t.moveHeadBy(n[2])

        self._current = n        
        if n[0] == '+': # positive program outcome
            return (1, None, None)
        elif n[0] == '-': # negative negative program outcome
            return (-1, None, None)
        else:
            self._next = self._code[int(n[0]), t.getCurrentValue()]
            #return (0,self._current, self._next)
            return (0,(n[0], t.getCurrentValue()), self._next)
        
