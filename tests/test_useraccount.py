"""file to handle testing of user account """
import unittest
from app.useraccount import useraccount

class UserAccountTestCases(unittest.TestCase)
    """ Test for password length
        Test for password mismatch when registering
        Test for duplicate account
        Test for special character in username
        Test for invalid email address
        test for correct inputs register
        test login with no account
        Test login with wrong password
        Test login with correct email and password
    """

    def setUp(self):
        """set up UserClass before anything"""
        
        self.user = UserClass()

    def tearDown(self):
        """removing user class after everything"""

        del self.user
    
    def test_password_length(self):
        """checking for password length"""

        msg = self.user.registerUser(
            "cliff", "cliff@gmail.com", "cliffor", "cliffor")
        self.assertEqual(
            msg,"Your password should be atleat 8 characters")

    def test_password_mismatch(self):
        """checking for password mismatch"""

        msg = self.user.registerUser(
            "cliff", "cliff@gmail.com", "clifford", "clifforf")
        self.assertEqual(msg, "Password mismatch")

    def test_duplicate_user(user):
        """checking for duplicate user"""

        self.user.registerUser(
            "cliff", "cliff@gmail.com", "clifford", "clifford")
        msg = self.user.registerUser(
            "cliff", "cliff@gmail.com", "clifford", "clifford")
        self.assertIn("User already exists", msg)

    def test_special_characters(self):
        """checking if username contains special chsracters"""

        msg = self.user.registerUser(
            "cl!ff", "cliff@gmail.com", "clifford", "clifford") 
        self.assertIn("No special character in username", msg)

    def test_invalid_email(self):
        """check if email is valid"""

        msg =(
            "cliff", "cliffgmail.com", "clifford", "clifford")
        self.assertEqual(msg,"Enter a valid email address")
    
    def test_correct_input("self"):
        """check if inputs are correct on all fields"""

        msg =(
            "cliff", "cliff@gmail.com", "clifford", "clifford")
        self.assertIn("Successfully registered",msg)

    def test_login_withoutaccount(self):
        """checks if user account exist"""

        self.user.user_list = [
            {'username':'cliff','email':'cliff@gmail.com','password':'clifford' }]
        msg = self.user.login("clifford@gmail.com","clifford25")
        self.assertEqual(msg,"User does not exist, please register")

    def test_login_wrongpassword(self):
        """checks for wrong password during login"""

        self.user.user_list = [
            {'username':'cliff','email':'cliff@gmail.com','password':'clifford' }]
        msg = self.user.login("cliff@gmail.com","clifford25")
        self.assertEqual(msg,"Wrong password")

    def test_correctlogin(self):
        """checks if user provide correct credentials"""

        self.user.user_list = [
            {'username':'cliff','email':'cliff@gmail.com','password':'clifford' }]
        msg = self.user.login("cliff@gmail.com","clifford")
        self.assertIn(msg,"You can now Register a Business")

        