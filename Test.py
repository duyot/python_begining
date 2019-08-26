# n = int(input())
# setN = set(map(int, input().split()))
# m = int(input())
# setM = set(map(int, input().split()))
#
# finalSet = setN.difference(setM).union(setM.difference(setN))
# for i in sorted(finalSet):
#   print(i)

n = int(input())
temp = dict()
for i in range(n):
    inputStr = input()
    temp.setdefault(inputStr, 0)
    temp[inputStr] += 1

print(len(temp))
print(*temp.values(), sep=" ")
