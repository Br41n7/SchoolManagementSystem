from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from datetime import date
from admissions.models import AdmissionApplication, UploadedDocument

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
        self.application = AdmissionApplication.objects.create(
            full_name='John Applicant',
            email='john@example.com',
            phone='1234567890',
            date_of_birth=date(2000, 1, 1),
            gender='Male',
            jamb_reg_number='JAMB123456',
            jamb_score=280,
            address='123 Campus Way',
            program='Computer Science'
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

    def test_admission_application_str(self):
        self.assertEqual(str(self.application), 'John Applicant - Computer Science - JAMB123456')

    def test_uploaded_document_str(self):
        doc = UploadedDocument.objects.create(
            application=self.application,
            doc_type='Birth Certificate'
        )
        self.assertEqual(str(doc), 'Birth Certificate for John Applicant')
