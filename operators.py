# Python Operators Example

a = 10
b = 3

# 1. Arithmetic Operators
print("Arithmetic Operators")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

# 2. Comparison (Relational) Operators
print("\nComparison Operators")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# 3. Assignment Operators
print("\nAssignment Operators")
x = 5
print("x =", x)

x += 2
print("x += 2 ->", x)

x -= 1
print("x -= 1 ->", x)

x *= 3
print("x *= 3 ->", x)

x /= 2
print("x /= 2 ->", x)

x //= 2
print("x //= 2 ->", x)

x %= 2
print("x %= 2 ->", x)

x **= 3
print("x **= 3 ->", x)

# 4. Logical Operators
print("\nLogical Operators")
p = True
q = False

print("p and q:", p and q)
print("p or q:", p or q)
print("not p:", not p)

# 5. Bitwise Operators
print("\nBitwise Operators")
print("a & b:", a & b)
print("a | b:", a | b)
print("a ^ b:", a ^ b)
print("~a:", ~a)
print("a << 1:", a << 1)
print("a >> 1:", a >> 1)

# 6. Membership Operators
print("\nMembership Operators")
numbers = [10, 20, 30, 40]

print("20 in numbers:", 20 in numbers)

print("50 not in numbers:", 50 not in numbers)

print("\nIdentity Operators")
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print("list1 is list2:", list1 is list2)
print("list1 is list3:", list1 is list3)
print("list1 is not list3:", list1 is not list3)