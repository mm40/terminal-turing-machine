#!/usr/bin/python3

# by github.com/mm40

import sys
    
from tape import Tape
from input import run
from program import Program

def readFile(path, destProgram, destTape):
    result = {}
    with open(path, "r") as lines:
        for line in lines:
            # line example "f ( q0, 1) = (q1, 1, 1)"
            line = line.strip()
            if len(line) > 0:
                if  line[0] == 'f': # function
                    destProgram.textLineToCode(line[1:])
                elif line[0] != '#': # data
                    toggle = False
                    index = 0
                    for part in line.split(" "):
                        if toggle:
                            result[index] = part
                        else:
                            index = int(part)
                        toggle = not toggle
                    destTape.setData(result)



def main():
    t1 = Tape()
    if len(sys.argv) > 2:
        t1.setDisplayWidth(int(sys.argv[2]))
    p1 = Program(t1)
    readFile(sys.argv[1], p1, t1)
    run(t1, p1)

if __name__ == "__main__":
    main()
