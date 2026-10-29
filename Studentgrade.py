Students=[]
grades=[]

while True:
    print("\n1.Add 2.Update 3.Remove 4.Average  5.High/low 6.Exit")
    choice=int(input("Enter your choice:"))

if choice==1:
    students.append(input("Name:"))
    grades.append(int(input("Grade:")))

elif choice==2:
    name =input("Name:")
    if name in students:
        i=student.index(name)
        grades[i] =int(input("New Grade:"))
elif choice==3:

    name =input("Name:")
    if name in students:
        i = students.index(name)
        students.pop(i)
        grades.pop(i)
elif choice ==4:
    print("Average =", sum(grades) / len(grades))
elif choice == 5:
        print("Highest =", max(grades))
        print("Lowest =", min(grades))

elif choice == 6:
     breakpoint
    
else:
        print("Invalid Choice")
    