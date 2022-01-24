from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """This function test user creation with the email address"""
        email = "test@example.com"
        password = "Test123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test user email is normalized"""
        email = 'test@EXAMPLE.com'
        password = 'Test123'

        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test new user with invalid email raise an exception"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Test123')

    def test_create_superuser(self):
        """This function test superuser creation with the email address"""
        email = "test@example.com"
        password = "Test123"
        user = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)


