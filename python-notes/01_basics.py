# Python Basics - Sep 3, 2025
# Variables & Data Types
x, y = 10, 20
print("Sum:", x + y)

# Conditionals
if x > y:
    print("x is greater")
else:
    print("y is greater")

# Loops
for i in range(1, 6):
    print("Loop:", i)

# Function
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print("Factorial of 5:", factorial(5))
