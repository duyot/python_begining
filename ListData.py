vowels = ["a", "e", "i", "o", "u", "u"]

vowels.remove("u")
vowels.pop(1)
vowels.extend(["k", "j"])
vowels.insert(0, "add through insert")
dup_vowel = vowels.copy()
print(dup_vowel)
print(vowels)

word = input("Please provide the word to check vowel: ")
found = []
for character in word:
    if character in vowels:
        if character not in found:
            found.append(character)

if len(found) > 0:
    for i in found:
        print(i)
else:
    print("Not found any vowel")
