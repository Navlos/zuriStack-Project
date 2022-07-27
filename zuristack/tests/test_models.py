from django.test import TestCase
from django.contrib.auth import get_user_model


class UserManagerCase(TestCase):
    def test_create_user(self):
        user = get_user_model
        user = User.objects.create_user(
            email='user@email.com', password='passworld')
        self.assertEqual(user.email, 'user@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        with self.assertRaises(TypeError):
            User.objects.create_user()

        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password='')

    def test_create_super_user(self):

        pass
