from sqlalchemy import create_engine,ForeignKey,String,Column,Integer,CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship
Base=declarative_base()

class Project(Base):
    __tablename__ = "project"
    Identifier = Column("ID", Integer, primary_key=True, autoincrement=True)
    About = Column("About", String)
    Degree = Column("Degree", String)
    Name = Column("Name", String)
    Price = Column("Price", Integer)
    Demo = Column("Demo", String)
    project_clients = relationship("ClientProject", back_populates="project")
    
    def __init__(self, About, Degree, Name, Price, Demo):
        self.About = About
        self.Degree = Degree
        self.Name = Name
        self.Price = Price
        self.Demo = Demo
    
    def __repr__(self):
        return f"About: {self.About}\n ID: {self.Identifier}\n Degree: {self.Degree}\n Name: {self.Name}\n Price: {self.Price} \n  Demo: {self.Demo}"