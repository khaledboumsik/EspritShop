from sqlalchemy import create_engine, ForeignKey, Boolean, String, Column, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from .ClientRepository import Client
from .ProjectRepository import Project
from .AdminRepository import Admin
Base = declarative_base()
from Repository.ClientRepository import Client
from Repository.ProjectRepository import Project
from Repository.AdminRepository import Admin

class ClientProject(Base):
    __tablename__ = "clientproject"

    identifier = Column("WorkID", Integer, primary_key=True, autoincrement=True)
    ClientID = Column("ClientID",Integer,ForeignKey("client.ID"))
    ProjectID = Column("ProjectID", Integer,ForeignKey("project.ID"))
    Progress = Column("Progress", Integer)
    ResponsableID = Column("ResponsableID", Integer,ForeignKey("admin.ID"))
    Status = Column("Status", Boolean)
    BuyTaskOnly = Column("BuyTaskOnly", Boolean)
    Customization = Column("Customization", String)
    FastDelivery = Column("FastDelivery", Boolean)
    PrivateSession = Column("PrivateSession", Boolean)
    client = relationship("Client", back_populates="client_projects")
    project = relationship("Project", back_populates="project_clients")
    admin = relationship("Admin", back_populates="admin_projects")

    def __init__(self, ClientID, ProjectID, ResponsableID,BuyTaskOnly,Customization,FastDelivery,PrivateSession,Status=0,Progress=0):
        self.ClientID = ClientID
        self.ProjectID = ProjectID
        self.Progress = Progress
        self.ResponsableID = ResponsableID
        self.Status = Status
        self.BuyTaskOnly=BuyTaskOnly
        self.Customization=Customization
        self.FastDelivery=FastDelivery
        self.PrivateSession=PrivateSession

    def __repr__(self):
        return f"ID: {self.identifier}\n ClientID : {self.ClientID}\n ID: {self.ID}\n ProjectID: {self.ProjectID}\n Progress: {self.Progress}\n ResponsableID: {self.ResponsableID}\n Status : {self.Status}\n BuyTaskOnly : {self.BuyTaskOnly}\n Customization : {self.Customization},\n FastDelivery : {self.FastDelivery}\n PrivateSession : {self.PrivateSession}"
