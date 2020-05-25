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
    print(rows)
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


symbols = input("Enter cells: > ")
print("---------")
print("| " + symbols[0] + " " + symbols[1] + " " + symbols[2] + " |")
print("| " + symbols[3] + " " + symbols[4] + " " + symbols[5] + " |")
print("| " + symbols[6] + " " + symbols[7] + " " + symbols[8] + " |")
print("---------")
print(findFinalState(symbols))
