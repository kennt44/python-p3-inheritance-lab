import pytest
from lib.teacher import Teacher
from lib.student import Student

def test_teacher_inheritance():
    teacher = Teacher("John", "Doe")
    assert teacher.first_name == "John"
    assert teacher.last_name == "Doe"
    assert isinstance(teacher, Teacher)  # Check that teacher is an instance of Teacher
    assert isinstance(teacher, User)  # Check that teacher is an instance of User (inherited)

def test_student_inheritance():
    student = Student("Jane", "Doe")
    assert student.first_name == "Jane"
    assert student.last_name == "Doe"
    assert isinstance(student, Student)  # Check that student is an instance of Student
    assert isinstance(student, User)  # Check that student is an instance of User (inherited)

def test_teacher_knowledge():
    teacher = Teacher("John", "Doe")
    knowledge_item = teacher.teach()
    assert knowledge_item in teacher.knowledge  # Check if the knowledge returned by teach is valid

def test_student_learn():
    student = Student("Jane", "Doe")
    student.learn("Learned about inheritance")
    assert "Learned about inheritance" in student.knowledge  # Check if the student's knowledge list contains the new information
