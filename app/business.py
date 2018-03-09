""" Handle creation, deletion and editing of businesses"""
import re
from flask import session


class BusinessClass(object):
    """ Handles creation of business """
    

    def __init__(self):
        """ list to hold business a user creates """
        self.businesses_list = []

    def getOwner(self, user):
        """ Returns businesses belonging to a user """
        
        user_businesses_list = [
            item for item in self.businesses_list if item['owner'] == user]
        return user_businesses_list

    def allBusinesses(self):
        """ returns all existing businesses """
        return self.businesses_list

    def get_business_by_name(self, business_name):
        """ return the business with the given name"""

        for business in self.businesses_list:
            if business['name'] == business_name:
                return business
        else:
            return False
            
    def createBusiness(self, business_name, user, category, location):
        """ Handles creation of businesses """          
        #Check for special characters
        if re.match("^[a-zA-Z0-9 _]*$", business_name):
            my_business = session['username'] == user
        else:
            return "No special characters (. , ! space [] )"
        #Get users business lists    
        #check if name of business list already exists
        if my_business:
            businesses_dict = {
                'name': business_name,
                'owner': user,
                'category': category,
                'location': location,
            }
            print my_business
            self.businesses_list.append(businesses_dict)
            return "Successfully registered above business."
        return "Please login to register a business."

    
    def editBusiness(self, edit_name, old_name, user):
        """ Handles edits made to business name """           
        #edited name and original name
        # print(len(self.businesses_list))
        if re.match("^[a-zA-Z0-9 _]*$", edit_name):
            #Get users business lists
            my_business = self.getOwner(user)
            businesses = [business for business in my_business if business["name"] == old_name]
            if not businesses:
                return "Business not found, Updpate failed"

            found_business = businesses[0]
            del found_business['name']
            edit_dict = {
                'name': edit_name
                }
            found_business.update(edit_dict) 
            return self.getOwner(user)               
        else:
            return "No special characters (. , ! space [] )"
        

    
    def deleteBusiness(self, busines_name, user):
        # Handles removal of businesss using list comprehension
        my_business = self.getOwner(user)

        businesses = [business for business in self.businesses_list if business["name"] == business_name]
        if not businesses:
            return "Deletion failed , Business Not found"
        # print("Current length of business list is ",len(self.businesses_list))
        found_business = business[0]
        new_business_list = [business for business in self.businesses_list if business["name"] != business_name]
        self.businesses_list = new_business_list
        # print(len(self.businesses_list))
        # print("Updated Length of business list is ",len(self.businesses_list))
        return self.businesses_list
