text = input("Enter a string: ")

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("\nCharacter Frequency:")

for key, value in frequency.items():
    print(key, ":", value)



OUTPUT:
Enter a string: khushi

Character Frequency:
k : 1
h : 2
u : 1
s : 1
i : 1
