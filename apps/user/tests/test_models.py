from django.test import TestCase

from apps.user.models import CustomUser


class CustomUserTest(TestCase):
    def test_model(self):
        user = CustomUser.objects.create_user(email="email@gmail.com", password="password")
        self.assertEqual(user.__str__(), user.email)
