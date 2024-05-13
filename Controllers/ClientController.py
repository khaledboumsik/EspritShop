import sys

sys.path.append(r"C:\Users\Khaled\Desktop\ESPRITSHOP")
from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from Services.ClientService import ClientService
from ErrorGenerators.CreateUserApiHandler import generate_add_client_error_message
from flask import Blueprint

client_blue_print = Blueprint("client_blue_print", __name__)
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:@localhost:3306/espritshopmaindb"
engine = create_engine(SQLALCHEMY_DATABASE_URL)


@client_blue_print.route("/user/<id>", methods=["GET"])
def get_user_by_id(id):
    client_service = ClientService(engine)
    information = client_service.get_client_by_ID(ID=id)
    return jsonify(information)


@client_blue_print.route("/user", methods=["POST"])
def create_user():
    email = request.json.get("Email")
    loginName = request.json.get("LoginName")
    password = request.json.get("Password")
    phoneNumber = request.json.get("PhoneNumber")
    error_message = generate_add_client_error_message(
        email, loginName, password, phoneNumber
    )
    if error_message == "":
        client_service = ClientService(engine)
        client_service.create_user(
            Username=loginName, Password=password, Email=email, PhoneNumber=phoneNumber
        )
        return jsonify({"message": "User created successfully"}), 201
    else:
        return jsonify({"error": error_message}), 400
