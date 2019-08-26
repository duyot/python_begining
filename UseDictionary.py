user1 = {"username": "ongtheduy", "password": "updated password", "password2": "new password"}
#add
user1["cando"] = True
#remove
removedItem = user1.pop("cando")
#update
user1["cando"] = False
#get
candoValue = user1["cando"]

for k, v in user1.items():
    print(k, ": ", v)

# print(user1["password"])

#######
n = int(input())
temp = dict()
for i in range(n):
    inputStr = input()
    temp.setdefault(inputStr, 0)
    temp[inputStr] += 1

print(len(temp))
print(*temp.values(), sep=" ")
