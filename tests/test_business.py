"""file to handle testing of user account """
import unittest
from app.useraccount import UserClass
import unittest
import json
from app import app
from app.business import BusinessClass


class BusinesTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.business = BusinessClass()

        self.register_details = {
            'username': 'cliff',
            'email': 'bla@bla.com',
            'password': '12345678',
            'cpassword': '12345678'
        }
        self.login_details = {
            'username': 'cliff',
            'password': '12345678'
        }
        self.businesses_list = {'owner': 'cliff', 'name': 'Samsung', 
                                        'category': 'Software', 'location': 'Nairobi'}
        self.register_user = self.client.post('/api/v1/auth/register', data=json.dumps(self.register_details),
                                    content_type='application/json')
        self.login_user = self.client.post('/api/v1/auth/login', data=json.dumps(self.login_details),
                                    content_type='application/json')
    def tearDown(self):
        """ Removing BusinessClass """
        
        del self.business

    
    
    def test_invalid_business_name(self):
        """ Check for special characters in business name """
        # self.invalidbusiness_name = {'owner': 'cliff', 
        #                                 'name': '@@@@', 
        #                                 'category': 'Software', 
        #                                 'location': 'Nairobi'}
        invalid_business_name = self.client.post('/api/v1/business', data=json.dumps({"owner":"mate", 'location':'wmm', 'category':'yyyyy', 'business_name':'@@@@'}), content_type='application/json')
        response_data = str(invalid_business_name.get_data(as_text=True))
        self.assertIn("No special characters", response_data)

    # def test_return_of_all_businesses(self):
    #     """ Check for all businesses in the system """
    #     self.business.businesses_list = [{'owner': 'cliff@gmail.com', 'name': 'Samsung', 'category': 
    #                                     'Software', 'location': 'Nairobi'},
    #                                     {'owner': 'clifford@gmail.com','name': 'Urban', 'category': 
    #                                     'Food', 'location': 'Nairobi'}]
    #     msg = self.business.businesses_list

    #     value = self.business.allBusinesses() 
    #     self.assertEqual(msg, value)                                 
    
    # def test_owner(self):
    #     """ Check for businesses belonging to owner """
    #     response = self.client.post('/api/v1/auth/business', data=json.dumps(password_duplicate_user),
    #                                 content_type='application/json'
    #                                 )
    #     self.assertEqual(msg, [{'owner': 'cliff@gmail.com', 'name': 'Samsung', 'category': 
    #                                     'Software', 'location': 'Nairobi'}])

    # def test_correct_output(self):
    #     """ Check for correct business creation """
        
    #     msg = self.business.createBusiness('Apple', "cliff@gmail.com", "Software", "Nairobi")
    #     self.assertEqual(msg, [{'owner': 'cliff@gmail.com', 'name': 'Apple', 'category': 'Software', 
    #                     'location': 'Nairobi',}])


if __name__ == '__main__':
    unittest.main()
