from config import db_serv
from datetime import datetime, timezone
from sqlalchemy import ForeignKey

# Definindo a Superclasse Usuário
class Usuario(db_serv.Model):
    __tablename__ = 'usuarios'

    # Está coluna irá diferenciar os tipos de usuário
    tipo_usuario = db_serv.Column(db_serv.String(50))
    __mapper_args__ = {
        'polymorphic_identity': 'usuario',
        'polymorphic_on': tipo_usuario
    }

    id = db_serv.Column(db_serv.Integer, primary_key=True)
    nome = db_serv.Column(db_serv.String(100),nullable=False)
    email = db_serv.Column(db_serv.String(120),unique=True,nullable=False)
    cpf = db_serv.Column(db_serv.String(14),unique=True,nullable=False)
    senha_hash = db_serv.Column(db_serv.String(255),nullable=False)
    status_cadastro = db_serv.Column(db_serv.Enum('Pendente','Aprovado','Rejeitado'), default='Pendente')
    data_cadastro = db_serv.Column(db_serv.DateTime,default=datetime.now(timezone.utc))

