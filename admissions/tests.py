from django.test import TestCase, Client
from django.contrib.auth import get_user_model

User = get_user_model()

class AdmissionsAuthTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.normal_user = User.objects.create_user(
            username='applicant',
            email='applicant@example.com',
            password='password123'
        )
        self.staff_user = User.objects.create_user(
            username='staffmember',
            email='staff@example.com',
            password='password123',
            is_staff=True
        )

    def test_screening_dashboard_requires_staff(self):
        # Unauthenticated -> redirect
        response = self.client.get('/admissions/screening/')
        self.assertEqual(response.status_code, 302)

        # Normal user -> redirect due to user_passes_test
        self.client.login(username='applicant', password='password123')
        response = self.client.get('/admissions/screening/')
        self.assertEqual(response.status_code, 302)

        # Staff user -> 200 OK
        self.client.login(username='staffmember', password='password123')
        response = self.client.get('/admissions/screening/')
        self.assertEqual(response.status_code, 200)
