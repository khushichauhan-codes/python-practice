numbers = [2, 3, 5, 2, 8, 2, 3, 5, 5, 5]

most_frequent = numbers[0]
max_count = 0

for num in numbers:
    count = numbers.count(num)

    if count > max_count:
        max_count = count
        most_frequent = num

print("Most Frequent Element:", most_frequent)
print("Frequency:", max_count)
