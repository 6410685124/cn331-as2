from django.test import TestCase
from .models import Subject, Student, Class

# Create your tests here.


class SubjectTestCase(TestCase):

    def setUp(self):
        Subject.objects.create(code="a", name="A")
        Subject.objects.create(code="b", name="B")

        Student.objects.create(
            first_name="c", last_name='d', student_id='e', year=1)
        Student.objects.create(
            first_name="f", last_name='g', student_id='h', year=1)

        subject1 = Subject.objects.get(name="A")
        subject2 = Subject.objects.get(name="B")
        Class.objects.create(
            name=subject1, year='1980', semester=1, max_seats=10)
        Class.objects.create(
            name=subject2, year='1980', semester=1, max_seats=1)
        
        #at start of all test
        subject1 = Subject.objects.get(name="A")
        subject2 = Subject.objects.get(name="B")
        student1 = Student.objects.get(
            first_name="c")
        student2 = Student.objects.get(
            first_name="f")
        class1 = Class.objects.get(
            name=subject1)
        class2 = Class.objects.get(
            name=subject2)
    
    def test_subject_to_str(self):
        subject1 = Subject.objects.get(name="A")
        
        self.assertEqual(str(subject1), 'a')
    def test_student_to_str(self):
        student1 = Student.objects.get(
            first_name="c")

        self.assertEqual(str(student1), 'e c d')
    def test_class_to_str(self):
        subject1 = Subject.objects.get(name="A")
        class1 = Class.objects.get(
            name=subject1)

        self.assertEqual(str(class1), str(subject1))
    def test_add_student(self):
        subject1 = Subject.objects.get(name="A")
        student1 = Student.objects.get(
            first_name="c")
        class1 = Class.objects.get(
            name=subject1)

        Class.add_student(class1, student1)
        self.assertAlmostEqual(class1.remaining_seats, 9, msg='test 1 failed')
    def test_remove_student(self):
        subject1 = Subject.objects.get(name="A")
        student1 = Student.objects.get(
            first_name="c")
        class1 = Class.objects.get(
            name=subject1)

        Class.add_student(class1, student1)
        Class.remove_student(class1, student1)
        self.assertAlmostEqual(class1.remaining_seats, 10, msg='test 2 failed')

