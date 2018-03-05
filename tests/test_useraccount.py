"""file to handle testing of user account """
import unittest
from app.useraccount import useraccount

class UserAccountTestCases(unittest.TestCase)
    """ Test for password length
        Test for password mismatch when registering
        Test for duplicate account
        Test for special character in username
        Test for invalid email address
        test for correct inputs
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

        