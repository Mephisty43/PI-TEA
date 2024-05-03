from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# Configurações do banco de dados
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'TeaSenha'
app.config['MYSQL_DB'] = 'PI-TEA'

mysql = MySQL(app)

# Cria a tabela 'locais' se não existir
with app.app_context():
    cursor = mysql.connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS locais (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        nome VARCHAR(255) NOT NULL,
                        endereco VARCHAR(255) NOT NULL)''')
    mysql.connection.commit()
    cursor.close()

@app.route('/locais', methods=['GET'])
def get_locais():
    with app.app_context():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT CODIGO,DESCRICAO FROM LOCALIDADES")
        locais = cursor.fetchall()
        cursor.close()
    return jsonify(locais)

@app.route('/locais', methods=['POST'])
def cadastrar_local():
    data = request.json
    descricao = data['descricao']
    localidade = data['localidade']

    with app.app_context():
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO LOCALIDADES (descricao, localidade) VALUES (%s, %s)", (descricao, localidade))
        mysql.connection.commit()
        cursor.close()

    return jsonify({'message': 'Local cadastrado com sucesso!'})

@app.route('/locais/<int:id>', methods=['PUT'])
def alterar_local(id):
    data = request.json
    descricao = data['descricao']
    localidade = data['localidade']

    with app.app_context():
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE LOCALIDADES SET descricao = %s, localidade = %s WHERE codigo = %s", (nome, endereco, id))
        mysql.connection.commit()
        cursor.close()

    return jsonify({'message': 'Local alterado com sucesso!'})

if __name__ == '__main__':
    app.run(debug=True)
