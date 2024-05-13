import sys

sys.path.append(r"C:\Users\Khaled\Desktop\ESPRITSHOP")
from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from Services.ClientProjectService import ClientProjectService
from ErrorGenerators.CreateJobApiHandler import generate_add_job_error_message
from flask import Blueprint

job_blue_print = Blueprint("job_blue_print", __name__)
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:@localhost:3306/espritshopmaindb"
engine = create_engine(SQLALCHEMY_DATABASE_URL)


@job_blue_print.route("/job_by_id/<id>", methods=["GET"])
def get_job_by_id(id):
    job_service = ClientProjectService(engine)
    information = job_service.get_job_by_ID(ID=id)
    return jsonify(information)


@job_blue_print.route("/job_by_project_id/<id>", methods=["GET"])
def get_jobs_by_project_id(id):
    job_service = ClientProjectService(engine)
    information = job_service.get_jobs_by_project(ProjectID=id)
    return jsonify(information)

@job_blue_print.route("/get_active_jobs", methods=["GET"])
def get_active_jobs():
    job_service = ClientProjectService(engine)
    information = job_service.get_active_jobs()
    return jsonify(information)
@job_blue_print.route("/get_inactive_jobs", methods=["GET"])
def get_inactive_jobs():
    job_service = ClientProjectService(engine)
    information = job_service.get_inactive_jobs()
    return jsonify(information)
@job_blue_print.route("/jobs", methods=["GET"])
def get_all_jobs():
    job_service = ClientProjectService(engine)
    information = job_service.get_all_jobs()
    return jsonify(information)
@job_blue_print.route("/job_by_client_id/<id>", methods=["GET"])
def get_jobs_by_client_id(id):
    job_service = ClientProjectService(engine)
    information = job_service.get_jobs_by_client(ClientID=id)
    return jsonify(information)
@job_blue_print.route("/activate/<id>", methods=["PUT"])
def activate_job(id):
    job_service = ClientProjectService(engine)
    job_service.change_satus_to_active(ID=id)
    return jsonify({"message": "Status changed successfully"}), 201
@job_blue_print.route("/deactivate/<id>", methods=["PUT"])
def deactivate_job(id):
    job_service = ClientProjectService(engine)
    job_service.change_satus_to_inactive(ID=id)
    return jsonify({"message": "Status changed successfully"}), 201


@job_blue_print.route("/job", methods=["POST"])
def create_job():
    clientID = request.json.get("ClientID")
    projectID = request.json.get("ProjectID")
    responsableID = request.json.get("ResponsableID")
    buyTaskOnly = request.json.get("BuyTaskOnly")
    fastDelivery = request.json.get("FastDelivery")
    customization = request.json.get("Customization")
    privateSession = request.json.get("PrivateSession")
    error_message = generate_add_job_error_message(
        ClientID=clientID,
        ProjectID=projectID,
        ResponsableID=responsableID,
        BuyTaskOnly=buyTaskOnly,
        FastDelivery=fastDelivery,
        Customization=customization,
        PrivateSession=privateSession,
    )
    if error_message == "":
        job_service = ClientProjectService(engine)
        job_service.create_job(
            ClientID=clientID,
            ProjectID=projectID,
            ResponsableID=responsableID,
            BuyTaskOnly=buyTaskOnly,
            FastDelivery=fastDelivery,
            Customization=customization,
            PrivateSession=privateSession,
            Status=0,
            Progress=0,
        )
        return jsonify({"message": "job created successfully"}), 201
    else:
        return jsonify({"error": error_message}), 400
