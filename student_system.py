
records = [
    ["Aman", "Math", 88],
    ["Priya", "Physics", 91],
    ["Rahul", "Math", 76],
    ["Sneha", "Chemistry", 84],
    ["Karan", "Math", 92],
    ["Meera", "Physics", 85],
    ["Rohit", "Chemistry", 79],
    ["Anita", "Math", 95],
    ["Vikas", "Physics", 73],
    ["Neha", "Chemistry", 89]
]


def add_student(name, subject, marks):
    for r in records:
        if r[0] == name and r[1] == subject:
            print("Duplicate record found. Student already exists for this subject.")
            return

    records.append([name, subject, marks])
    print("Student added successfully.")


def get_toppers(subject):
    subject_students = [r for r in records if r[1].lower() == subject.lower()]

    if not subject_students:
        print("No records found for this subject.")
        return

    sorted_students = sorted(subject_students, key=lambda x: x[2], reverse=True)

    toppers = sorted_students[:3]

    print(f"\nTop students in {subject}:")
    for t in toppers:
        print(t)


def class_average(subject):
    marks = [r[2] for r in records if r[1].lower() == subject.lower()]

    if not marks:
        print("No records found.")
        return

    avg = sum(marks) / len(marks)
    print(f"Average marks in {subject}: {avg:.2f}")


def above_average_students():
    all_marks = [r[2] for r in records]

    overall_avg = sum(all_marks) / len(all_marks)

    above_avg = [r for r in records if r[2] > overall_avg]

    print(f"\nOverall class average: {overall_avg:.2f}")
    print("Students scoring above average:")

    for student in above_avg:
        print(student)


def remove_student(name):
    global records

    before_count = len(records)

    records = [r for r in records if r[0].lower() != name.lower()]

    after_count = len(records)

    if before_count == after_count:
        print("Student not found.")
    else:
        print("Student records removed.")


# Save records to file
def save_to_file():
    with open("students.txt", "w") as f:
        for r in records:
            line = f"{r[0]},{r[1]},{r[2]}\n"
            f.write(line)

    print("Records saved to students.txt")


# Menu System
def menu():

    while True:

        print("\n----- Student Management System -----")
        print("1 Add student")
        print("2 Show toppers")
        print("3 Show class average")
        print("4 Show above-average students")
        print("5 Remove student")
        print("6 Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            subject = input("Enter subject: ")
            marks = int(input("Enter marks: "))

            add_student(name, subject, marks)

        elif choice == "2":
            subject = input("Enter subject(Math, Physics, Chemistry): ")
            get_toppers(subject)

        elif choice == "3":
            subject = input("Enter subject: ")
            class_average(subject)

        elif choice == "4":
            above_average_students()

        elif choice == "5":
            name = input("Enter student name to remove: ")
            remove_student(name)

        elif choice == "6":
            save_to_file()
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    menu()