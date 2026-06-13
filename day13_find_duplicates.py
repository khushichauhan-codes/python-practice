numbers = [1, 2, 3, 4, 2, 5, 6, 3, 7, 8, 1]

duplicates = []

for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print("Duplicate Elements:", duplicates)
