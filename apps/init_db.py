from config import app, db_serv
from empresa.model_empresa import Empresa

with app.app_context():
    db_serv.create_all()