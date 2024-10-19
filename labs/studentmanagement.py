class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = {}  # Dictionary to store course_name: grade
        self.attendance = {}  # Dictionary to store date: status

    def add_grade(self, course, grade):
        if not isinstance(grade, (int, float)) or grade < 0 or grade > 100:
            raise ValueError("Grade must be a number between 0 and 100")
        self.courses[course] = grade

    def mark_attendance(self, date, status):
        if status not in ['present', 'absent']:
            raise ValueError("Status must be 'present' or 'absent'")
        self.attendance[date] = status

    def get_average_grade(self):
        if not self.courses:
            return 0
        return sum(self.courses.values()) / len(self.courses)

    def get_attendance_percentage(self):
        if not self.attendance:
            return 0
        present_count = sum(1 for status in self.attendance.values() if status == 'present')
        return (present_count / len(self.attendance)) * 100

class StudentManagementSystem:
    def __init__(self):
        self.students = {}  # Dictionary to store student_id: Student_object
        self.courses = set()  # Set to store unique courses

    def add_student(self, student_id, name):
        if student_id in self.students:
            raise ValueError(f"Student with ID {student_id} already exists")
        self.students[student_id] = Student(student_id, name)

    def add_course(self, course_name):
        self.courses.add(course_name)

    def get_top_performers(self, course_name):
        if course_name not in self.courses:
            raise ValueError(f"Course {course_name} does not exist")
        
        # List comprehension with filter
        course_students = [
            (student, student.courses.get(course_name))
            for student in self.students.values()
            if course_name in student.courses
        ]
        
        # Sort using lambda function
        return sorted(course_students, key=lambda x: x[1], reverse=True)

    def get_attendance_report(self, date):
        # Dictionary comprehension
        return {
            student.name: student.attendance.get(date, 'no record')
            for student in self.students.values()
        }

    def export_grades_to_file(self, filename):
        try:
            with open(filename, 'w') as f:
                for student in self.students.values():
                    f.write(f"Student: {student.name} (ID: {student.student_id})\n")
                    for course, grade in student.courses.items():
                        f.write(f"{course}: {grade}\n")
                    f.write("\n")
        except IOError as e:
            print(f"Error writing to file: {e}")

def main():
    # Create an instance of the management system
    sms = StudentManagementSystem()

    try:
        # Add some courses
        courses = ["Python", "Data Structures", "Algorithms"]
        for course in courses:
            sms.add_course(course)

        # Add students
        students_data = [
            (1, "Alice Smith"),
            (2, "Bob Johnson"),
            (3, "Charlie Brown")
        ]

        # Using tuple unpacking in loop
        for student_id, name in students_data:
            sms.add_student(student_id, name)

        # Add grades using exception handling
        grades_data = [
            (1, "Python", 95),
            (1, "Data Structures", 88),
            (2, "Python", 82),
            (2, "Algorithms", 90),
            (3, "Data Structures", 85)
        ]

        for student_id, course, grade in grades_data:
            try:
                student = sms.students[student_id]
                student.add_grade(course, grade)
            except KeyError:
                print(f"Student with ID {student_id} not found")
            except ValueError as e:
                print(f"Error adding grade: {e}")

        # Demonstrate various operations
        print("\nTop performers in Python:")
        for student, grade in sms.get_top_performers("Python"):
            print(f"{student.name}: {grade}")

        # Export grades to file
        sms.export_grades_to_file("grades_report.txt")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()