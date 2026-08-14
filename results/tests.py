from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from courses.models import Course
from results.models import CourseResult, CGPA

User = get_user_model()

class ResultsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='student1',
            email='student1@example.com',
            password='password123'
        )
        self.course1 = Course.objects.create(
            code='CS101',
            title='Introduction to Computer Science',
            unit=3,
            level=100
        )
        self.course2 = Course.objects.create(
            code='MTH101',
            title='Algebra and Trigonometry',
            unit=4,
            level=100
        )
        CourseResult.objects.create(
            student=self.user,
            course=self.course1,
            score=85,
            session='2024/2025',
            semester='1st'
        )
        CourseResult.objects.create(
            student=self.user,
            course=self.course2,
            score=72,
            session='2024/2025',
            semester='1st'
        )

    def test_view_results_authenticated(self):
        self.client.login(username='student1', password='password123')
        response = self.client.get('/results/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('results', response.context)
        cgpa_obj = CGPA.objects.filter(student=self.user).first()
        self.assertIsNotNone(cgpa_obj)
        self.assertEqual(float(cgpa_obj.cgpa), 5.0)

    def test_download_results_pdf_authenticated(self):
        self.client.login(username='student1', password='password123')
        response = self.client.get('/results/download/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')
