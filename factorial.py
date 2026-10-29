# Factorial Program in Python (All Methods)

# Function using Recursion
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Input
num = int(input("Enter a number: "))

if num < 0:
    print("Factorial does not exist for negative numbers.")

else:
    # Method 1: Using For Loop
    fact_for = 1
    for i in range(1, num + 1):
        fact_for *= i

    # Method 2: Using While Loop
    fact_while = 1
    i = 1
    while i <= num:
        fact_while *= i
        i += 1

    # Method 3: Using Recursion
    fact_recursive = factorial_recursive(num)

    # Display Results
    print("\nFactorial using For Loop      :", fact_for)
    print("Factorial using While Loop    :", fact_while)
    print("Factorial using Recursion     :", fact_recursive) 