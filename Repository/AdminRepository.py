from sqlalchemy import create_engine,ForeignKey,Boolean,String,Column,Integer,CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from main import db

class Admin(db.Model):
    __tablename__="admin"
    identifier=Column("ID",Integer,primary_key=True,autoincrement=True)
    Login=Column("Login",String)
    Password=Column("Password",String)
    Status=Column("Status",Boolean)
    PhoneNumber=Column("PhoneNumber",Integer)
    Email=Column("Email",String)
    admin_projects = relationship("ClientProject", back_populates="admin")
    def __init__(self,Login,Password,Status,PhoneNumber,Email):
        self.Login=Login
        self.Password=Password
        self.Status=Status
        self.PhoneNumber=PhoneNumber
        self.Email=Email
        
    def __repr__(self):
        return f"Login : {self.Login}\n ID: {self.Identifier}\n Password: {self.Password}\n Status: {self.Status}\n PhoneNumber: {self.PhoneNumber}\n Email: {self.Email}"
    