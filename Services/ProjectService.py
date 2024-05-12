from sqlalchemy.orm import sessionmaker
import sys
sys.path.append(r'C:\Users\Khaled\Desktop\ESPRITSHOP')
from Repository.ProjectRepository import Project

class ProjectService:
    def __init__(self, engine):
        self.Session = sessionmaker(bind=engine)

    def create_project(self, About, Degree, Name,Price,Demo):
        session = self.Session()
        project = Project(About=About, Degree=Degree, Name=Name,Price=Price,Demo=Demo)
        session.add(project)
        session.commit()
        session.close()
    def get_projects_by_degree(self,Degree):
        session=self.Session()
        selected_projects=session.query(Project).filter_by(Degree=Degree).all()
        session.close
        return [{"id": project.Identifier, "About": project.About, "Degree":project.Degree ,"Name": project.Name,"Price":project.Price,"Demo":project.Demo} for project in selected_projects ]if selected_projects else {}
    def get_project_by_ID(self, ID):
        session = self.Session()
        selected_project = session.query(Project).filter_by(Identifier=ID).first() 
        session.close() 
        return {"id": selected_project.Identifier, "About": selected_project.About, "Degree":selected_project.Degree ,"Name": selected_project.Name,"Price":selected_project.Price,"Demo":selected_project.Demo} if selected_project else {}