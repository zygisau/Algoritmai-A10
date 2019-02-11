import math

# Declaration and preparation
n = int(input("Enter the number (n) to find all prime numbers in a range from 2 to n: "))
numbers = []
for a in range(2, n+1):
    numbers.append(a)

isPrime = [None] * (n-1)

# Main
for a in range(0, math.trunc(math.sqrt(n))+1):
    if isPrime[a] is None:
        isPrime[a] = 1
        for b in range(a+1, n-1):
            if numbers[b] % numbers[a] == 0:
                isPrime[b] = 0

for a in range(len(isPrime)):
    if isPrime[a] is None:
        isPrime[a] = 1

# Printing
print("Prime numbers are: ")
for a in range(0, n-1):
    if isPrime[a] == 1:
        print(numbers[a])