# init
vowels = set()
temp = {"3", "4", "4"}

strInput = input("Please enter input: ")
setUniqueChar = set()
for character in strInput:
    if character != " ":
        setUniqueChar.add(character)

print("List of unique char in your string: " + "".join(setUniqueChar))

word = "hello world"
print("".join(vowels.union(set(word))))
print("".join(vowels.difference(set(word))))
print("".join(vowels.intersection(set(word))))


# sample
def average(array) -> int:
    a = set()
    for i in array:
        a.add(i)
    return sum(a) / len(a)


b = [3, 5, 6, 3, 2, 2]
print(str(average(b)))

#
a, b = [set(input().split()) for _ in range(4)][1::2]
print(*sorted(a ^ b, key=int), sep="\n")

#
n, a, b = [set(input().split()) for _ in range(4)][1:4]
temp = [(i in a) - (i in b) for i in n]
print(sum(temp))