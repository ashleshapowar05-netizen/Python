# File Handling in Python

# 1. Open file and write data
file = open("student.txt", "w")

file.write("Name: Ashlesha\n")
file.write("Course: Computer Engineering\n")
file.write("Subject: Python\n")

file.close()
print("File closed after writing.")

# 2. Open file and read data using read()
file = open("student.txt", "r")

data = file.read()
print("\nData using read():")
print(data)

file.close()

# 3. Open file using with statement
with open("student.txt", "r") as file:
    print("Data using with open:")
    print(file.read())

# 4. Read data using readlines()
with open("student.txt", "r") as file:
    lines = file.readlines()

print("Data using readlines():")
for line in lines:
    print(line, end="")