from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()


class PasswordAuthenticationTests(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpass'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login(self):
        # Attempt to authenticate the user with the correct credentials
        response = self.client.post('/login/', {'username': self.username, 'password': self.password})
        self.assertEqual(response.status_code, 302)  # Assuming a successful login redirects

        # Check if the user is logged in
        self.assertTrue('_auth_user_id' in self.client.session)

    def test_login_incorrect_password(self):
        # Attempt to authenticate the user with an incorrect password
        response = self.client.post('/login/', {'username': self.username, 'password': 'wrongpass'})
        self.assertEqual(response.status_code, 200)  # Assuming a failed login returns to the same page

        # Check if the user is not logged in
        self.assertFalse('_auth_user_id' in self.client.session)

    def test_logout(self):
        # Log in the user
        self.client.login(username=self.username, password=self.password)

        # Log out the user
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 302)  # Assuming a successful logout redirects

        # Check if the user is logged out
        self.assertFalse('_auth_user_id' in self.client.session)
        
        
        
        
