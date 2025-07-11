from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
from flask_mysqldb import MySQL
import os

app = Flask(__name__)
app.secret_key = 'minha_chave_secreta'  # Usada para sessões

# Permitir acessar arquivos da pasta styles
@app.route('/styles/<path:filename>')
def styles(filename):
    return send_from_directory(os.path.join(app.root_path, 'templates', 'styles'), filename)

# Configuração do banco de dados
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'shoesmixweb'

mysql = MySQL(app)

# Página inicial (index)
@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM produtos")
    produtos = cur.fetchall()
    cur.close()

    # Verifica se o usuário está logado e passa o nome do usuário para o template
    nome_usuario = session.get('nome_usuario', None)

    return render_template('index.html', produtos=produtos, nome_usuario=nome_usuario)

# Página de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    erro = None

    if request.method == 'POST':
        email = request.form['email'].strip().lower()
        senha = request.form['senha'].strip()

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM usuarios WHERE email = %s AND senha = %s", (email, senha))
        usuario = cur.fetchone()
        cur.close()

        if usuario:
            session['usuario'] = email  # salva o email na sessão
            session['nome_usuario'] = usuario[0]  # salva o nome do usuário na sessão

            # Redireciona admin para a área administrativa
            if email == 'admin@shoesmix.com' and senha == 'admin123' and usuario[1].lower() == 'admin':
                return redirect(url_for('admin'))

            # Senão, vai para a página de usuário logado
            return redirect(url_for('usuario'))

        else:
            erro = 'Email ou senha inválidos.'

    return render_template('login.html', erro=erro)

# Página de usuário logado
@app.route('/usuario')
def usuario():
    if 'usuario' not in session:
        return redirect(url_for('index'))

    nome_usuario = session.get('nome_usuario', None)

    return render_template('usuario.html', nome_usuario=nome_usuario)

# Página de cadastro
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    erro = None
    sucesso = None

    if request.method == 'POST':
        nome = request.form['nome'].strip()
        email = request.form['email'].strip().lower()
        senha = request.form['senha'].strip()
        cpf = request.form['cpf'].strip()
        telefone = request.form['telefone'].strip()
        cep = request.form['cep'].strip()
        rua = request.form['rua'].strip()
        numero = request.form['numero'].strip()
        bairro = request.form['bairro'].strip()

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
        existente = cur.fetchone()

        if existente:
            erro = "Email já cadastrado."
        else:
            cur.execute("""
                INSERT INTO usuarios (nome, email, senha, cpf, telefone, cep, rua, numero, bairro)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (nome, email, senha, cpf, telefone, cep, rua, numero, bairro))
            mysql.connection.commit()
            sucesso = "Cadastro realizado com sucesso! Faça login."

        cur.close()

    return render_template("cadastro.html", erro=erro, sucesso=sucesso)

# Área administrativa (somente admin)
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if 'usuario' not in session or session['usuario'].lower() != 'admin@shoesmix.com':
        return redirect(url_for('index'))

    sucesso = None
    if request.method == 'POST':
        nome = request.form['nome'].strip()
        preco = request.form['preco']
        estoque = request.form['estoque']
        quantidade = request.form['quantidade']
        imagem = request.form['imagem'].strip()

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO produtos (nome, preco, estoque, quantidade, imagem) VALUES (%s, %s, %s, %s, %s)",
                    (nome, preco, estoque, quantidade, imagem))
        mysql.connection.commit()
        cur.close()

        sucesso = "Produto adicionado com sucesso!"

    return render_template("admin.html", sucesso=sucesso)

# Logout
@app.route('/logout')
def logout():
    session.pop('usuario', None)
    session.pop('nome_usuario', None)  # Remover o nome do usuário também
    return redirect(url_for('index'))

# Executar o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)
