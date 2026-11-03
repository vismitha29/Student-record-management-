# Student Record Management System
# NeoStark - Python Fundamentals Task

students = [
    {
        "name": "Dass",
        "age": 20,
        "department": "CSE",
        "marks": [78, 85, 72],
        "attendance": 91
    },
    {
        "name": "Chandra",
        "age": 21,
        "department": "CSE",
        "marks": [65, 71, 68],
        "attendance": 84
    },
    {
        "name": "Parvathi",
        "age": 20,
        "department": "ECE",
        "marks": [45, 52, 48],
        "attendance": 72
    }
]

PASS_MARK = 40
ATTENDANCE_LIMIT = 75


def calculate_average(student):
    """Return the average of a student's marks."""
    return sum(student["marks"]) / len(student["marks"])


def check_result(student):
    """Return PASS if the student's average is at least PASS_MARK."""
    return "PASS" if calculate_average(student) >= PASS_MARK else "FAIL"


def display_students():
    print("\n--- ALL STUDENTS ---")
    for student in students:
        print(f"\nName: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Department: {student['department']}")
        print(f"Marks: {student['marks']}")
        print(f"Average: {calculate_average(student):.1f}")
        print(f"Attendance: {student['attendance']}%")
        print(f"Result: {check_result(student)}")


def find_top_performer():
    topper = max(students, key=calculate_average)
    print("\n--- TOP PERFORMER ---")
    print(f"Name: {topper['name']}")
    print(f"Average: {calculate_average(topper):.1f}")


def filter_by_attendance(limit=ATTENDANCE_LIMIT):
    print(f"\n--- STUDENTS WITH ATTENDANCE BELOW {limit}% ---")
    matches = [s for s in students if s["attendance"] < limit]
    if matches:
        for student in matches:
            print(f"{student['name']} - {student['attendance']}%")
    else:
        print("No students found.")


def filter_by_average(limit=50):
    print(f"\n--- STUDENTS WITH AVERAGE BELOW {limit} ---")
    matches = [s for s in students if calculate_average(s) < limit]
    if matches:
        for student in matches:
            print(f"{student['name']} - {calculate_average(student):.1f}")
    else:
        print("No students found.")


def display_class_summary():
    all_marks = [mark for student in students for mark in student["marks"]]
    class_average = sum(all_marks) / len(all_marks)

    print("\n--- CLASS SUMMARY ---")
    print(f"Total Students: {len(students)}")
    print(f"Average Class Mark: {class_average:.1f}")
    find_top_performer()
    filter_by_attendance()

    print("\n--- STUDENT RESULTS ---")
    for student in students:
        print(f"{student['name']} - {check_result(student)}")


def main():
    display_students()
    find_top_performer()
    filter_by_attendance()
    filter_by_average()
    display_class_summary()


if __name__ == "__main__":
    main()
