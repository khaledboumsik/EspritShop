import sys
sys.path.append(r'C:\Users\Khaled\Desktop\ESPRITSHOP')
from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from Services.ClientService import ClientService
from Utils.EmailVerification import vertify_email

app = Flask(__name__)

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:@localhost:3306/espritshopmaindb"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

@app.route("/users/<id>", methods=["GET"])  # Moved above the POST route
def get_user_by_id(id):
    client_service = ClientService(engine)
    information = client_service.get_client_by_ID(ID=id)
    return jsonify(information)

@app.route('/users', methods=['POST'])
def create_user():
    email = request.json.get('Email')
    loginName = request.json.get('LoginName')
    password = request.json.get('Password')
    phoneNumber = request.json.get('PhoneNumber')
    confirmation = []
    error_message = ""
    if not email:
        confirmation.append("Email")
    if not loginName:
        confirmation.append("LoginName")
    if not password:
        confirmation.append("Password")
    if not phoneNumber:
        confirmation.append("PhoneNumber")
    if confirmation:
        for mistake in confirmation:
            error_message += mistake + " is missing  | | "
    if (not vertify_email(email)) or len(email)>100:
        print(email,vertify_email(email))
        error_message+="Email must be valid and it's length dosent go over 100 letters | | "
    if not isinstance(phoneNumber,int) or len(str(phoneNumber))>12:
        error_message+="PhoneNumber must be composed of only numbers and dosent go over 12 number  | | "
    if len(password)<10:
        error_message+="Password must be at least 10 chacters long"
    if error_message=="":
        client_service = ClientService(engine)
        client_service.create_user(Username=loginName, Password=password, Email=email, PhoneNumber=phoneNumber)
        return jsonify({'message': 'User created successfully'}), 201
    else:
        return jsonify({'error': error_message}), 400

if __name__ == '__main__':
    app.run(debug=True)
