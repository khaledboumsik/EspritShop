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

    def change_satus_to_active(self, ID):
        session = self.Session()
        row_to_edit = session.query(ClientProject).filter_by(identifier=ID).first()

        if row_to_edit:
            row_to_edit.Status = 1
            row_to_edit.field_to_change = row_to_edit
            session.commit()
            print("Row with ID {} updated successfully.".format(ID))
        else:
            print("Row with ID {} not found.".format(ID))

    def change_satus_to_inactive(self, ID):
        session = self.Session()
        row_to_edit = session.query(ClientProject).filter_by(identifier=ID).first()

        if row_to_edit:
            row_to_edit.Status = 0
            row_to_edit.field_to_change = row_to_edit
            session.commit()
            print("Row with ID {} updated successfully.".format(ID))
        else:
            print("Row with ID {} not found.".format(ID))

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
    def get_all_jobs(self):
        session=self.Session()
        selected_jobs=(session.query(ClientProject).all())
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
    def get_active_jobs(self):
        session = self.Session()
        selected_jobs = (
            session.query(ClientProject).filter_by(Status=1).all()
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

    def get_inactive_jobs(self):
        session = self.Session()
        selected_jobs = (
            session.query(ClientProject).filter_by(Status=0).all()
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
