from sqlalchemy.orm import sessionmaker
import sys
sys.path.append(r'C:\Users\Khaled\Desktop\ESPRITSHOP')
from Repository.AdminRepository import Admin

class AdminService:
    def __init__(self, engine):
        self.Session = sessionmaker(bind=engine)

    def create_admin(self,Login,Password,Status,PhoneNumber,Email):
        session = self.Session()
        admin = Admin(Login=Login, Password=Password, Status=Status, PhoneNumber=PhoneNumber,Email=Email)
        session.add(admin)
        session.commit()
        session.close()
    
    def get_admin_by_ID(self, ID):
        session = self.Session()
        selected_admin = session.query(Admin).filter_by(identifier=ID).first() 
        session.close() 
        return {"id": selected_admin.identifier, "name": selected_admin.Login, "PhoneNumber":selected_admin.PhoneNumber ,"Email": selected_admin.Email,"PhoneNumber":selected_admin.PhoneNumber,"Email":selected_admin.Email} if selected_admin else {}