from config import db_serv
from datetime import datetime, timezone
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

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

    def __init__(self, nome, email, cpf, senha_hash):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.senha_hash = senha_hash

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "cpf": self.cpf,
            "status_cadastro": self.status_cadastro.value,
            "data_cadastro": self.data_cadastro.isoformat()
        }

# Definindo a Subclasse 1: Estoquista
class Estoquista(Usuario):
    __tablename__ = 'estoquistas'
    __mapper_args__ = {'polymorphic_identity': 'estoquista'}

    id = db_serv.Column(db_serv.Integer,ForeignKey('usuarios.id'),primary_key=True)

    # Definindo o relacionamento com a Empresa
    id_empresa = db_serv.Column(db_serv.Integer,db_serv.ForeignKey('empresas.id'),nullable=False)
    empresa = db_serv.relationship("Empresa", back_populates="estoquistas")


class Empresario(Usuario):
    __tablename__ = 'empresarios'
    __mapper_args__ = {'polymorphic_identity': 'empresario'}

    id = db_serv.Column(db_serv.Integer, ForeignKey('usuarios.id'),primary_key=True)

    # Definindo o relacionamento com a Empresa
    empresas = db_serv.relationship("Empresa", back_populates="dono")

