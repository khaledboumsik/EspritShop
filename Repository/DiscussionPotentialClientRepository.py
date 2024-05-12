from sqlalchemy import create_engine,ForeignKey,Boolean,String,Column,Integer,CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from main import db

class DiscussionPotentialClient(db.Model):
    __tablename__="discussionpotentialclient"
    identifier=Column("DiscussionID",Integer,primary_key=True)
    AdminID=Column("AdminID",ForeignKey=("admin.ID"))
    ClientID=Column("ClientID",ForeignKey=("client.ID"))
    Messages=Column("Messages",String)
    Status=Column("Status",Boolean)
    def __init__(self,ID,AdminID,ClientID,Messages,Status):
        self.Identifier=ID
        self.AdminID=AdminID
        self.ClientID=ClientID
        self.Messages=Messages
        self.Status=Status
        
    def __repr__(self):
        return f"Messages : {self.AdminID}\n ID: {self.identifier}\n ClientID: {self.ClientID}\n Messages: {self.Name}\n Status: {self.Status}"
    