""" view file to handle views """
import os
import requests 
from flask import request, session, jsonify
from app import app
from app.useraccount import UserClass
from app.business import BusinessClass
""" Variable stores user's email """
user = None
app.secret_key = os.urandom(20)
user = UserClass()
businessC = BusinessClass()
@app.route('/')
def index():
    """ Render index page """
    
    return jsonify({"message": "Welcome to WeConnect"})


@app.route('/api/v1/auth/register', methods=['GET', 'POST'])
def register():
    """ User registration """
    
    if request.method == "POST":
            username = request.json.get('username')
            email = request.json.get('email')
            password = request.json.get('password')
            cpassword = request.json.get('cpassword')
                           
            response = user.registerUser(username, email, password, cpassword)
            return response

@app.route('/api/v1/auth/login', methods=['GET', 'POST'])
def login():
    """ User login """
    
    if request.method == "POST":
            username = request.json['username']
            password = request.json['password']
            session['username']= username            
            msg = user.login(username, password)
            response = msg
            return response

@app.route('/api/v1/business', methods=['GET', 'POST'])
def business():
    """ create business """
    if session.get('username') is not None:
        if request.method == "POST":
           user = request.json['owner']
           category = request.json['category']
           location = request.json['location']
           business_name = request.json['business_name']
           msg = businessC.createBusiness(business_name, user, category, location,)
           response = jsonify(msg)
           response.status_code = 201
           return response
        elif request.method == "GET":
            business = businessC.allBusinesses()
            
            return jsonify(business)    
    return jsonify({"message": "Please Login"})



@app.route('/api/v1/business/<businessId>', methods=['PUT'])
def edit_business(businessId):
    """ edit business """
    if session.get('username') is not None:
        if request.method == "PUT":
            old_name = businessId
            edit_name = request.json['edit_name']
            user =  session['username']
            update_business = businessC.editBusiness(edit_name, old_name, user)
            return jsonify(update_business)
    return jsonify({"message": "Please Login"})

@app.route('/api/v1/business/<businessId>', methods=['GET'])
def get_business(businessId):
    """ edit business """
    if session.get('username') is not None:
        if request.method == "GET":
            business_name = businessId
            get_business = businessC.get_business_by_name(business_name)
            return jsonify(get_business)
    return jsonify({"message": "Please Login"})


@app.route('/api/v1/business/<businessId>', methods=['DELETE'])
def delete_business(businessId):
    """ delete business """
    if session.get('username') is not None:
        business_name = businessId
        user = session['username']
        delete = business.deleteBusiness(business_name, user)
        return jsonify(delete)
    return jsonify({"message": "Please Login"})
               

@app.route('/api/v1/auth/reset-password', methods=['POST'])
def reset_password():
    """ Reseting password """
    if request.method == "POST":
        npassword = request.json['npassword']
        cpassword = request.json['cpassword']
        msg = user.changePassword(npassword,cpassword)
        return msg

@app.route('/api/v1/logout', methods=['POST'])
def logout():
    """ Logging out """
    if session.get('username') is not None:
        session.pop('username', None)
        return jsonify({"message": "Logout successful"})
    return jsonify({"message": "You are not logged in"})
        




	