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


    def __str__(self):
        line1 = line3 = "----"
        line2 = " ..."
        cnt = self._displayWidth// 2
        for i in range(self._headPosition - cnt, self._headPosition + cnt + 1):
            field = self._data.get(i, blancCharacter)
            width = len(field)
            topchar = "-"
            if cnt == 0:
                topchar = "V"
            if width % 2 == 0:
                topchar = "\b" + topchar
            line1 = line1 + "--" + width//2 * '-' + topchar + width//2 * '-' + "-"
            line2 = line2 + "| " + field + " "
            line3 = line3 + "--" + width * "-" + "-"
            cnt = cnt - 1

        print(line1 + "+----")
        print(line2 + "|...")
        print(line3 + "+----")
        return 'HEAD pos = ' + str(self._headPosition) + '| DATA = ' + str(self._data)

    def setData(self, newData):
        self._data = newData

    def getData(self):
        return self._data

    def moveHeadBy(self, offset):
        self._headPosition = self._headPosition + offset

    def moveHeadTo(self, newPosition):
        self._headPosition = newPosition

