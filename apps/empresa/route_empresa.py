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
    
