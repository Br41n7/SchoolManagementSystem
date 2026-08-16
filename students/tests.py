from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from students.models import Student

User = get_user_model()

class StudentsAuthTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='authstudent',
            email='authstudent@example.com',
            password='password123'
        )
        self.student = Student.objects.create(
            user=self.user,
            full_name='Auth Student',
            program='Engineering',
            level=200
        )

    def test_dashboard_unauthenticated_redirect(self):
        response = self.client.get('/students/student/dashboard/')
        self.assertEqual(response.status_code, 302)

    def test_dashboard_authenticated(self):
        self.client.login(username='authstudent', password='password123')
        response = self.client.get('/students/student/dashboard/')
        self.assertEqual(response.status_code, 200)
