from rest_framework.test import APITestCase, APIClient
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.utils import json
from rest_framework_simplejwt.tokens import RefreshToken

from apps.user.models import CustomUser


class CustomUserRegisterSerializerTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("register-list")

    def test_user_create(self):
        data = {
            "first_name": "Beksultan",
            "last_name": "Akmatbek",
            "email": "email@gmail.com",
            "password": "password",
            "check_password": "password",
            "phone": "0999999999",
        }
        self.response = self.client.post(self.url, json.dumps(data), content_type='application/json')
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.get().email, 'email@gmail.com')
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_invalid_password(self):
        data = {
            "check_password": "password",
            "password": "password1",
            "email": "email@gmail.com",
            "first_name": "Beksultan",
            "last_name": "Akmatbek",
            "phone": "0999999999",
        }
        self.response = self.client.post(self.url, data, format="json")
        self.assertContains(self.response, text="invalid password", status_code=400)

    def test_userprofile_list_unauthenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


class TestChangePasswordSerializer(APITestCase):
    def setUp(self):
        self.client = APIClient()
        CustomUser.objects.create_user(email="email@gmail.com", password="password")
        self.res = self.client.post(
            reverse("token_obtain_pair"),
            {"email": "email@gmail.com", "password": "password"},
        )
        self.client.login(email="email@gmail.com", password="password")
        access_token = self.res.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION="bearer " + access_token)
        self.url = reverse("change_password")

    def test_changed_password(self):
        data = {"old_password": "password", "new_password": "new password"}
        self.response = self.client.put(self.url, data, format="json")
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)


class TestLogoutSerializer(APITestCase):
    def setUp(self):
        self.client = APIClient()
        CustomUser.objects.create_user(email="email@gmail.com", password="password")
        self.res = self.client.post(
            reverse("token_obtain_pair"),
            {"email": "email@gmail.com", "password": "password"},
        )
        access_token = self.res.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + access_token)
        self.url = reverse("auth_logout")

    def test_logout(self):
        refresh_token = self.res.data["refresh"]
        data = {"refresh": refresh_token}
        self.response = self.client.post(self.url, data, format="json")
        self.assertTrue(self.url)
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
