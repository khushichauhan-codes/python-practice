print("===== EVEN ODD COUNTER =====")

numbers = [12, 5, 8, 19, 22, 7, 10]

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even Numbers:", even_count)
print("Odd Numbers:", odd_count)
