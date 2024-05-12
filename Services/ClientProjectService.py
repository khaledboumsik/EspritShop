from sqlalchemy.orm import sessionmaker
import sys

sys.path.append(r"C:\Users\Khaled\Desktop\ESPRITSHOP")
from Repository.ClientProjectRepository import ClientProject


class ClientProjectService:
    def __init__(self, engine):
        self.Session = sessionmaker(bind=engine)

    def create_job(
        self,
        ClientID,
        ProjectID,
        Progress,
        ResponsableID,
        Status,
        BuyTaskOnly,
        Customization,
        FastDelivery,
        PrivateSession,
    ):
        session = self.Session()
        job = ClientProject(
            ClientID=ClientID,
            ProjectID=ProjectID,
            Progress=Progress,
            ResponsableID=ResponsableID,
            Status=Status,
            BuyTaskOnly=BuyTaskOnly,
            Customization=Customization,
            FastDelivery=FastDelivery,
            PrivateSession=PrivateSession,
        )
        session.add(job)
        session.commit()
        session.close()

    def get_job_by_ID(self, ID):
        session = self.Session()
        selected_job = session.query(ClientProject).filter_by(identifier=ID).first()
        session.close()
        return (
            {
                "id": selected_job.identifier,
                "ClientID": selected_job.ClientID,
                "ProjectID": selected_job.ProjectID,
                "ResponsableID": selected_job.ResponsableID,
                "Status": selected_job.Status,
                "BuyTaskOnly": selected_job.BuyTaskOnly,
                "Customization": selected_job.Customization,
                "FastDelivery": selected_job.FastDelivery,
                "PrivateSession": selected_job.PrivateSession,
            }
            if selected_job
            else {}
        )

    def get_jobs_by_project(self, ProjectID):
        session = self.Session()
        selected_jobs = (
            session.query(ClientProject).filter_by(ProjectID=ProjectID).all()
        )
        session.close()
        return (
            [
                {
                    "id": job.identifier,
                    "ClientID": job.ClientID,
                    "ProjectID": job.ProjectID,
                    "ResponsableID": job.ResponsableID,
                    "Status": job.Status,
                    "BuyTaskOnly": job.BuyTaskOnly,
                    "Customization": job.Customization,
                    "FastDelivery": job.FastDelivery,
                    "PrivateSession": job.PrivateSession,
                }
                for job in selected_jobs
            ]
            if selected_jobs
            else {}
        )

    def get_jobs_by_client(self, ClientID):
        session = self.Session()
        selected_jobs = (
            session.query(ClientProject).filter_by(identifier=ClientID).all()
        )
        session.close()
        return (
            [
                {
                    "id": job.identifier,
                    "ClientID": job.ClientID,
                    "ProjectID": job.ProjectID,
                    "ResponsableID": job.ResponsableID,
                    "Status": job.Status,
                    "BuyTaskOnly": job.BuyTaskOnly,
                    "Customization": job.Customization,
                    "FastDelivery": job.FastDelivery,
                    "PrivateSession": job.PrivateSession,
                }
                for job in selected_jobs
            ]
            if selected_jobs
            else {}
        )
