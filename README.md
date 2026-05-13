# Turing machine in terminal
```
code = {(0, '1'): ('1', '1', 1), (1, '1'): ('1', 'b', 1), (1, 'b'): ('+', 'b', 1)}
----------------------------------------------V-----------------------------------------+----
 ...| b | b | b | b | b | b | b | b | b | b | 1 | 1 | 1 | 1 | 1 | b | b | b | b | b | b |...
----------------------------------------------------------------------------------------+----
HEAD pos = 0| DATA = {0: '1', 1: '1', 2: '1', 3: '1', 4: '1'}
f (0, '1') -> ('1', '1', 1)
> 
```
The tape has infinite empty slots.

Program example:
```
0 1 1 1 2 1 3 1 4 1
f ( q0, 1) = (q1, 1, 1)
f ( q1, 1) = (q1, b, 1)
f ( q1, b) = (q+, b, 1)
```
First line represents the tape contents. It's pairs of (index, value). So (0, 1), (1, 1), ... , (4, 1). So in this case the tape has value on 1 in idexes ranging from 0 to 4.

Following lines are operations in the form `f ( qU, x ) = ( qV, y, z)`, where:
1. `qU` is the state with number `U`
2. `X` is the value that happens to be read while in the state `qU`
3. ` f ( qU, X )` means that the machine is currently in the state `qU` and has read value `X`
-

## Usage
- Run a program, for instance`./main.py program-examples/pr1.txt`
- Press enter to move head to the right
- Type h for additional options
