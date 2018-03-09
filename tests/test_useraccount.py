"""file to handle testing of user account """
import unittest
from app.useraccount import UserClass
import unittest
import json
from app import app
from app.useraccount import UserClass


class UserTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.user = UserClass()

        self.user_details = {
            'username': 'cliff',
            'email': 'bla@bla.com',
            'password': '12345678',
            'cpassword': '12345678'
        }

    def tearDown(self):
        """removing user class after everything"""
        del self.user

    def test_duplicate_user(self):
        """check if inputs are correct on all fields"""
        self.user.registerUser("cliff", "bla@bla.com", "clifford", "clifford")
        password_duplicate_user = {'username': 'cliff', 'email': 'bla@bla.com','password': 'clifford','cpassword': 'clifford'}
        response = self.client.post('/api/v1/auth/register', data=json.dumps(password_duplicate_user),
                                    content_type='application/json'
                                    )
        response_data = response.get_data(as_text=True)
        self.assertEqual(response_data, "User already exists.Please login")

    def test_short_password_length(self):
        """check if password is too short"""
        password_length = {'username': 'cliffer', 'email': 'bla@blah.com','password': '12367','cpassword': '12367'}
        response = self.client.post('/api/v1/auth/register', data=json.dumps(password_length),
                                    content_type='application/json'
                                    )
        response_data = response.get_data(as_text=True)
        self.assertEqual(response_data, "Your password should be atleast 8 characters")

    def test_invalid_username(self):
        """check if inputs are correct on all fields"""
        invalid_username = {'username': '@@@@@', 'email': 'blabla.com','password': '12345678','cpassword': '12345678'}
        response = self.client.post('/api/v1/auth/register', data=json.dumps(invalid_username),
                                    content_type='application/json'
                                    )
        response_data = response.get_data(as_text=True)
        self.assertEqual(response_data, "No special characters (. , ! space [] )")

    def test_invalid_email(self):
        """check if email is valid"""
        invalid_email = {'username': 'clifff', 'email': 'blabla.com','password': '12345678','cpassword': '12345678'}
        response = self.client.post('/api/v1/auth/register', data=json.dumps(invalid_email),
                                    content_type='application/json'
                                    )
        response_data = response.get_data(as_text=True)
        self.assertEqual(response_data, "Enter a valid email address")

   

  
    def test_special_characters(self):
        """checking if username contains special chsracters"""

        register_user = {'username': '#@$%yubh', 'email': 'blabla.com','password': '12345678','cpassword': '12345678'}
        register = self.client.post('/api/v1/auth/register', data=json.dumps(register_user),
                                    content_type='application/json')

        response_data = register.get_data(as_text=True)
        self.assertEqual( response_data, "No special characters (. , ! space [] )")

    def test_login_without_account(self):
        """checks if user logs in without account """

        no_account = {'username': 'clifffer','password': '12345678'}
        response = self.client.post('/api/v1/auth/login', data=json.dumps(no_account),
                                    content_type='application/json'
                                    )
        response_data = response.get_data(as_text=True)
        self.assertEqual(response_data, "User have no account, please register")

    def test_login_wrongpassword(self):
        """checks for wrong password during login"""

        no_account = {'username': 'cliff','password': '12367sfrdtfygujkl8'}
        register_user = {'username': 'cliff', 'email': 'blabla.com','password': '12345678','cpassword': '12345678'}
        self.client.post('/api/v1/auth/register', data=json.dumps(register_user),
                                    content_type='application/json'
                                    )
        login = self.client.post('/api/v1/auth/login', data=json.dumps(no_account),
                                    content_type='application/json'
                                    )
        response_data = login.get_data(as_text=True)
        self.assertEqual(response_data,"Wrong password")

    def test_correctlogin(self):
        """checks if user provide correct credentials"""

        login_user = {'username': 'cliff','password': '12345678'}
        register_user = {'username': 'cliff', 'email': 'blabla.com','password': '12345678','cpassword': '12345678'}
        self.client.post('/api/v1/auth/register', data=json.dumps(register_user),
                                    content_type='application/json'
                                    )
        login = self.client.post('/api/v1/auth/login', data=json.dumps(login_user),
                                    content_type='application/json'
                                    )
        response_data = login.get_data(as_text=True)
        self.assertEqual(response_data, "Successfully logged in.You can now Register a Business")

if __name__ == '__main__':
    unittest.main()      
