from sqlalchemy.orm import sessionmaker
import sys
sys.path.append(r'C:\Users\Khaled\Desktop\ESPRITSHOP')
from Repository.ClientRepository import Client

class ClientService:
    def __init__(self, engine):
        self.Session = sessionmaker(bind=engine)

    def create_user(self, Username, Password, Email, PhoneNumber):
        session = self.Session()
        client = Client(LoginName=Username, Password=Password, Email=Email, PhoneNumber=PhoneNumber)
        session.add(client)
        session.commit()
        session.close()
    
    def get_client_by_ID(self, ID):
        session = self.Session()
        my_user = session.query(Client).filter_by(identifier=ID).first()  # Query Client by ID
        session.close() 
        return {"id": my_user.identifier, "name": my_user.LoginName} if my_user else {}