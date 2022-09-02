import email
from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        email = 'mishaba1990@gmail.com'
        password = "Testpass231"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = 'misha1990@GMAIL'
        user = get_user_model().objects.create_user(email,'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None)
    
    def test_create_new_superuser_(self):
        user = get_user_model().objects.create_superuser(
            'mishaba1990@gmail.com',
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)