# by github.com/mm40

displayWidth = 25
blancCharacter = 'b'

class Tape:
    def __init__(self, headPosition=0):
        # data is content of the tape in format index:"value"
        # where index is zero-based position on tape, and value content on that position
        self._data={}
        self._headPosition = headPosition
        self._displayWidth = displayWidth

