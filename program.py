# by github.com/mm40

from tape import Tape

class Program:
    def __init__(self, dataTape, code={}):
        self._code = code
        self._dataTape = dataTape

    def __str__(self):
        return 'code = ' + str(self._code)

        
