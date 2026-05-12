# by github.com/mm40

from tape import Tape

# t : the tape to be worked on, p : program executed
def run(t, p):
    done = False
    print(p)
    print(t)
    pre = p.initialize()
    print("f " + str(pre[0]) + " -> " + str(pre[1]))
    while True:
        line = input("> ")
        if len(line) > 0:
            first = line[0]
            
            # quit
            if line == "q":
                break

            # help
            elif line == "h":
                print("q : quit\n<[OFFSET] : move head by OFFSET to the left\n>[OFFSET] : move head by OFFSET to the right\n^POSITION : move head to the position POSITION\n=VALUE : set new VALUE of the field pointed by head\ni : reinitialise (return to q0 with current value)\np : print table")

            # head movement to the left or right
            elif first == '<' or first == '>':
                if len(line) == 1:
                    offset = 1
                else:
                    offset = int(line[1:])
                if first == '<':
                    offset = -offset
                t.moveHeadBy(offset)
                print(t)

            # head movement to specific position
            elif first == '^':
                position = int(line[1:])
                t.moveHeadTo(position)
                print(t)

            elif first == '=':
                value = line[1:]
                t.setCurrentValue(value)
                print(t)

            elif line == "i":
                p.initialize()
                done = False

            elif line == "p":
                print(t)

        else:
            if not done:
                result = p.executeLine()
            else:
                print("Program is finished. If needed, you could set the data and reinitialize. Type h for help")
                continue
            print(t)
            if result[0] == 1:
                print("POSITIVE OUTCOME !")
                done = True
            elif result[0] == -1:
                print("NEGATIVE OUTCOME !")
                done = True
            else:
                print("f "+str(result[1]) + " -> " + str(result[2]))

                
                



            

