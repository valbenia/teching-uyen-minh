class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}, Honor Student: {self.is_honor_student()}")

    def is_honor_student(self):
        return self.grade == "A"
        
class School:
    def __init__(self, name, students = []):
        self.name = name
        self.students = students

    def add_student(self, name, age, grade):
        new_student = Student(name, age, grade)
        self.students.append(new_student)
    
    def add_students(self, student: Student):
        self.students.append(student)

    def display_students(self):
        for student in self.students:
            student.show_info() 

my_school = School("Sunrise School")
my_school.add_student("Alice", 12, "A")
my_school.add_student("Bob", 13, "B")
my_school.display_students()
