from django.test import TestCase, Client
from home.models import Feature, Testimonial, Client as ClientModel

class HomeCMSTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.feature = Feature.objects.create(
            title='Fast Performance',
            description='System works seamlessly with high speed.',
            icon='bi-speedometer'
        )
        self.testimonial = Testimonial.objects.create(
            name='Jane Doe',
            position='Principal',
            quote='Outstanding platform for higher institutions.'
        )
        self.client_obj = ClientModel.objects.create(
            name='Partner University',
            logo='clients/partner.png'
        )

    def test_model_str_methods(self):
        self.assertEqual(str(self.feature), 'Fast Performance')
        self.assertEqual(str(self.testimonial), 'Jane Doe - Principal')
        self.assertEqual(str(self.client_obj), 'Partner University')

    def test_landing_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
