#* 📝 Student Record Management System using File I/O
#^ Add, View, Search, Delete student records stored in a text file

def menu():
    print("\n📚 ====== Student Record System ======")
    print("1️⃣  Add Student")
    print("2️⃣  View All Students")
    print("3️⃣  Search Student by Roll No")
    print("4️⃣  Delete Student")
    print("5️⃣  Exit")

while True:
    menu()
    choice = input("🔢 Choose Between (1-5): ")

    #* 1. Add Student
    if choice == '1':
        name = input("👤 Enter Student Name: ")
        roll = input("🆔 Enter Roll Number: ")
        marks = input("📊 Enter Marks: ")

        with open("students.txt", "a") as f:  #* Append mode to add new record
            f.write(f"{name},{roll},{marks}\n")

        print("✅ Student added successfully!")

    #* 2. View All Students
    elif choice == '2':
        try:
            with open("students.txt", "r") as f:
                lines = f.readlines()

            if not lines:
                print("📂 No student records found.")
            else:
                print("\n📋 All Student Records:")
                for line in lines:
                    if line.strip():  #* Avoid blank lines
                        parts = line.strip().split(",")
                        if len(parts) == 3:
                            name, roll, marks = parts
                            print(f"👤 Name: {name} | 🆔 Roll No: {roll} | 📊 Marks: {marks}")
                        else:
                            print("⚠️ Skipping corrupted line:", line.strip())
        except FileNotFoundError:
            print("⚠️ File not found. Please add some students first.")

    #* 3. Search Student by Roll Number
    elif choice == '3':
        roll_search = input("🔍 Enter Roll No to search student: ")
        found = False

        try:
            with open("students.txt", "r") as f:
                for line in f:
                    if line.strip():
                        parts = line.strip().split(",")
                        if len(parts) == 3:
                            name, roll, marks = parts
                            if roll == roll_search:
                                print(f"\n✅ Record Found:\n👤 Name: {name} | 🆔 Roll No: {roll} | 📊 Marks: {marks}")
                                found = True
                                break
            if not found:
                print("❌ No student found with that Roll Number.")
        except FileNotFoundError:
            print("⚠️ File not found. Add some students first.")

    #* 4. Delete Student by Roll No
    elif choice == '4':
        roll_delete = input("🗑️ Enter the Roll No to delete: ")
        found = False

        try:
            with open("students.txt", "r") as f:
                lines = f.readlines()

            with open("students.txt", "w") as f:
                for line in lines:
                    if line.strip():
                        parts = line.strip().split(",")
                        if len(parts) == 3:
                            name, roll, marks = parts
                            if roll != roll_delete:
                                f.write(line)
                            else:
                                found = True
            if found:
                print(f"✅ Student with Roll No {roll_delete} has been deleted.")
            else:
                print("❌ No student found with that Roll Number.")
        except FileNotFoundError:
            print("⚠️ File not found. Add some students first.")

    #* 5. Exit
    elif choice == '5':
        print("👋 Exiting Program. Bye Hafiz!")
        break

    else:
        print("❌ Invalid choice! Please select from 1 to 5.")
