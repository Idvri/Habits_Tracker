from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


# Create your tests here.
class RegistrationApiViewTest(APITestCase):

    def setUp(self):
        pass

    def test_registration_api_view(self):
        registration_data = {
            "email": "testuser@example.com",
            "password": "testpassword",
        }
        response = self.client.post('/users/register/', registration_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = User.objects.get(email="testuser@example.com")
        self.assertIsNotNone(user)

    def tearDown(self):
        pass
