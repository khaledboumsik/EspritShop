from sqlalchemy import create_engine,ForeignKey,Boolean,String,Column,Integer,CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
Base=declarative_base()

class DiscussionClient(Base):
    __tablename__="discussionclient"
    identifier=Column("DiscussionID",Integer,primary_key=True)
    Messages=Column("Messages",String)
    AdminID=Column("AdminID",int)
    Status=Column("Status",Boolean)
    WorkID=Column("WorkID",ForeignKey=("clientproject.WorkID"))
    
    def __init__(self,ID,Messages,AdminID,Status,WorkID):
        self.Identifier=ID
        self.Messages=Messages
        self.AdminID=AdminID
        self.Status=Status
        self.WorkID=WorkID
    def __repr__(self):
        return f"ID: {self.identifier}\n Messages : {self.Messages}\n AdminID: {self.AdminID}\n Status: {self.Status}\n WorkID: {self.WorkID}"
    