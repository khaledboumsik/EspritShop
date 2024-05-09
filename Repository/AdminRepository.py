from sqlalchemy import create_engine,ForeignKey,Boolean,String,Column,Integer,CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
Base=declarative_base()

class Admin(Base):
    __tablename__="admin"
    identifier=Column("ID",Integer,primary_key=True)
    Login=Column("Login",String)
    Password=Column("Password",String)
    Status=Column("Status",Boolean)
    def __init__(self,identifier,Login,Password,Status):
        self.Identifier=identifier
        self.Login=Login
        self.Password=Password
        self.Status=Status
        
    def __repr__(self):
        return f"Login : {self.Login}\n ID: {self.Identifier}\n Password: {self.Password}\n Status: {self.Status}"
    