from flask import Blueprint, request, jsonify
import empresa.model_empresa as modEmp



bd_Empresa = Blueprint("/empresa", __name__)


@bd_Empresa.route("/empresa", methods=["GET"])
def listar_empresas():
    try:
        empresa = modEmp.listarEmpresa()
        return jsonify (empresa)
    except Exception as e:
        return {"Erro": str(e)}, 400
    

@bd_Empresa.route("/empresa/<int:id_empresa>",methods=["GET"])
def empresa_por_id(id_empresa):
    try:
        return modEmp.listarEmpresaPorId(id_empresa), 200
    except Exception as e:
        return jsonify ({
            "Erro": "Não foi possível fazer a requisição",
            "Descrição": str(e)
        }), 500
    
@bd_Empresa.route("/empresa",methods=["POST"])
def cria_empresa():
    try:
        dict_empresa = request.get_json()

        if not dict_empresa or 'id' not in dict_empresa:
            return jsonify ({"Erro": modEmp.EmpresaSemId().msg}),400
        if not dict_empresa or 'razao_social' not in dict_empresa:
            return jsonify ({"Erro": modEmp.EmpresaSemRazaoSocial().msg}),400
        if not dict_empresa or 'nome_fantasia' not in dict_empresa:
            return jsonify({"Erro": modEmp.EmpresaSemNomeFantasia().msg}),400
        if not dict_empresa or 'endereco' not in dict_empresa:
            return jsonify({"Erro": modEmp.EmpresaSemEndereco().msg}), 400
        if not dict_empresa or 'cnpj' not in dict_empresa:
            return jsonify({"Erro": modEmp.EmpresaSemCNPJ().msg}), 400
        
        return modEmp.criarEmpresa(dict_empresa),200
    
    except Exception as e:
        return jsonify ({
            "Erro": "Não foi possível executar a requisição",
            "Detalhes": str(e)
        }), 500
    

