from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from subject.models import Student, Subject, Class

# Create your tests here.

class StudentRegistryTestCase(TestCase):
    def setUp(self) -> None:
        subject1 = Subject.objects.create(code='MA101', name='Math')
        subject2 = Subject.objects.create(code='SC101', name='Science')

        student1 = Student.objects.create(first_name='A1', last_name='B1', student_id='1', year='1st Year')
        student2 = Student.objects.create(first_name='A2', last_name='B2', student_id='2', year='1st Year')

        class1 = Class.objects.create(name=subject1, year=2023, semester='1',max_seats=99, status=True)
        class1.students.add(student2)

        class2 = Class.objects.create(name=subject2, year=2023, semester='1',max_seats=99, status=True)
        class2.students.add(student1)
        class1.students.add(student2)

        user1 = User.objects.create_user(username='1', email='example@gmail.com', password='12345')
        user2 = User.objects.create_user(username='2', email='example@gmail.com', password='12345')

    def test_index_view_status_code_with_out_login(self):
        c = Client()
        response = c.get(reverse('index'))
        self.assertEqual(response.status_code, 302)

    def test_login_page(self):
        c = Client()
        response = c.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_validate_user_login(self):
        c = Client()
        response = c.post("/student/login", {"username": "1", "password": "12345"})
        self.assertEqual(response.status_code, 302)

        c.login(username='0', password='12345')
        response = c.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
    
    def test_not_validate_user_login(self):
        c = Client()
        login = c.login(username='0', password='12345')
        self.assertFalse(login)

        response = c.post("/student/login", {"username": "", "password": ""})
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        c = Client()
        response = self.client.get('/student/logout')
        self.assertEqual(response.status_code, 200)
    
    def test_add_student(self):
        c = Client()
        login = c.login(username='1', password='12345')
        class2 = Class.objects.first()
        student = Student.objects.first()
        response = self.client.get(reverse('add_student', args=(student.student_id,class2.name)))
        self.assertEqual(response.status_code, 302)
    
    def test_invalid_add_student(self):
        c = Client()
        class2 = Class.objects.first()
        student = Student.objects.first()

        response = self.client.get(reverse('add_student', args=('5',class2.name)))
        self.assertEqual(response.status_code, 404)

        response = self.client.get(reverse('add_student', args=(student.student_id,'MA')))
        self.assertEqual(response.status_code, 404)

    def test_remove_student(self):
        c = Client()
        class2 = Class.objects.first()
        student = Student.objects.first()
        response = self.client.get(reverse('remove_student', args=(student.student_id,class2.name)))
        self.assertEqual(response.status_code, 302)

    def test_remove_student(self):
        c = Client()
        class2 = Class.objects.first()
        student = Student.objects.first()
        response = self.client.get(reverse('remove_student', args=(student.student_id,class2.name)))
        self.assertEqual(response.status_code, 302)

        response = self.client.get(reverse('remove_student', args=('5',class2.name)))
        self.assertEqual(response.status_code, 404)

        response = self.client.get(reverse('remove_student', args=(student.student_id,'MA')))
        self.assertEqual(response.status_code, 404)

    def test_show_class_detail(self):
        c = Client()
        class2 = Class.objects.first()
        response = self.client.get(reverse('class_detail', args=(class2.name,)))
        self.assertEqual(response.status_code, 200)

    def test_invalid_show_class_detail(self):
        c = Client()
        response = self.client.get(reverse('class_detail', args=('MA',)))
        self.assertEqual(response.status_code, 404)
