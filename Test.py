s = "aabbbcccddddeeeee"
mapApp = {}
for char in s:
    mapApp.setdefault(char, 0)
    mapApp[char] += 1

data = [[mapApp[c],c] for c in mapApp.keys()]
for x in range(3):
    print
    data[x][1], data[x][0]

