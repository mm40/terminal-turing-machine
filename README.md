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

## Usage
- Run a program, for instance`./main.py program-examples/pr1.txt`
- Press enter to move head to the right
- Type h for additional options

## Program example:
```
0 1 1 1 2 1 3 1 4 1
f ( q0, 1) = (q1, 1, 1)
f ( q1, 1) = (q1, b, 1)
f ( q1, b) = (q+, b, 1)
```
First line represents the tape contents. It's pairs of (index, value). Like this - (0, 1), (1, 1), ... , (4, 1). So in this case the tape has value of 1 in idexes ranging from 0 to 4.

Following lines are operations in the form `f ( qU, x ) = ( qV, y, z)`, where:
1. `qU` is the state with number `U`
2. `x` is the value that happens to be read while in the state `qU`
3. ` f ( qU, x )` means "when machine is in the state `qU` and has read value `x`"

The left side of `=` is the given state, and the right side of `=` is the state that machine will move to from the given state.

4. `qV` is the state with number `V`
5. `y` is the value that will be written to the tape. Could be `1` or `b`
6. `z` is by how many places to the right will the head move. Could be `0`, `1`, `-1`, or any other value

So, when machine is in state `qU`, and the value under its head is `x`, it will overwrite that value to `y`, move the head by `z` to the right, and it's new state will be `qV`.

7. `q+` is a special state, meaning the program has executed successfully.
8. `q-` is the same but for failure.
