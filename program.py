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

