def convertToTitle(columnNumber: int):
    title = []
    while columnNumber > 0:
        columnNumber -= 1
        title.append(chr(columnNumber % 26 + ord('A')))
        columnNumber = columnNumber // 26
    return "".join(title[::-1])


        


print(convertToTitle(701))