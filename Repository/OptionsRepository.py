from sqlalchemy import create_engine,ForeignKey,Boolean,String,Column,Integer,CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
Base=declarative_base()

class Options(Base):
    __tablename__="options"
    identifier=Column("OptionsID",Integer,primary_key=True)
    Custimization=Column("Custimization",String)
    FastDelivery=Column("FastDelivery",Boolean)
    PrivateSession=Column("PrivateSession",Boolean)
    ProjectID=Column("ProjectID",ForeignKey("project.ID"))
    BuyNotFullProject=Column("ButNotFullProject",Boolean)
    
    def __init__(self,ID,Custimization,FastDelivery,PrivateSession,ProjectID,BuyNotFullProject):
        self.Identifier=ID
        self.Custimization=Custimization
        self.FastDelivery=FastDelivery
        self.PrivateSession=PrivateSession
        self.ProjectID=ProjectID
        self.BuyNotFullProject=BuyNotFullProject
    def __repr__(self):
        return f"ID: {self.identifier}\n Custimization : {self.Custimization}\n ID: {self.ID}\n FastDelivery: {self.FastDelivery}\n PrivateSession: {self.PrivateSession}\n ProjectID: {self.ProjectID} \n BuyNotFullProject : {self.BuyNotFullProject}"
    