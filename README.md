# Turing machine in terminal
```
code = {(0, '1'): ('1', '1', 1), (1, '1'): ('1', 'b', 1), (1, 'b'): ('+', 'b', 1)}
------------------------------------------------------V-------------------------------------------------+----
 ...| b | b | b | b | b | b | b | b | b | b | b | b | 1 | 1 | 1 | 1 | 1 | b | b | b | b | b | b | b | b |...
--------------------------------------------------------------------------------------------------------+----
HEAD pos = 0| DATA = {0: '1', 1: '1', 2: '1', 3: '1', 4: '1'}
f (0, '1') -> ('1', '1', 1)
```
## Usage
- Run a program, for instance`./main.py program-examples/pr1.txt`
- Press enter to move head to the right
- Type h for additional options
