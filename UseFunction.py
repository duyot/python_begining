def show_user_name(user_name: str) -> str:
    """document for this def"""
    print("Hello " + user_name)
    return "Hello World to" + user_name


def double(value: int):
    print("previous value: " + str(value))
    finalValue = value * 2
    print("After value: " + str(finalValue))
    return value, finalValue


def split_and_join(line):
    # write your code here
    return "-".join(line.split(" "))


def count_string_appear(mainStr: str, findStr):
    findStrLength = len(findStr)
    mainStrLength = len(mainStr)
    if mainStrLength < findStrLength:
        return 0
    count = 0
    for i in range(0, mainStrLength + 1 - findStrLength):
        if mainStr[i:(i + findStrLength)] == findStr:
            count += 1
    return count


def filterAlpha(valueInput: str):
    for i in valueInput:
        if not i.isalpha():
            valueInput = valueInput.replace(i, "")
    return valueInput
