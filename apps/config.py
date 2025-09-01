# 1 -Importando as bibliotecas necessárias:
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 2 - Estou criando uma instância do Flask e salvando na variável app
# Flask é a classe "molde" ou a "planta" para cria um aplicativo web

app = Flask(__name__)


# 3 - Configuração para o aplicativo flask 

# estou definindo o endereço IP que o servidor irá "escutar"
# No caso o "0.0.0.0" significa que ele está disponível para qualquer endereço IP,
# como container e embiente virtual.
# A porta onde o app Flask irá rodar, 5000 é do flask e 5002 defini agora
# Quando o DEBUG é True o Flask ativa as seguintes funcionalidades:
# O Flask reinicia o servidor automaticamente toda vez que faz alteração no seu código fonte
# e caso haja um erro na aplicação o Flask exibirá um depurador interativo no navegador

app.config["HOST"] = "0.0.0.0" 
app.config["PORT"] = 5002 
app.config["DEBUG"] = True # 

# 4 - Definindo as variáveis de ambiente
# 'os.environ' é um objeto que age como um dicionário, contendo as variáveis de ambiente
# que foram configuradas no seu computador ou servidor.
# o método '.get("NOME_DA_VARIAVEL")' é usado para pegar o valor de
# uma variável específica dentro desse dicionário.


DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")