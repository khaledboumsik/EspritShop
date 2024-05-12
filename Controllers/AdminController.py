import sys
sys.path.append(r'C:\Users\Khaled\Desktop\ESPRITSHOP')
from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from Services.AdminService import AdminService
from ErrorGenerators.CreateAdminApiHandler import generate_add_admin_error_message
from flask import Blueprint
admin_blue_print=Blueprint("admin_blue_print",__name__)
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:@localhost:3306/espritshopmaindb"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

@admin_blue_print.route("/admin/<id>", methods=["GET"])  
def get_admin_by_id(id):
    adminService = AdminService(engine)
    information = adminService.get_admin_by_ID(ID=id)
    return jsonify(information)

@admin_blue_print.route('/admin', methods=['POST'])
def create_user():
    email = request.json.get('Email')
    Login = request.json.get('Login')
    password = request.json.get('Password')
    phoneNumber = request.json.get('PhoneNumber')
    status=request.json.get('Status')
    error_message=generate_add_admin_error_message(email,Login,password,phoneNumber,status)
    if error_message=="":
        admin_serivce = AdminService(engine)
        admin_serivce.create_admin(Login=Login, Password=password, Email=email, PhoneNumber=phoneNumber,Status=status)
        return jsonify({'message': 'Admin created successfully'}), 201
    else:
        return jsonify({'error': error_message}), 400
