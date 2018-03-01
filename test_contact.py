import unittest
from contact import Contact

class Contactest(unittest.TestCase):
    """
       Class performing unit testing for class Contact
    """

    def setUp(self):
        """Defining setUp() method that runs prior to each test."""
        self.contacts = Contact()
        self.contacts.phonebook = {}

         """Test to create contacts"""
    def test_create_contact(self):
        output = self.contacts.create("john", "+12346789")
        self.assertIn("contact successfully created", output)

        """test to create existing contact"""
    def test_create_existing_contact(self):
        create = self.contacts.create("john", "+12346789")
        output = self.contacts.create("john", "+12346789")
        self.assertIn("contact already exist", output)

        """Test for missing name when creating contacr"""
    def test_create_contact_wihout_name(self):
        output = self.contacts.create(" ", "+12346789")
        self.assertIn("name is missing", output)

        """Test for missing number when creating contact"""
    def test_create_name_without_number(self):
        output = self.contacts.create("john", " " )
        self.assertIn("number is missing", output)

        """Test to edit contact name"""      
    def test_edit_contact_name(self):
        create = self.contacts.create("john", "+12346789")
        output = self.contacts.edit("john", "second john", "+12346789")
        self.assertIn("successfully edited name", output)

        """Test to edit contact number""" 
    def test_edit_contact_number(self):
        create = self.contacts.create("john", "+12346789")
        output = self.contacts.edit("john", "+12346789", "+987654321")
        self.assertIn("successfully edited number", output)

        """test to edit non-existing contacts"""
    def test_edit_non_existing_contact(self):
        create = self.contacts.create("john", "+12346789")
        output = self.contacts.edit("john1", "+987654321")
        self.assertIn("contact does not exist", output)


        """test to delete a contact"""
    def test_delete_contact_number(self):
        create = self.contacts.create("john", "+12346789")
        output = self.contacts.delete("john", "+123456789")
        self.assertIn("contact succefully deleted", output)

        """test to delete a contact the doesn't exist"""
    def test_delete_null_contact(self):
        create = self.contacts.create("john", "+12346789")
        output = self.contacts.delete("john1", "987654321")
        self.assertIn("contact doesnt exist ", output)
