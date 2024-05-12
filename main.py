from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost:3306/espritshopmaindb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        # Import your models here
        from Repository.ClientRepository import Client
        from Repository.ProjectRepository import Project
        from Repository.AdminRepository import Admin
        from Repository.ClientProjectRepository import ClientProject
        # Import your Controllers here
        from Controllers.ClientController import client_blue_print
        from Controllers.ProjectController import project_blue_print
        from Controllers.AdminController import admin_blue_print
        from Controllers.ClientProjectController import job_blue_print
        # Register your blueprints here
        app.register_blueprint(client_blue_print)
        app.register_blueprint(project_blue_print)
        app.register_blueprint(admin_blue_print)
        app.register_blueprint(job_blue_print)

    return app