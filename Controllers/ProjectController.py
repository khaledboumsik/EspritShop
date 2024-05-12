import sys
sys.path.append(r'C:\Users\Khaled\Desktop\ESPRITSHOP')
from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from Services.ProjectService import ProjectService
from ErrorGenerators.CreateProjectApiHandler import generate_add_project_error_message
from flask import Blueprint
project_blue_print=Blueprint("project_blue_print",__name__)
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:@localhost:3306/espritshopmaindb"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

@project_blue_print.route("/project/<id>", methods=["GET"])  
def get_project_by_id(id):
    projectservice = ProjectService(engine)
    information = projectservice.get_project_by_ID(ID=id)
    return jsonify(information)
@project_blue_print.route("/projects/<degree>",methods=['GET'])
def get_project_by_degree(degree):
    projectService=ProjectService(engine)
    information=projectService.get_projects_by_degree(Degree=degree)
    return jsonify(information)


@project_blue_print.route('/project', methods=['POST'])
def create_project():
    about = request.json.get('About')
    degree = request.json.get('Degree')
    name = request.json.get('Name')
    price = request.json.get('Price')
    demo = request.json.get('Demo')
    error_message=generate_add_project_error_message(about,degree,name,price,demo)
    if error_message=="":
        project_service = ProjectService(engine)
        project_service.create_project(About=about, Degree=degree, Name=name,Price=price,Demo=demo)
        return jsonify({'message': 'Project created successfully'}), 201
    else:
        return jsonify({'error': error_message}), 400
