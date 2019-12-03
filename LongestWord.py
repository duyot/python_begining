value = input()
table = str.maketrans(dict.fromkeys("~!@#$%^&*()-_+={}[]:;'<>?/,.|`"))
value = value.translate(table)
valuesArr = value.split(sep=" ")

longestWord = max(valuesArr, key=len)

print(longestWord)

