from sqlalchemy import create_engine,ForeignKey,String,Column,Integer,CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from main import db
class Client(db.Model):
    __tablename__ = "client"
    identifier = Column("ID", Integer, primary_key=True, autoincrement=True)
    LoginName = Column("LoginName", String)
    Password = Column("Password", String)
    Email = Column("Email", String)
    PhoneNumber = Column("PhoneNumber", Integer)
    client_projects = relationship("ClientProject", back_populates="client")
    def __init__(self, LoginName, Password, Email, PhoneNumber):
        self.LoginName = LoginName
        self.Password = Password
        self.Email = Email
        self.PhoneNumber = PhoneNumber
    
    def __repr__(self):
        return f"Name: {self.LoginName}\nIdentifier: {self.identifier}\nPassword: {self.Password}\nEmail: {self.Email}\nPhoneNumber: {self.PhoneNumber}"