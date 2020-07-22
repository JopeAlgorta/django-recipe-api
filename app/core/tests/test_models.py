from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successfully(self):
        """Test creating a new user with an email is successfull"""
        email = 'test@example.com'
        password = 'Test1234'
        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user to be normalized"""
        email = 'test@EXAMPLE.com'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test if the new user email is correct"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_super_user(self):
        user = get_user_model().objects.create_superuser('hola@example.io', 'test123')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)