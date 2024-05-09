from sqlalchemy import create_engine,ForeignKey,Boolean,String,Column,Integer,CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
Base=declarative_base()

class ClientProject(Base):
    __tablename__="clientproject"
    identifier=Column("ID",Integer,primary_key=True)
    ClientID=Column("ClientID",ForeignKey=("client.ID"))
    ProjectID=Column("ProjectID",ForeignKey=("project.ID"))
    Progress=Column("Progress",int)
    ResponsableID=Column("ResponsableID",ForeignKey=("admin.ID"))
    Status=Column("Status",Boolean)
    
    def __init__(self,ID,ClientID,ProjectID,Progress,ResponsableID,Status):
        self.Identifier=ID
        self.ClientID=ClientID
        self.ProjectID=ProjectID
        self.Progress=Progress
        self.ResponsableID=ResponsableID
        self.Status=Status
    def __repr__(self):
        return f"ID: {self.identifier}\n ClientID : {self.ClientID}\n ID: {self.ID}\n ProjectID: {self.ProjectID}\n Progress: {self.Progress}\n ResponsableID: {self.ResponsableID}\n Status : {self.Status}"
    
    