from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from courses.models import Course, StudentCourseRegistration
from students.models import Student

User = get_user_model()

class CoursesTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='coursestudent',
            email='coursestudent@example.com',
            password='password123'
        )
        self.student = Student.objects.create(
            user=self.user,
            full_name='Course Student',
            program='Computer Science',
            level=100
        )
        self.course = Course.objects.create(
            code='CSC101',
            title='Intro to CS',
            unit=3,
            level=100
        )

    def test_course_registration(self):
        self.client.login(username='coursestudent', password='password123')
        reg = StudentCourseRegistration.objects.create(
            student=self.student,
            course=self.course,
            semester='1st',
            session='2024/2025'
        )
        self.assertEqual(reg.student, self.student)
        self.assertEqual(reg.course, self.course)
        self.assertEqual(StudentCourseRegistration.objects.count(), 1)
