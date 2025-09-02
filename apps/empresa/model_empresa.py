from config import db_serv

class Empresa(db_serv.Model): # Estou criand a class empresa que herda de db_serv
    __tablename__ = "empresas"
    __table_args__ = {'extend_existing': True}

    id = db_serv.Column(db_serv.Integer, primary_key=True)
    razao_social = db_serv.Column(db_serv.String(100), nullable=False)
    nome_fantasia = db_serv.Column(db_serv.String(100), nullable=False)
    endereco = db_serv.Column(db_serv.String(80), nullable=False)
    cnpj = db_serv.Column(db_serv.String(30), nullable=False)

    def __init__(self, id, razao_social, nome_fantasia, endereco, cnpj):
        self.id = id
        self.razao_social = razao_social
        self.nome_fantasia = nome_fantasia
        self.endereco = endereco
        self.cnpj = cnpj

    def to_dict(self):
        return {
            "id": self.id,
            "razao_social": self.razao_social,
            "nome_fantasia": self.nome_fantasia,
            "endereco": self.endereco,
            "cnpj":self.cnpj
    }
        