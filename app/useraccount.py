"""file to handle user account"""
import re
"""import regular expression"""

class UserClass(object):
    """class to handleregistration and login of user"""

    def __init__(self):
        """list containing users"""
        self.user_list = []

    def registerUser(self, username, email, password,cpassword):
        """create registered users by adding to dictionary
           Empty dict to hold each user"""
        user_dict = {}
        #chsck if user already exists
        for user in self.user_list:
            if username == user['username']:
                return "User already exists.Please login"
            elif email == user['email']:
                msg="User already exists.Please login"
                return msg
        #Check for right password length
        if len(password) < 8:
            msg="Your password should be atleast 8 characters"
            return msg
        #Check for special characters in username
        if not re.match("^[a-zA-Z0-9_]*$", username):
            msg="No special characters (. , ! space [] )"
            return msg
        #Check for correct email
        if not re.match(r"(^[a-zA-Z0-9_.]+@[a-zA-Z0-9-]+\.[a-z]+$)", email):
            msg = "Enter a valid email address"
            return msg
        #Password Mismatch
        if password == cpassword:
            user_dict['username'] = username
            user_dict['email'] = email
            user_dict['password'] = password
            self.user_list.append(user_dict)
            msg = "Successfully registered. You can now login!"
            return msg
        else:
            msg ="Password mismatch"
            return msg

    def login(self, username, password):
        #Log in users
        for user in self.user_list:
            if username == user['username']:
                if password == user['password']:
                    msg = "Successfully logged in.You can now Register a Business"
                    return msg
                msg = "Wrong password"
                return msg
        msg = "User have no account, please register"
        return  msg

    def changePassword(self, npassword, cpassword):
        #reset password
        for user in self.user_list:
            if npassword == cpassword:
                user['password'] = npassword
                return "Password changed successful"
            return "The new passwords should match"
        return "User does not exist, sign up!"

   