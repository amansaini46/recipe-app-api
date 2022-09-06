"""Test for models"""

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """ Test model"""

    def test_create_user_with_email_successful(self):
        """test creating a user with the test email"""
        email = "test@example.com"
        password = "test123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_with_normalized_email(self):
        sample_emails = [
            ["Test1@Examaple.com", "Test1@examaple.com"],
            ["TeSt2@Examaple.com", "TeSt2@examaple.com"],
            ["test3@Examaple.com", "test3@examaple.com"],
            ["TEST4@Examaple.com", "TEST4@examaple.com"],
            ["test5@Examaple.COM", "test5@examaple.com"],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(
                email=email,
                password="password"
            )
            self.assertEqual(user.email, expected)

    def test_create_user_without_email_raise_error(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email="",
                password="password"
            )

    def test_create_super_user_with_email_successful(self):
        """Test creating superuser with test email"""
        email = "test@example.com"
        password = "test123"
        super_user = get_user_model().objects.create_superuser(
            email=email,
            password=password,
        )

        self.assertEqual(super_user.email, email)
        self.assertTrue(super_user.check_password(password))
