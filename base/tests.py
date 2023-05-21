from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

User = get_user_model()


class PasswordAuthenticationTests(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpass'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login(self):
        # Attempt to authenticate the user with the correct credentials
        url = reverse('login')
        data = {'username': self.username, 'password': self.password}
        response = self.client.post(url, data)

        self.assertRedirects(response, reverse('tasks'))  # Update 'home' with the correct URL name

        # Check if the user is logged in
        self.assertTrue(self.client.session['_auth_user_id'])

    def test_login_incorrect_password(self):
        # Attempt to authenticate the user with an incorrect password
        url = reverse('login')
        data = {'username': self.username, 'password': 'testpass'}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)

        # Check if the user is not logged in
        self.assertFalse('_auth_user_id' in self.client.session)

    def test_logout(self):
        # Log in the user
        self.client.login(username=self.username, password=self.password)

        # Log out the user
        url = reverse('logout')
        response = self.client.get(url)

        self.assertRedirects(response, reverse('login'))  # Update 'home' with the correct URL name

        # Check if the user is logged out
        self.assertFalse('_auth_user_id' in self.client.session)
