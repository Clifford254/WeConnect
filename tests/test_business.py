""" File to handle testing of businesses """
import unittest
from app.business import BusinessClass


class TestCasesBusiness(unittest.TestCase):
    """ Test for special character in business names
        Test for owner of business
        Test for correct output(business creation)
        Test for deletion of existing business
        Test for editing business names
    """
    

    def setUp(self):
        """ Setting up BusinessClass """
        
        self.business = BusinessClass()

    def tearDown(self):
        """ Removing BusinessClass """
        
        del self.business
    
    def test_special_characters(self):
        """ Check for special characters in business name """
        
        user = "cliff@gmail.com"
        msg = self.business.createBusiness("M!niso","Retail","Nairobi", user)
        self.assertEqual(msg, "No special characters (. , ! space [] )")

    def test_return_of_all_businesses(self):
        """ Check for all businesses in the system """
        self.business.businesses_list = [{'owner': 'cliff@gmail.com', 'name': 'Samsung', 'category': 
                                        'Software', 'location': 'Nairobi'},
                                        {'owner': 'clifford@gmail.com','name': 'Urban', 'category': 
                                        'Food', 'location': 'Nairobi'}]
        msg = self.business.businesses_list

        value = self.business.allBusinesses() 
        self.assertEqual(msg, value)                                 
    
    def test_owner(self):
        """ Check for businesses belonging to owner """
        self.business.businesses_list = [{'owner': 'cliff@gmail.com', 'name': 'Samsung', 'category': 
                                        'Software', 'location': 'Nairobi'}]
        user = "cliff@gmail.com"
        msg = self.business.getOwner(user)
        self.assertEqual(msg, [{'owner': 'cliff@gmail.com', 'name': 'Samsung', 'category': 
                                        'Software', 'location': 'Nairobi'}])

    def test_correct_output(self):
        """ Check for correct business creation """
        
        msg = self.business.createBusiness('Apple', "cliff@gmail.com", "Software", "Nairobi")
        self.assertEqual(msg, [{'owner': 'cliff@gmail.com', 'name': 'Apple', 'category': 'Software', 
                        'location': 'Nairobi',}])


if __name__ == '__main__':
    unittest.main()
