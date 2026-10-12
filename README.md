 Digital Exam & Results Management System

PROG211 Object-Oriented Programming 1, Individual Assignment
Limkokwing University of Creative Technology, Sierra Leone
Author: [Saffie Ella Conteh]  Student ID: [905005470]

Problem
Exam results in many institutions are recorded and calculated by hand, which is slow and error prone. This Python program records exam scores, converts them to letter grades, calculates a credit-weighted GPA, finds the top-scoring student, and lets staff add, update, view and delete student records. It is built with Object-Oriented Programming (OOP) in the Education domain.

How to Run
Requires Python 3.8 or newer. No extra libraries or internet connection needed.

```python results_system.py```

 Features
Menu option and What it does 

1. Add a student: Creates a new Student object and stores it in the dictionary 
2. Record an exam score: Links a Student to a Course with a score (0 to 100) 
3. View all students: Loops through the dictionary and shows every student's results and GPA 
4. View one student: Finds a student by ID and shows their results 
5. Update a student: Changes a student's programme and/or semester 
6. Delete a student: Removes a student after a yes/no confirmation 
7. Show top-scoring student | Finds the student(s) with the highest GPA, including ties 
8. List courses: Shows all courses and their credit hours 
9. System summary: Shows total students and courses using class methods 

 Code Structure
All code is in one file, `results_system.py`, organised into clear sections:
1. Grade scale (tuple): `GRADE_SCALE`, the fixed grading rules
2. `Course` class: course code, title and credit hours
3. `Student` class: student ID, programme, semester and results
4. Data storage: the `student_records` dictionary and functions to add, find, display and delete students and show the top student
5. Sample data: three students and three courses loaded at start-up
6. User interface: the text menu and input validation

 OOP Concepts Used

 Classes, Attributes and Objects
- 'Course': instance attributes 'code', 'title', 'credit_hours'; class attribute 'course_count'.
- 'Student': instance attributes 'student_id', 'programme', 'semester', 'results'; class attribute 'student_count.
- Object creation: students are created with the normal constructor ('Student("LUCT1001", ...)') and with a class method constructor ('Student.from_string("LUCT1002, BSc Information Technology, 3")').
- Object interaction: 'student.add_result(course, score)' takes a 'Course' object, and 'calculate_gpa()' uses that course's 'credit_hours' to weight the GPA.

 Python Data Structures
- Dictionary: 'student_records' stores every Student object with the student ID as the key. 'add_student()' adds records and 'display_all_students()' loops through and displays them.
- Tuples (bonus): 'GRADE_SCALE' is a tuple because the grading scale is fixed and should not change. Each result is stored as a '(course, score)' tuple.

 Methods
 Type and Methods 
 Instance methods  'add_result()', 'calculate_gpa()', 'update_record()', 'display_info()' 
 Class methods ('@classmethod')  'Student.from_string()', 'Student.total_students()', 'Student.record_removed()', 'Course.total_courses()' 
 Static methods ('@staticmethod')  'Student.is_valid_score()', 'Student.score_to_grade()' 

 Digital Public Goods (DPG) Alignment
- Open source: the code is publicly available on GitHub under the MIT License, so anyone can use, study and improve it.
- Inclusive and accessible: a plain-language text menu that runs on any computer with Python, including low-spec machines, and needs no internet. Invalid input (wrong menu choice, letters instead of numbers, scores outside 0 to 100) is handled with clear messages instead of crashes. Student IDs and course codes are accepted in upper or lower case.
- Privacy-respecting: students are identified only by student ID. No names, dates of birth, phone numbers or addresses are stored, and no data is saved to disk. Deleting a student removes their record completely.
- Modular and reusable: the classes, data storage functions and user interface are kept in separate sections, so the `Course` and `Student` classes can be reused in another program (for example, a web app) without changes.

 Example Usage (sample input and output)

Viewing a student (option 4)
'''
Choose an option: 4
Student ID: LUCT1003
Student ID : LUCT1003
Programme : BSc Business Information Technology
Semester : 3
Code      Course                             Score  Grade
PROG211   Object-Oriented Programming 1         91   A
COMM102   Communication Skills                  82   A
GPA        : 4.0

'''Recording a score (option 2)'''
Choose an option: 2
Student ID: LUCT1002
Course code ['PROG211', 'MATH101', 'COMM102']: math101
Score (0-100): 72
Recorded 72 (B) for MATH101.

'''Invalid score is rejected'''
Score (0-100): 150
Please enter a whole number from 0 to 100.
'''

Top-scoring student before and after a delete (options 7 and 6)
'''
Choose an option: 7
Top-scoring student(s): LUCT1003  (GPA 4.0)

Choose an option: 6
Student ID to delete: LUCT1003
Are you sure you want to delete LUCT1003? (y/n): y
Student LUCT1003 deleted.

Choose an option: 7
Top-scoring student(s): LUCT1001  (GPA 3.5)
'''

System summary (option 9)
'''
Choose an option: 9
Total students: 2
Total courses : 3
'''

 Grading Scale
Score, Grade, and Grade point 

 80 to 100  A  4.0 
 70 to 79  B  3.0 
 60 to 69  C  2.0 
 50 to 59  D  1.0 
 0 to 49  F  0.0 

 License
MIT License. Free to use, modify and share.

