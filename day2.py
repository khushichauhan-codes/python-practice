x = int(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))

sum = 0
power = 1

for i in range(1, n + 1):
    power = power * x
    sum = sum + (power / i)

print("Sum of the series is:", sum)
