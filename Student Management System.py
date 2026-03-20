students = []

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # 1. Add Student
    if choice == "1":
        name = input("Enter student name: ")
        
        m1 = int(input("Enter marks 1: "))
        m2 = int(input("Enter marks 2: "))
        m3 = int(input("Enter marks 3: "))

        student = {
            "name": name,
            "marks": [m1, m2, m3]
        }

        students.append(student)
        print("Student added successfully!")

    # 2. View Students
    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            for s in students:
                total = sum(s["marks"])
                avg = total / 3

                print("\nName:", s["name"])
                print("Marks:", s["marks"])
                print("Total:", total)
                print("Average:", avg)

    # 3. Search Student
    elif choice == "3":
        search_name = input("Enter name to search: ")
        found = False

        for s in students:
            if s["name"].lower() == search_name.lower():
                total = sum(s["marks"])
                avg = total / 3

                print("\nStudent Found!")
                print("Name:", s["name"])
                print("Marks:", s["marks"])
                print("Total:", total)
                print("Average:", avg)

                found = True
                break

        if not found:
            print("Student not found.")

    # 4. Exit
    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")