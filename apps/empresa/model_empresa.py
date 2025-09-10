from config import db_serv

class Empresa(db_serv.Model): # Estou criand a class empresa que herda de db_serv
    __tablename__ = "empresas"
    __table_args__ = {'extend_existing': True}

    id = db_serv.Column(db_serv.Integer, primary_key=True)
    razao_social = db_serv.Column(db_serv.String(100), nullable=False)
    nome_fantasia = db_serv.Column(db_serv.String(100), nullable=False)
    endereco = db_serv.Column(db_serv.String(80), nullable=False)
    cnpj = db_serv.Column(db_serv.String(30), nullable=False)

    def __init__(self, razao_social, nome_fantasia, endereco, cnpj):
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

class EmpresaSemId(Exception):
    def __init__(self, msg="Não é possível cadastrar uma empresa sem 'id!"):
        self.msg = msg
        super().__init__(self.msg)

class EmpresaSemRazaoSocial(Exception):
    def __init__(self, msg="Não é possível cadastrar uma empresa sem a 'Razão Social' "):
        self.msg = msg
        super().__init__(self.msg)

class EmpresaSemNomeFantasia(Exception):
    def __init__(self, msg="Não é possível cadastrar uma empresa sem o 'Nome Fantasia' "):
        self.msg = msg
        super().__init__(self.msg)

class EmpresaSemEndereco(Exception):
    def __init__(self, msg="Não é possível cadastrar uma empresa sem o 'Endereço' "):
        self.msg = msg
        super().__init__(self.msg)

class EmpresaSemCNPJ(Exception):
    def __init__(self, msg="Não é possível cadastrar uma empresa sem o 'CNPJ' "):
        self.msg = msg
        super().__init__(self.msg)

class CampoSemDados(Exception):
    def __init__(self, msg="O corpo da requisição está vazio! Preecha todos os campos"):
        self.msg = msg
        super().__init__(self.msg)


######    Funções auxiliares:  ######
def criarEmpresa(nova_empresa):
    """
    Esta função tem como objetivo cadastrar uma nova empresa no 
    Banco de dados, ela recebe um dicionário entregue através da rota,
    assim adiciona ao banco. Retornando True ou Falso a depender do caso.
    """
    try:
        db_serv.session.add(nova_empresa)
        db_serv.session.commit()
        return True
    except Exception as e:
        print(f"Erro ao criar empresa: {e}")
        return False
    
        
def listarEmpresa():
    """
    Essa função faz uma requisição ao Banco de dados de todas as empresas
    cadastradas armazenando em uma variável, assim através de um for ela
    itera sobre todos os dados e os retorna. 
    """
    empresas = Empresa.query.all()
    return[empresa.to_dict() for empresa in empresas]


def resetarEmpresa():
    """
    Esta função tem como objetivo resetar todas as informações da tabela
    Empresa no Banco de dados. Sem parâmetro. Não retorna nada.
    """
    db_serv.session.delete()
    db_serv.session.commit()
    return


def deletarEmpresaPorId(id_empresa):
    """
    Esta função deleta uma empresa pelo seu id, tem como parâmetro o id da
    empresa, faz uma requisição ao Banco de Dados e remove a empresa com o id
    correspondente, sem retornar nada.
    """
    empresa = Empresa.query.get(id_empresa)
    db_serv.session.delete(empresa)
    db_serv.session.commit()
    return


def listarEmpresaPorId(id_empresa):
    """
    Busca uma empresa no banco de dados por ID.
    Retorna o objeto da empresa se encontrada, ou levanta uma exceção.
    """
    empresa = Empresa.query.get(id_empresa)
    if empresa is None:
        raise EmpresaNaoEncontrada()
    return empresa.to_dict()

def procurarEmpresa(id_empresa):
    """
    Procura uma empresa no banco de dados pelo seu id, verifica se
    o id/empresa realmente existe, retornando True ou Falso a depender
    da situação.
    """
    empresa = Empresa.query.get(id_empresa)
    if empresa is None:
        return False
    else:
        return True
    

def alterarEmpresa(id_empresa, dados_atualizados):
    """
    Busca e atualiza os dados de uma empresca no banco de dados,
    caso a mesma não seja encontrada, é levantada uma exceção
    """
    
    empresa = Empresa.query.get(id_empresa)
    if empresa is None:
        raise EmpresaNaoEncontrada()
        
    empresa.razao_social = dados_atualizados.get('razao_social', empresa.razao_social)
    empresa.nome_fantasia = dados_atualizados.get('nome_fantasia', empresa.nome_fantasia)
    empresa.endereco = dados_atualizados.get('endereco', empresa.endereco)
    empresa.cnpj = dados_atualizados.get('cnpj', empresa.cnpj)

    db_serv.session.commit()
    return empresa.to_dict()
    

        
        