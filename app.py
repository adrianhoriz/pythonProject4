from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Conectar ao banco de dados
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ae2208ae",
    database="MissaoRS"
)

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para lidar com o envio do formulário de cadastro de pessoas resgatadas
@app.route('/cadastrar_resgatado', methods=['GET', 'POST'])
def cadastrar_resgatado():
    if request.method == 'POST':
        nome = request.form['nome']
        regiao = request.form['regiao']
        nome_pai = request.form['nome_pai']
        nome_mae = request.form['nome_mae']
        irmaos = request.form['irmaos']
        idade = request.form['idade']
        filhos = request.form['filhos']

        cursor = conexao.cursor()
        sql = "INSERT INTO Resgatados (nome, Regiao, nome_pai, nome_mae, irmaos, idade, filhos) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (nome, regiao, nome_pai, nome_mae, irmaos, idade, filhos)
        cursor.execute(sql, val)
        conexao.commit()
        print("Pessoa resgatada cadastrada com sucesso")

        return redirect(url_for('index'))
    else:
        return render_template('cadastrar_resgatado.html')

# Rota para a página de cadastro de pessoas desaparecidas
@app.route('/cadastrar_desaparecido')
def cadastrar_desaparecido():
    return render_template('cadastrar_desaparecido.html')

# Rota para lidar com o envio do formulário de cadastro de pessoas desaparecidas
@app.route('/cadastrar_desaparecido', methods=['POST'])
def cadastrar_desaparecido_post():
    # Obter dados do formulário
    seu_nome = request.form['seu_nome']
    nome_desaparecido = request.form['nome_desaparecido']
    regiao = request.form['regiao']
    idade = request.form['idade']
    seu_telefone = request.form['seu_telefone']

    # Inserir os dados no banco de dados
    cursor = conexao.cursor()
    sql = "INSERT INTO Desaparecidos (seu_nome, nome_Desaparecido, Regiao, idade, seu_telefone) VALUES (%s, %s, %s, %s, %s)"
    val = (seu_nome, nome_desaparecido, regiao, idade, seu_telefone)
    cursor.execute(sql, val)
    conexao.commit()
    print("Pessoa desaparecida cadastrada com sucesso")

    return redirect(url_for('index'))

# Rota para mostrar as tabelas de resgatados e desaparecidos
@app.route('/mostrar_tabelas')
def mostrar_tabelas():
    # Consulta SQL para selecionar todos os registros da tabela Resgatados
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Resgatados")
    resgatados = cursor.fetchall()

    # Consulta SQL para selecionar todos os registros da tabela Desaparecidos
    cursor.execute("SELECT * FROM Desaparecidos")
    desaparecidos = cursor.fetchall()

    return render_template('mostrar_tabelas.html', resgatados=resgatados, desaparecidos=desaparecidos)


if __name__ == '__main__':
    app.run(debug=True)