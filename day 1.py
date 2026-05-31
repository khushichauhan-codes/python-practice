x = int(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))

sum = 1
power = 1

for i in range(1, n + 1):
    power = power * x
    if i % 2 == 0:
        sum = sum + power
    else:
        sum = sum - power

print("Sum of the series is:", sum)
