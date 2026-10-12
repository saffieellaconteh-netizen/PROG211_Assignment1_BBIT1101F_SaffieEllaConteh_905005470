"""
Digital Exam & Results Management System
By: Saffie Ella Conteh 905005470

Run with:  python results_system.py
"""


# GRADE SCALE (TUPLE)
# A tuple of tuples: (minimum score, letter grade, grade point).
# A tuple is used because the grading scale is fixed and must not change.

GRADE_SCALE = (
    (80, "A", 4.0),
    (70, "B", 3.0),
    (60, "C", 2.0),
    (50, "D", 1.0),
    (0, "F", 0.0),
)


# CLASS 1: Course
class Course:
    """A course (module) that students sit exams for."""

    course_count = 0  # class attribute: shared by every Course object

    def __init__(self, code, title, credit_hours):
        # Instance attributes: each Course object has its own values
        self.code = code
        self.title = title
        self.credit_hours = credit_hours
        Course.course_count += 1

    # Instance method
    def display_info(self):
        print(f"{self.code:<10}{self.title:<35}{self.credit_hours} credit hours")

    # Class method: works with the class itself, not one object
    @classmethod
    def total_courses(cls):
        return cls.course_count


# CLASS 2: Student
class Student:
    """A student whose exam results are recorded."""

    student_count = 0  # class attribute

    def __init__(self, student_id, programme, semester):
        self.student_id = student_id
        self.programme = programme
        self.semester = semester
        # Dictionary of results: course code -> (Course object, score) tuple
        self.results = {}
        Student.student_count += 1

    # Instance methods
    def add_result(self, course, score):
        """Record a score for a course. Student and Course objects interact here."""
        if not Student.is_valid_score(score):
            print(f"Invalid score {score}. Scores must be between 0 and 100.")
            return False
        self.results[course.code] = (course, score)
        return True

    def calculate_gpa(self):
        """Credit-weighted GPA across all recorded courses."""
        if not self.results:
            return 0.0
        total_points = 0
        total_credits = 0
        for course, score in self.results.values():
            _, grade_point = Student.score_to_grade(score)
            total_points += grade_point * course.credit_hours
            total_credits += course.credit_hours
        return round(total_points / total_credits, 2)

    def update_record(self, programme=None, semester=None):
        """Update programme and/or semester; keeps the old value if None."""
        if programme:
            self.programme = programme
        if semester:
            self.semester = semester

    def display_info(self):
        print(f"Student ID : {self.student_id}")
        print(f"Programme  : {self.programme}")
        print(f"Semester   : {self.semester}")
        if not self.results:
            print("Results    : none recorded yet")
            return
        print(f"{'Code':<10}{'Course':<35}{'Score':>5}  Grade")
        for code, (course, score) in self.results.items():
            letter, _ = Student.score_to_grade(score)
            print(f"{code:<10}{course.title:<35}{score:>5}  {letter}")
        print(f"GPA        : {self.calculate_gpa()}")

    # Class methods
    @classmethod
    def from_string(cls, data):
        """Alternative constructor, e.g. 'LUCT1002, BSc Information Technology, 3'."""
        student_id, programme, semester = data.split(",")
        return cls(student_id.strip(), programme.strip(), int(semester))

    @classmethod
    def total_students(cls):
        return cls.student_count

    @classmethod
    def record_removed(cls):
        """Called when a student is deleted, so the count stays correct."""
        cls.student_count -= 1

    # Static methods 
    @staticmethod
    def is_valid_score(score):
        return 0 <= score <= 100

    @staticmethod
    def score_to_grade(score):
        """Convert a numeric score to (letter, grade point) using GRADE_SCALE."""
        for minimum, letter, grade_point in GRADE_SCALE:
            if score >= minimum:
                return letter, grade_point


# DATA STRUCTURE: one dictionary storing all Student objects
# Key = student ID, Value = Student object
student_records = {}


def add_student(student):
    """Add a Student object to the dictionary. Rejects duplicate IDs."""
    if student.student_id in student_records:
        print(f"A student with ID {student.student_id} already exists.")
        Student.record_removed()  # the object was created but not stored
        return False
    student_records[student.student_id] = student
    return True


def find_student(student_id):
    """Return the Student with this ID, or None if not found."""
    return student_records.get(student_id)


def display_all_students():
    """Loop through the dictionary and display every student."""
    if not student_records:
        print("No student records yet.")
        return
    for student in student_records.values():
        student.display_info()
        print("-" * 60)


def delete_student(student_id):
    """NEW FEATURE: remove a student from the dictionary."""
    if student_id not in student_records:
        print("Student not found.")
        return False
    del student_records[student_id]
    Student.record_removed()
    print(f"Student {student_id} deleted.")
    return True


def show_top_student():
    """NEW FEATURE: find the student(s) with the highest GPA."""
    top_gpa = -1
    top_ids = ""
    for student in student_records.values():
        if not student.results:
            continue  # skip students with no results yet
        gpa = student.calculate_gpa()
        if gpa > top_gpa:
            top_gpa = gpa
            top_ids = student.student_id
        elif gpa == top_gpa:
            top_ids += ", " + student.student_id  # handle a tie

    if top_gpa < 0:
        print("No results recorded yet.")
        return
    print(f"Top-scoring student(s): {top_ids}  (GPA {top_gpa})")


# SAMPLE DATA
def create_courses():
    """Courses stored in a dictionary keyed by course code."""
    return {
        "PROG211": Course("PROG211", "Object-Oriented Programming 1", 3),
        "MATH101": Course("MATH101", "Discrete Mathematics", 3),
        "COMM102": Course("COMM102", "Communication Skills", 2),
    }


def load_sample_data(courses):
    """Shows object creation in two ways and objects interacting."""
    s1 = Student("LUCT1001", "BSc Software Engineering", 3)                # normal constructor
    s2 = Student.from_string("LUCT1002, BSc Information Technology, 3")    # class method constructor
    s3 = Student("LUCT1003", "BSc Business Information Technology", 3)
    add_student(s1)
    add_student(s2)
    add_student(s3)

    s1.add_result(courses["PROG211"], 78)
    s1.add_result(courses["MATH101"], 85)
    s2.add_result(courses["PROG211"], 64)
    s2.add_result(courses["COMM102"], 49)
    s3.add_result(courses["PROG211"], 91)
    s3.add_result(courses["COMM102"], 82)


# USER INTERFACE (text menu)
def read_int(prompt, low, high):
    """Keep asking until the user types a whole number in range (no crashes)."""
    while True:
        text = input(prompt).strip()
        if text.isdigit() and low <= int(text) <= high:
            return int(text)
        print(f"Please enter a whole number from {low} to {high}.")


def show_menu():
    print("\n===== DIGITAL EXAM & RESULTS SYSTEM =====")
    print("1. Add a student")
    print("2. Record an exam score")
    print("3. View all students")
    print("4. View one student")
    print("5. Update a student's programme/semester")
    print("6. Delete a student")
    print("7. Show top-scoring student")
    print("8. List courses")
    print("9. System summary")
    print("0. Exit")


def main():
    courses = create_courses()
    load_sample_data(courses)

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            student_id = input("Student ID: ").strip().upper()
            programme = input("Programme: ").strip()
            semester = read_int("Semester (1-8): ", 1, 8)
            if add_student(Student(student_id, programme, semester)):
                print(f"Student {student_id} added.")

        elif choice == "2":
            student = find_student(input("Student ID: ").strip().upper())
            if not student:
                print("Student not found.")
                continue
            code = input(f"Course code {list(courses)}: ").strip().upper()
            if code not in courses:
                print("Course not found.")
                continue
            score = read_int("Score (0-100): ", 0, 100)
            if student.add_result(courses[code], score):
                letter, _ = Student.score_to_grade(score)
                print(f"Recorded {score} ({letter}) for {code}.")

        elif choice == "3":
            display_all_students()

        elif choice == "4":
            student = find_student(input("Student ID: ").strip().upper())
            if student:
                student.display_info()
            else:
                print("Student not found.")

        elif choice == "5":
            student = find_student(input("Student ID: ").strip().upper())
            if not student:
                print("Student not found.")
                continue
            programme = input("New programme (press Enter to keep current): ").strip()
            semester = read_int("New semester (1-8): ", 1, 8)
            student.update_record(programme or None, semester)
            print("Record updated.")

        elif choice == "6":
            student_id = input("Student ID to delete: ").strip().upper()
            confirm = input(f"Are you sure you want to delete {student_id}? (y/n): ").strip().lower()
            if confirm == "y":
                delete_student(student_id)
            else:
                print("Delete cancelled.")

        elif choice == "7":
            show_top_student()

        elif choice == "8":
            for course in courses.values():
                course.display_info()

        elif choice == "9":
            print(f"Total students: {Student.total_students()}")
            print(f"Total courses : {Course.total_courses()}")

        elif choice == "0":
            print("Goodbye.")
            break

        else:
            print("Invalid option. Please type a number from the menu.")


if __name__ == "__main__":
    main()
