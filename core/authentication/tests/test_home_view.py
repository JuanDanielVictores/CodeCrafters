from django.test import TestCase
from django.urls import reverse

class HomeViewTests(TestCase):
    def test_home_view_renders_correctly(self):
        response = self.client.get(reverse('authentication:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login/login.html')

