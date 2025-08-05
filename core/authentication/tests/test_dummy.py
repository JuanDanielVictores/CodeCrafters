import unittest

from django.test import RequestFactory

from core.authentication.views.login import LoginAuthView


class DummyLoginViewTest(unittest.TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_login_auth_view_renders(self):
        request = self.factory.get('/login/')
        response = LoginAuthView.as_view()(request)
        self.assertEqual(response.status_code, 200)
