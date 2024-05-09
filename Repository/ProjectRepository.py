from sqlalchemy import create_engine,ForeignKey,String,Column,Integer,CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
Base=declarative_base()

class Project(Base):
    __tablename__="project"
    identifier=Column("ID",Integer,primary_key=True)
    About=Column("About",String)
    Degree=Column("Degree",String)
    Name=Column("Name",String)
    Price=Column("Price",Integer)
    OptionsID=Column("OptionsID",ForeignKey=("options.OptionsID"))
    Demo=Column("Demo",Integer)
    def __init__(self,ID,About,Degree,Name,Price,OptionsID,Demo):
        self.Identifier=ID
        self.About=About
        self.Degree=Degree
        self.Name=Name
        self.Price=Price
        self.OptionsID=OptionsID
        self.Demo=Demo
    def __repr__(self):
        return f"Name : {self.About}\n ID: {self.identifier}\n Degree: {self.Degree}\n Name: {self.Name}\n Price: {self.Price} \n OptionsID: {self.OptionsID} \n Demo: {self.Demo}"
    