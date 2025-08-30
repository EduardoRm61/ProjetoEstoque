from flask import Flask, request, jsonify


empresa = {"empresa":[
    {"nome_fantasia": "Google"},
    {"razao_social": "Google Brasil Internet Ltda"},
    {"endereco":"Avenida Brigadeiro Faria Lima, 3477 - Vila Olímpia"},
    {"cnpj":"06.990.590/0001-23"},
    {"id_empresa":1}
]}

app = Flask(__name__) # Criamos um objeto app que será responsável por
# criar o aplicativo web

@app.route("/empresa",methods=['GET'])
def mostrar_empresa():
    return jsonify(empresa)


if __name__ == '__main__':
    app.run(host = 'localhost', port= 5002, debug= True)