import os

# Create package
os.makedirs("MyPackage", exist_ok=True)

# Create __init__.py
with open("MyPackage/__init__.py", "w") as f:
    f.write("")

# Create calculator.py module
with open("MyPackage/calculator.py", "w") as f:
    f.write("""
def add(a, b):
    return a + b

def sub(a, b):
    return a - b
""")

# Use package
from MyPackage.calculator import add, sub

print("Addition:", add(10, 20))
print("Subtraction:", sub(20, 10))