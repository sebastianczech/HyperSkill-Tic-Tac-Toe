# write your code here
def getRows(symbols):
    rows = []
    rows.append(symbols[0] + symbols[1] + symbols[2])
    rows.append(symbols[3] + symbols[4] + symbols[5])
    rows.append(symbols[6] + symbols[7] + symbols[8])
    rows.append(symbols[0] + symbols[4] + symbols[8])
    rows.append(symbols[2] + symbols[4] + symbols[6])
    rows.append(symbols[0] + symbols[3] + symbols[6])
    rows.append(symbols[1] + symbols[4] + symbols[7])
    rows.append(symbols[2] + symbols[5] + symbols[8])
    # print(rows)
    return rows


def findFinalState(symbols):
    if ("XXX" in getRows(symbols) and "OOO" in getRows(symbols)) \
            or (abs(symbols.count("X") - symbols.count("O")) > 1):
        result = "Impossible"
    elif "XXX" not in getRows(symbols) and "OOO" not in getRows(symbols) \
            and any("_" in t for t in getRows(symbols)):
        result = "Game not finished"
    elif "XXX" not in getRows(symbols) and "OOO" not in getRows(symbols):
        result = "Draw"
    elif "XXX" in getRows(symbols):
        result = "X wins"
    elif "OOO" in getRows(symbols):
        result = "O wins"

    return result


def analyzeCoordinates(symbols, x, y):
    if not (x.isnumeric() and y.isnumeric()):
        print("You should enter numbers!")
        return False
    if not (int(x) in range(1, 4) and int(y) in range(1, 4)):
        print("Coordinates should be from 1 to 3!")
        return False
    matrix = symbolsToMatrix(symbols)
    if matrix[int(x) - 1][int(y) - 1] == 'X' or matrix[int(x) - 1][int(y) - 1] == 'O':
        print("This cell is occupied! Choose another one!")
        return False
    return True


def symbolsToMatrix(symbols):
    matrix = [[0 for x in range(3)] for y in range(3)]
    matrix[0][0] = symbols[6]
    matrix[1][0] = symbols[7]
    matrix[2][0] = symbols[8]
    matrix[0][1] = symbols[3]
    matrix[1][1] = symbols[4]
    matrix[2][1] = symbols[5]
    matrix[0][2] = symbols[0]
    matrix[1][2] = symbols[1]
    matrix[2][2] = symbols[2]
    # print(matrix)
    return matrix


def matrixToSymblos(matrix):
    symbols = ['_' for x in range(9)]
    symbols[6] = matrix[0][0]
    symbols[7] = matrix[1][0]
    symbols[8] = matrix[2][0]
    symbols[3] = matrix[0][1]
    symbols[4] = matrix[1][1]
    symbols[5] = matrix[2][1]
    symbols[0] = matrix[0][2]
    symbols[1] = matrix[1][2]
    symbols[2] = matrix[2][2]
    return symbols


def updateRows(symbols, x, y, symbol):
    matrix = symbolsToMatrix(symbols)
    matrix[int(x) - 1][int(y) - 1] = symbol
    return matrixToSymblos(matrix)


def printSymbols(symbols):
    print("---------")
    print("| " + symbols[0] + " " + symbols[1] + " " + symbols[2] + " |")
    print("| " + symbols[3] + " " + symbols[4] + " " + symbols[5] + " |")
    print("| " + symbols[6] + " " + symbols[7] + " " + symbols[8] + " |")
    print("---------")


def getSymbol(lastSymbol):
    if lastSymbol == "O":
        return "X"
    else:
        return "O"


# symbols = input("Enter cells: > ")
symbols = ['_' for x in range(9)]
printSymbols(symbols)
result = "unkonw"
lastSymbol = "O"

while result != "X wins" and result != "O wins" and result != "Draw":
    coordinates_str = input("Enter the coordinates: > ")
    coordinates_list = coordinates_str.split()
    if len(coordinates_list) > 1:
        while not (analyzeCoordinates(symbols, coordinates_list[0], coordinates_list[1])):
            coordinates_str = input("Enter the coordinates: > ")
            coordinates_list = coordinates_str.split()
        lastSymbol = getSymbol(lastSymbol)
        print("Last symbol" + lastSymbol)
        symbols = updateRows(symbols, coordinates_list[0], coordinates_list[1], lastSymbol)
        printSymbols(symbols)
        result = findFinalState(symbols)
        print(result)
