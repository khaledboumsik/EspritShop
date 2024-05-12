import sys
sys.path.append(r'C:\Users\Khaled\Desktop\ESPRITSHOP')
from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from Services.ClientProjectService import ClientProjectService
from ErrorGenerators.CreateJobApiHandler import generate_add_job_error_message
from flask import Blueprint
job_blue_print=Blueprint("job_blue_print",__name__)
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:@localhost:3306/espritshopmaindb"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

@job_blue_print.route("/job_by_id/<id>", methods=["GET"])  
def get_job_by_id(id):
    job_service = ClientProjectService(engine)
    information = job_service.get_client_by_ID(ID=id)
    return jsonify(information)

@job_blue_print.route('/job', methods=['POST'])
def create_job():
    clientID = request.json.get('ClientID')
    projectID = request.json.get('ProjectID')
    responsableID = request.json.get('ResponsableID')
    buyTaskOnly = request.json.get('BuyTaskOnly')
    fastDelivery = request.json.get('FastDelivery')
    customization = request.json.get('Customization')
    privateSession = request.json.get('PrivateSession')
    error_message=generate_add_job_error_message(ClientID=clientID,ProjectID=projectID,ResponsableID=responsableID,BuyTaskOnly=buyTaskOnly,FastDelivery=fastDelivery,Customization=customization,PrivateSession=privateSession)
    if error_message=="":
        job_service = ClientProjectService(engine)
        job_service.create_job(ClientID=clientID,ProjectID=projectID,ResponsableID=responsableID,BuyTaskOnly=buyTaskOnly,FastDelivery=fastDelivery,Customization=customization,PrivateSession=privateSession,Status=0,Progress=0)
        return jsonify({'message': 'job created successfully'}), 201
    else:
        return jsonify({'error': error_message}), 400
