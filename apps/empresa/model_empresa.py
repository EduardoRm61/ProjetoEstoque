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

#####     Classes de Exceção:  ######

class EmpresaNaoEncontrada(Exception):
    def __init__(self, msg="Erro, Empresa não encontrada"):
        self.msg = msg
        super().__init__(self.msg)
    


######    Funções auxiliares:  ######
def criarEmpresa(nova_empresa):
    """
    Esta função tem como objetivo cadastrar uma nova empresa no 
    Banco de dados, ela recebe um dicionário entregue através da rota,
    assim adiciona ao banco.
    """
    db_serv.session.add(nova_empresa)
    db_serv.session.commit()
    return {"Descrição": "Empresa criada com êxito!"},200
        
def listarEmpresa():
    """
    Essa função faz uma requisição ao Banco de dados, retornando todas
    as empresas cadastradas e assim as retorna.
    """
    empresas = Empresa.quary.all()
    return[empresa.to_dict() for empresa in empresas]

def resetarEmpresa():
    db_serv.session.delete()
    db_serv.session.commit()
    return

def deletarEmpresaPorId(id_empresa):
    empresa = Empresa.query.get(id_empresa)
    db_serv.session.delete(empresa)
    db_serv.session.commit()
    return

# def alterarInfoEmpresa(razao_social, nome_fantasia, endereco, cnpj, id_empresa):
#     nv_dict = Empresa.query.get(id_empresa)
#     try:
#         if not nv_dict: