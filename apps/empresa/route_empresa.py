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