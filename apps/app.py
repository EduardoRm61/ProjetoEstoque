from config import app, db_serv
from empresa.route_empresa import bd_Empresa
from flask_sqlalchemy import SQLAlchemy

app.register_blueprint(bd_Empresa)

if __name__ == '__main__':
    app.run(host = 'localhost', port= 5002, debug= True)