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

        if not dict_empresa or 'razao_social' not in dict_empresa:
            return jsonify ({"Erro": modEmp.EmpresaSemRazaoSocial().msg}),400
        if not dict_empresa or 'nome_fantasia' not in dict_empresa:
            return jsonify({"Erro": modEmp.EmpresaSemNomeFantasia().msg}),400
        if not dict_empresa or 'endereco' not in dict_empresa:
            return jsonify({"Erro": modEmp.EmpresaSemEndereco().msg}), 400
        if not dict_empresa or 'cnpj' not in dict_empresa:
            return jsonify({"Erro": modEmp.EmpresaSemCNPJ().msg}), 400
        
        nova_empresa = modEmp.Empresa(
            razao_social=dict_empresa["razao_social"],
            nome_fantasia=dict_empresa["nome_fantasia"],
            endereco=dict_empresa["endereco"],
            cnpj=dict_empresa["cnpj"]
        )

        modEmp.criarEmpresa(nova_empresa)
        return jsonify({"Mensagem": "Empresa criada com sucesso!"}),201
    
    except Exception as e:
        return jsonify ({
            "Erro": "Não foi possível executar a requisição",
            "Detalhes": str(e)
        }), 500
    

    
@bd_Empresa.route("/empresa/<int:id>",methods=["PUT"])
def alterar_empresa(id):
    try:
        dict_empresa = request.get_json()

        if not dict_empresa:
            return jsonify ({
                "Erro": "Não foi possível realizar a requisição",
                "Descrição": "O corpo da requisição está vazio, preencha todos os campos"
            }), 400
        
        if 'razao_social' not in dict_empresa:
            return jsonify ({
                "Erro": modEmp.EmpresaSemRazaoSocial().msg
            }), 400
        
        if 'nome_fantasia' not in dict_empresa and "nome_fantasia" == "":
            return jsonify ({
                "Erro": modEmp.EmpresaSemNomeFantasia().msg
            }), 400
        
        if 'endereco' not in dict_empresa:
            return jsonify ({
                "Erro": modEmp.EmpresaSemEndereco().msg
            }), 400
        
        if 'cnpj' not in dict_empresa:
            return jsonify ({
                "Erro": modEmp.EmpresaSemCNPJ().msg
            }), 400
        
        # nv_dados = modEmp.Empresa(
        #     razao_social=dict_empresa["razao_social"],
        #     nome_fantasia=dict_empresa["nome_fantasia"],
        #     endereco=dict_empresa["endereco"],
        #     cnpj=dict_empresa["cnpj"]
        # )

        modEmp.alterarEmpresa(id, dict_empresa)
        return jsonify ({"Mensagem": "Dados da empresa alterado com sucesso"}), 200
    
    except Exception as e:
        return jsonify({
            "Erro": "Não foi possível processar a requisição",
            "Detalhes": str(e)
        }), 500