""" Handle creation, deletion and editing of businesses"""
import re


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
        all_businesses = [
            item for item in self.businesses_list
        ]
        return all_businesses
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
            #Get users business lists
            my_business = self.getOwner(user)
            #check if name of list already exists
            businesses_dict = {
                'name': business_name,
                'owner': user,
                'category': category,
                'location': location,
            }
            self.businesses_list.append(businesses_dict),"successfully registered above business"
        else:
            return "No special characters (. , ! space [] )"
        return self.getOwner(user)

    