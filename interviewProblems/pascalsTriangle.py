
def getRow(rowIndex):
    """
    i-th row and j-th column.
    Recursive Relation -> f(i, j) = f(i-1, j-1) + f(i-1, j)
    Base case -> f(i, j) = 1 where j = 1 or i = j
    :param rowIndex: (int) index to compute
    :return:
    """
    cache = dict()
    def getNum(rowIndex, columnIndex):
        """
        Recursively find solution. Cache it in dict.
        :param rowIndex:
        :param columnIndex:
        :return:
        """
        rowCol = (rowIndex, columnIndex)
        if cache.get(rowCol):
            return cache[rowCol]
        if columnIndex == 0 or rowIndex == 0 or rowIndex == columnIndex:
            cache[rowCol] = 1
            return 1
        cache[rowCol] = getNum(rowIndex - 1, columnIndex - 1) + getNum(rowIndex - 1, columnIndex)
        return cache[rowCol]

    arr = []

    for columnIndex in range(0, rowIndex + 1):
        arr.append(getNum(rowIndex, columnIndex))

    return arr


def getRowPython(rowIndex):
    """
    Fast
    :param rowIndex:
    :return:
    """
    row = [1]
    for _ in range(rowIndex):
        row = [x + y for x, y in zip([0] + row, row + [0])]
    return row

def test_cache():
    getRow(15)

def test_pythonic():
    getRowPython(15)

if __name__ == "__main__":
    test_cache()
