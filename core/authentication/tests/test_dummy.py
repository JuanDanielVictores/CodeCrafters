import unittest
from unittest.mock import patch

from django.test import RequestFactory

from core.authentication.models.user import user
from core.authentication.views import login


class DummyUserModelTest(unittest.TestCase):
    def test_user_class_exists(self):
        self.assertIsNotNone(user)


class DummyLoginViewTest(unittest.TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    @patch('core.authentication.views.login.render')
    def test_login_view_renders(self, mock_render):
        request = self.factory.get('/login/')
        response = login.login_view(request)
        mock_render.assert_called_once()
        self.assertTrue(response)


class DummyFormTest(unittest.TestCase):
    def test_fake_form_validation(self):
        class FakeForm:
            def is_valid(self): return False

        form = FakeForm()
        self.assertFalse(form.is_valid())
