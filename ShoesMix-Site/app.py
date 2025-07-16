from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.secret_key = 'minha_chave_secreta'

# Pasta de uploads
UPLOAD_FOLDER = os.path.join('static', 'uploads')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Configuração banco
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'shoesmixweb'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

mysql = MySQL(app)

@app.route('/styles/<path:filename>')
def styles(filename):
    return send_from_directory(os.path.join(app.root_path, 'templates', 'styles'), filename)

@app.route('/uploads/<path:filename>')
def uploads(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM produtos")
    produtos = cur.fetchall()
    cur.close()
    if 'usuario' in session:
        if session['usuario'].lower() == 'admin@shoesmix.com':
            modo = 'admin'
        else:
            modo = 'logado'
    else:
        modo = 'visitante'
    return render_template('index.html', produtos=produtos, modo=modo)

@app.route('/login', methods=['GET', 'POST'])
def login():
    erro = None
    if request.method == 'POST':
        email = request.form['email'].strip().lower()
        senha = request.form['senha'].strip()
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM usuarios WHERE email=%s AND senha=%s", (email, senha))
        usuario = cur.fetchone()
        cur.close()
        if usuario:
            session['usuario'] = email
            session['nome_usuario'] = usuario[0]
            if email == 'admin@shoesmix.com' and senha == 'admin123' and usuario[1].lower() == 'admin':
                return redirect(url_for('admin'))
            return redirect(url_for('usuario'))
        else:
            erro = 'Email ou senha inválidos.'
    return render_template('login.html', erro=erro)

@app.route('/usuario')
def usuario():
    if 'usuario' not in session:
        return redirect(url_for('index'))
    nome_usuario = session.get('nome_usuario')
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM produtos")
    produtos = cur.fetchall()
    cur.close()
    return render_template('usuario.html', nome_usuario=nome_usuario, produtos=produtos)

@app.route('/perfil')
def perfil():
    if 'usuario' not in session:
        return redirect(url_for('index'))
    email = session['usuario']
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT nome, email, cpf, telefone, bairro, rua, numero, cidade, uf, complemento
        FROM usuarios WHERE email=%s
    """, (email,))
    dados = cur.fetchone()
    cur.close()
    if not dados:
        return redirect(url_for('index'))
    dados_usuario = {
        'nome': dados[0],
        'email': dados[1],
        'cpf': dados[2],
        'telefone': dados[3],
        'endereco': {
            'bairro': dados[4] or 'Não informado',
            'rua': dados[5] or 'Não informado',
            'numero': dados[6] or 'Não informado',
            'cidade': dados[7] or 'Não informado',
            'uf': dados[8] or 'Não informado',
            'complemento': dados[9] or 'Não informado'
        }
    }
    return render_template('perfil.html', usuario=dados_usuario)

@app.route('/editar_perfil', methods=['GET', 'POST'])
def editar_perfil():
    if 'usuario' not in session:
        return redirect(url_for('index'))
    email = session['usuario']
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        nome = request.form['nome'].strip()
        telefone = request.form['telefone'].strip()
        cpf = request.form['cpf'].strip()
        bairro = request.form['bairro'].strip()
        rua = request.form['rua'].strip()
        numero = request.form['numero'].strip()
        cidade = request.form['cidade'].strip()
        uf = request.form['uf'].strip()
        complemento = request.form['complemento'].strip()
        cur.execute("""
            UPDATE usuarios
            SET nome=%s, telefone=%s, cpf=%s, bairro=%s, rua=%s, numero=%s, cidade=%s, uf=%s, complemento=%s
            WHERE email=%s
        """, (nome, telefone, cpf, bairro, rua, numero, cidade, uf, complemento, email))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('perfil'))
    cur.execute("""
        SELECT nome, email, cpf, telefone, bairro, rua, numero, cidade, uf, complemento
        FROM usuarios WHERE email=%s
    """, (email,))
    dados = cur.fetchone()
    cur.close()
    if not dados:
        return redirect(url_for('index'))
    dados_usuario = {
        'nome': dados[0],
        'email': dados[1],
        'cpf': dados[2],
        'telefone': dados[3],
        'bairro': dados[4],
        'rua': dados[5],
        'numero': dados[6],
        'cidade': dados[7],
        'uf': dados[8],
        'complemento': dados[9]
    }
    return render_template("editar_perfil.html", usuario=dados_usuario)

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
        uf = request.form['uf'].strip()
        cidade = request.form['cidade'].strip()
        complemento = request.form['complemento'].strip()
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM usuarios WHERE email=%s", (email,))
        existente = cur.fetchone()
        if existente:
            erro = "Email já cadastrado."
        else:
            cur.execute("""
                INSERT INTO usuarios (nome, email, senha, cpf, telefone, cep, rua, numero, bairro, uf, cidade, complemento)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (nome, email, senha, cpf, telefone, cep, rua, numero, bairro, uf, cidade, complemento))
            mysql.connection.commit()
            sucesso = "Cadastro realizado com sucesso! Faça login."
        cur.close()
    return render_template("cadastro.html", erro=erro, sucesso=sucesso)

@app.route('/meus_pedidos')
def meus_pedidos():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    aba = request.args.get('aba', 'devolucao')
    return render_template('meus_pedidos.html', aba=aba)

@app.route('/admin')
def admin():
    if 'usuario' not in session or session['usuario'].lower() != 'admin@shoesmix.com':
        return redirect(url_for('index'))
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM produtos")
    produtos = cur.fetchall()
    cur.close()
    return render_template("admin.html", produtos=produtos)

@app.route('/estoque')
def estoque():
    if 'usuario' not in session or session['usuario'].lower() != 'admin@shoesmix.com':
        return redirect(url_for('index'))
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM produtos")
    produtos = cur.fetchall()
    cur.close()
    return render_template("estoque.html", produtos=produtos)

@app.route('/produto/<int:id>')
def produto(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM produtos WHERE id=%s", (id,))
    produto = cur.fetchone()
    cur.close()
    if not produto:
        return redirect(url_for('index'))
    return render_template("produto.html", produto=produto)

@app.route('/adicionar_carrinho/<int:produto_id>', methods=['POST'])
def adicionar_carrinho(produto_id):
    if 'usuario' not in session:
        return redirect(url_for('login'))
    tamanho = request.form.get('tamanho')
    quantidade = int(request.form.get('quantidade', 1))
    cur = mysql.connection.cursor()
    cur.execute("""
        INSERT INTO carrinho (usuario_email, produto_id, quantidade, tamanho)
        VALUES (%s, %s, %s, %s)
    """, (session['usuario'], produto_id, quantidade, tamanho))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('carrinho'))

@app.route('/remover_item/<int:item_id>', methods=['POST'])
def remover_item(item_id):
    if 'usuario' not in session:
        return redirect(url_for('login'))
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM carrinho WHERE id=%s AND usuario_email=%s", (item_id, session['usuario']))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('carrinho'))

@app.route('/carrinho')
def carrinho():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT c.id, p.nome, p.descricao, p.preco, p.imagem, c.quantidade, c.tamanho
        FROM carrinho c
        JOIN produtos p ON c.produto_id = p.id
        WHERE c.usuario_email = %s
    """, (session['usuario'],))
    itens = cur.fetchall()
    cur.close()
    return render_template('carrinho.html', itens=itens)

@app.route('/cadastro_produto', methods=['GET', 'POST'])
def cadastro_produto():
    if 'usuario' not in session or session['usuario'].lower() != 'admin@shoesmix.com':
        return redirect(url_for('index'))
    sucesso = None
    if request.method == 'POST':
        nome = request.form['nome_produto'].strip()
        descricao = request.form['descricao'].strip()
        preco = request.form['preco']
        quantidade = request.form['quantidade']
        tamanho = request.form.get('tamanho', '').strip()
        promocao = request.form.get('promocao', '').strip()
        categoria = request.form['categoria']
        imagem_file = request.files['imagem']
        if imagem_file and imagem_file.filename != '':
            filename = secure_filename(imagem_file.filename)
            imagem_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            imagem_file.save(imagem_path)
            imagem = f'uploads/{filename}'
        else:
            imagem = ''
        cur = mysql.connection.cursor()
        cur.execute("""
            INSERT INTO produtos (nome, descricao, preco, quantidade, tamanho, promocao, categoria, imagem)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (nome, descricao, preco, quantidade, tamanho, promocao, categoria, imagem))
        mysql.connection.commit()
        cur.close()
        sucesso = "Produto cadastrado com sucesso!"
    return render_template("cadastro_produto.html", sucesso=sucesso)
# Verificação de pedidos pelo admin
@app.route('/verificar_pedidos')
def verificar_pedidos():
    if 'usuario' not in session or session['usuario'].lower() != 'admin@shoesmix.com':
        return redirect(url_for('index'))
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT id, cliente_nome, produto_nome, tamanho, data_pedido
        FROM pedidos
        ORDER BY data_pedido DESC
    """)
    pedidos = cur.fetchall()
    cur.close()
    return render_template('verificar_pedidos.html', pedidos=pedidos)

# Detalhe de um pedido
@app.route('/detalhe_pedido/<int:pedido_id>')
def detalhe_pedido(pedido_id):
    if 'usuario' not in session or session['usuario'].lower() != 'admin@shoesmix.com':
        return redirect(url_for('index'))
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT id, email, cliente_nome, produto_nome, tamanho, quantidade, data_pedido,
               bairro, rua, numero, cidade, uf, pagamento, status
        FROM pedidos
        WHERE id = %s
    """, (pedido_id,))
    pedido = cur.fetchone()
    cur.close()
    if not pedido:
        return redirect(url_for('verificar_pedidos'))
    return render_template('detalhe_pedidos.html', pedido=pedido)

@app.route('/checkout', methods=['POST'])
def checkout():
    if 'usuario' not in session:
        return redirect(url_for('login'))

    # Recebe os itens selecionados
    produto_id = request.form.get('produto_id')
    quantidade = int(request.form.get('quantidade', 1))
    tamanho = request.form.get('tamanho')

    cur = mysql.connection.cursor()
    # Pega o produto
    cur.execute("SELECT id, nome, preco, imagem FROM produtos WHERE id=%s", (produto_id,))
    produto = cur.fetchone()

    # Pega dados do usuário
    email = session['usuario']
    cur.execute("""
        SELECT bairro, rua, numero, cidade, uf
        FROM usuarios WHERE email=%s
    """, (email,))
    endereco = cur.fetchone()
    cur.close()

    if not produto or not endereco:
        return redirect(url_for('carrinho'))

    # Calcula total
    total = produto[2] * quantidade
    # Salvar no session para finalizar depois
    session['produto_id_checkout'] = produto[0]
    session['quantidade_checkout'] = quantidade
    session['tamanho_checkout'] = tamanho

    return render_template(
        "checkout.html",
        produto=produto,
        quantidade=quantidade,
        tamanho=tamanho,
        endereco=endereco,
        total=total
    )
@app.route('/pagamento_pix')
def pagamento_pix():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    return render_template('pagamento_pix.html')

@app.route('/compra_finalizada')
def compra_finalizada():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    return render_template('compra_finalizada.html')

@app.route('/finalizar_compra', methods=['POST'])
def finalizar_compra():
    if 'usuario' not in session:
        return redirect(url_for('login'))

    produto_id = session.get('produto_id_checkout')
    quantidade = session.get('quantidade_checkout')
    tamanho = session.get('tamanho_checkout')

    if not produto_id or not quantidade or not tamanho:
        return redirect(url_for('index'))

    email = session['usuario']

    cur = mysql.connection.cursor()

    # Buscar dados do usuário
    cur.execute("""
        SELECT nome, bairro, rua, numero, cidade, uf
        FROM usuarios WHERE email=%s
    """, (email,))
    usuario = cur.fetchone()
    if not usuario:
        cur.close()
        return redirect(url_for('index'))

    nome_cliente = usuario[0]
    bairro = usuario[1]
    rua = usuario[2]
    numero = usuario[3]
    cidade = usuario[4]
    uf = usuario[5]

    # Buscar dados do produto
    cur.execute("SELECT nome, preco, quantidade FROM produtos WHERE id=%s", (produto_id,))
    produto = cur.fetchone()
    if not produto:
        cur.close()
        return redirect(url_for('index'))

    nome_produto = produto[0]
    preco = produto[1]
    estoque_atual = produto[2]

    # Atualizar estoque
    novo_estoque = estoque_atual - quantidade
    if novo_estoque < 0:
        novo_estoque = 0

    cur.execute("UPDATE produtos SET quantidade=%s WHERE id=%s", (novo_estoque, produto_id))

    # Inserir pedido na tabela pedidos
    cur.execute("""
        INSERT INTO pedidos (
            email, cliente_nome, produto_nome, tamanho, quantidade, data_pedido,
            bairro, rua, numero, cidade, uf, pagamento, status
        ) VALUES (
            %s, %s, %s, %s, %s, NOW(),
            %s, %s, %s, %s, %s, %s, %s
        )
    """, (
        email, nome_cliente, nome_produto, tamanho, quantidade,
        bairro, rua, numero, cidade, uf, "PIX", "Processando"
    ))

    mysql.connection.commit()
    cur.close()

    # Limpar dados do session
    session.pop('produto_id_checkout', None)
    session.pop('quantidade_checkout', None)
    session.pop('tamanho_checkout', None)

    return "OK"

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    session.pop('nome_usuario', None)
    return redirect(url_for('index'))

@app.route('/buscar')
def buscar():
    termo = request.args.get('q', '').strip()
    cur = mysql.connection.cursor()
    # Buscar produtos cujo nome ou descrição contenham o termo
    query = """
        SELECT * FROM produtos
        WHERE nome LIKE %s OR descricao LIKE %s
    """
    like_term = f"%{termo}%"
    cur.execute(query, (like_term, like_term))
    produtos = cur.fetchall()
    cur.close()

    # Descobrir modo (admin, logado, visitante)
    if 'usuario' in session:
        if session['usuario'].lower() == 'admin@shoesmix.com':
            modo = 'admin'
        else:
            modo = 'logado'
    else:
        modo = 'visitante'

    return render_template('resultados_busca.html', produtos=produtos, termo=termo, modo=modo)

@app.route('/filtro/<categoria>')
def filtro(categoria):
    cur = mysql.connection.cursor()
    if categoria == 'promocao':
        cur.execute("SELECT * FROM produtos WHERE promocao IS NOT NULL AND promocao != ''")
    else:
        cur.execute("SELECT * FROM produtos WHERE categoria = %s", (categoria,))
    produtos = cur.fetchall()
    cur.close()

    modo = 'visitante'
    if 'usuario' in session:
        if session['usuario'].lower() == 'admin@shoesmix.com':
            return redirect(url_for('filtro_admin', categoria=categoria))
        else:
            return redirect(url_for('filtro_usuario', categoria=categoria))

    return render_template('index.html', produtos=produtos, modo=modo)

@app.route('/filtro_usuario/<categoria>')
def filtro_usuario(categoria):
    cur = mysql.connection.cursor()
    if categoria == 'promocao':
        cur.execute("SELECT * FROM produtos WHERE promocao IS NOT NULL AND promocao != ''")
    else:
        cur.execute("SELECT * FROM produtos WHERE categoria = %s", (categoria,))
    produtos = cur.fetchall()
    cur.close()

    nome_usuario = session.get('nome_usuario')
    return render_template('usuario.html', nome_usuario=nome_usuario, produtos=produtos)

@app.route('/filtro_admin/<categoria>')
def filtro_admin(categoria):
    cur = mysql.connection.cursor()
    if categoria == 'promocao':
        cur.execute("SELECT * FROM produtos WHERE promocao IS NOT NULL AND promocao != ''")
    else:
        cur.execute("SELECT * FROM produtos WHERE categoria = %s", (categoria,))
    produtos = cur.fetchall()
    cur.close()

    return render_template('admin.html', produtos=produtos)

@app.route('/checkout_carrinho', methods=['POST'])
def checkout_carrinho():
    if 'usuario' not in session:
        return redirect(url_for('login'))

    ids_str = request.form.get('itens')
    if not ids_str:
        return redirect(url_for('carrinho'))

    ids = ids_str.split(',')

    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT c.id, p.nome, p.preco, p.imagem, c.quantidade, c.tamanho
        FROM carrinho c
        JOIN produtos p ON c.produto_id = p.id
        WHERE c.id IN ({})
        AND c.usuario_email = %s
    """.format(','.join(['%s']*len(ids))), (*ids, session['usuario']))
    itens = cur.fetchall()
    cur.close()

    if not itens:
        return redirect(url_for('carrinho'))

    # Pega o endereço
    email = session['usuario']
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT bairro, rua, numero, cidade, uf
        FROM usuarios WHERE email=%s
    """, (email,))
    endereco = cur.fetchone()
    cur.close()

    total = sum(i[2] * i[4] for i in itens)

    return render_template(
        "checkout.html",
        itens=itens,
        endereco=endereco,
        total=total
    )

@app.route('/finalizar_compra_carrinho', methods=['POST'])
def finalizar_compra_carrinho():
    if 'usuario' not in session:
        return redirect(url_for('login'))

    email = session['usuario']
    ids_str = request.form.get('itens')
    if not ids_str:
        return redirect(url_for('carrinho'))

    ids = ids_str.split(',')

    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT c.id, c.produto_id, p.nome, p.preco, c.quantidade, c.tamanho
        FROM carrinho c
        JOIN produtos p ON c.produto_id = p.id
        WHERE c.id IN ({})
        AND c.usuario_email = %s
    """.format(','.join(['%s'] * len(ids))), (*ids, email))
    pedidos = cur.fetchall()

    # Buscar dados do usuário
    cur.execute("""
        SELECT nome, bairro, rua, numero, cidade, uf
        FROM usuarios WHERE email=%s
    """, (email,))
    usuario = cur.fetchone()
    if not usuario:
        cur.close()
        return redirect(url_for('index'))

    nome_cliente, bairro, rua, numero, cidade, uf = usuario

    # Inserir pedidos e atualizar estoque
    for pedido in pedidos:
        carrinho_id, produto_id, nome_produto, preco, quantidade, tamanho = pedido

        # Atualizar estoque
        cur.execute("SELECT quantidade FROM produtos WHERE id=%s", (produto_id,))
        estoque_atual = cur.fetchone()[0]
        novo_estoque = max(0, estoque_atual - quantidade)
        cur.execute("UPDATE produtos SET quantidade=%s WHERE id=%s", (novo_estoque, produto_id))

        # Inserir pedido
        cur.execute("""
            INSERT INTO pedidos (
                email, cliente_nome, produto_nome, tamanho, quantidade, data_pedido,
                bairro, rua, numero, cidade, uf, pagamento, status
            ) VALUES (
                %s, %s, %s, %s, %s, NOW(),
                %s, %s, %s, %s, %s, %s, %s
            )
        """, (
            email, nome_cliente, nome_produto, tamanho, quantidade,
            bairro, rua, numero, cidade, uf, "PIX", "Processando"
        ))

        # Remover item do carrinho
        cur.execute("DELETE FROM carrinho WHERE id=%s", (carrinho_id,))

    mysql.connection.commit()
    cur.close()

    return redirect(url_for('compra_finalizada'))


if __name__ == '__main__':
    app.run(debug=True)
