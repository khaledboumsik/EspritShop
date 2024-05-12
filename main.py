from flask import Flask
import sys
sys.path.append(r'C:\Users\Khaled\Desktop\ESPRITSHOP')
from Controllers.ClientController import client_blue_print
from Controllers.ProjectController import project_blue_print
from Controllers.AdminController import admin_blue_print
app = Flask(__name__)

app.register_blueprint(client_blue_print)
app.register_blueprint(project_blue_print)
app.register_blueprint(admin_blue_print)
if __name__ == '__main__':
    app.run(debug=True)