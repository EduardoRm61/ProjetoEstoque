from config import app, db_serv
from empresa.route_empresa import bd_Empresa
from flask_sqlalchemy import SQLAlchemy

app.register_blueprint(bd_Empresa)

if __name__ == '__main__':
    app.run(host = app.config['HOST'], port= app.config['PORT'],debug=app.config['DEBUG'])