# Python Functions - Sep 4, 2025
# Defining a simple function
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# Function with default argument
def power(base, exponent=2):
    return base ** exponent

print("Square of 5:", power(5))
print("Cube of 3:", power(3, 3))

# Function with multiple return values
def min_max(numbers):
    return min(numbers), max(numbers)

nums = [4, 7, 1, 9, 3]
mn, mx = min_max(nums)
print("Min:", mn, "Max:", mx)

# Recursive function (factorial again for practice)
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print("Factorial of 6:", factorial(6))

# Lambda function
double = lambda x: x * 2
print("Double of 7:", double(7))

# Higher-order function (passing function as argument)
def apply_func(f, value):
    return f(value)

print("Applying double on 10:", apply_func(double, 10))
