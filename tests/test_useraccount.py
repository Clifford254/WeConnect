"""file to handle testing of user account """
import unittest
from app.useraccount import useraccount

class UserAccountTestCases(unittest.TestCase)
    """ Test for password length
        Test for password mismatch when registering
        Test for duplicate account
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
    

