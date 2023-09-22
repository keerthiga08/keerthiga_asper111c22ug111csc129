class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Example usage:
student1 = Student("Alice", "101", 3.7)
student2 = Student("Bob", "102", 3.9)
student3 = Student("Charlie", "103", 3.5)
student4 = Student("David", "104", 4.0)

students = [student1, student2, student3, student4]

sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")