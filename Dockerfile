FROM python:3.12-slim

WORKDIR /app

COPY requiremensts.txt .
RUN pip install --user -r requiremensts.txt

COPY . .

EXPOSE 5002

CMD ["python", "apps/app.py"]



#-------------------------------------------------------------------#
#                       Ordens dos comandos                         #
#                                                                   #
#       1 - 'docker-compose build --no-cache api'                   #
#                                                                   #
#       Comando para atualizar a imagem da API.                     #
#       ele irá reconstruir a imagem do zero, garante               #
#       que todas as alterações no código sejam salvas              #
#                                                                   #
#       2 - 'docker-compose run -- api python apps/init_db.py'      #
#                                                                   #
#       Esse comando irá inicializar o banco de dados,              #
#       executando o script init_db.py que cira as tabelas no       #
#       MySQL.                                                      #
#                                                                   #
#       3 - 'docker-compose up'                                     #
#                                                                   #
#       Ele inicia a aplicação completa, subindo o contâiner        #
#       do MySQL (COm as tabelas já criadas)                        #
#-------------------------------------------------------------------#