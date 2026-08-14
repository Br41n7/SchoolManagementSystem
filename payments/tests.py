from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from payments.models import Payment

User = get_user_model()

class PaymentsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='paystudent',
            email='paystudent@example.com',
            password='password123'
        )
        self.payment = Payment.objects.create(
            student=self.user,
            amount=50000.0,
            purpose='Tuition Fee',
            ref_id='REF123456',
            status='paid',
            payment_method='paystack'
        )

    def test_payment_receipt_view(self):
        self.client.login(username='paystudent', password='password123')
        response = self.client.get(f'/payments/receipt/{self.payment.ref_id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['payment'], self.payment)

    def test_download_receipt_pdf(self):
        self.client.login(username='paystudent', password='password123')
        response = self.client.get(f'/payments/receipt/{self.payment.ref_id}/download/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')
