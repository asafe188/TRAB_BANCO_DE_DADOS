<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <title>Cadastro - ShoesMix</title>
  <link rel="stylesheet" href="{{ url_for('static', filename='styles/style.css') }}">
  <link href="https://fonts.googleapis.com/css2?family=Aleo&family=Amiri&display=swap" rel="stylesheet">
</head>
<body class="tela-cadastro">
  <div class="login-container">
    <div class="lado-esquerdo">
      <img src="{{ url_for('static', filename='logo-grande.png') }}" alt="ShoesMix" class="logo-grande">
    </div>

    <div class="lado-direito">
      <h1>Cadastro</h1>
      <h2 id="subtitulo">Dados Pessoais</h2>
      <form id="formCadastro" method="POST">
        <div class="etapa" id="etapa1">
          <div class="form-group">
            <label for="nome">Nome Completo</label>
            <input type="text" id="nome" name="nome" required>
          </div>
          <div class="duplo">
            <div class="form-group">
              <label for="email">E-mail</label>
              <input type="email" id="email" name="email" required>
            </div>
            <div class="form-group campo-senha">
              <label for="senha">Senha</label>
              <input type="password" id="senha" name="senha" required>
              <img src="{{ url_for('static', filename='olho-cadastro.png') }}" alt="Mostrar senha" class="icone-olho-cadastro" id="iconeOlhoCadastro">
            </div>
          </div>
          <div class="form-group">
            <label for="cpf">CPF</label>
            <input type="text" id="cpf" name="cpf" placeholder="000.000.000-00" required>
          </div>
          <div class="form-group">
            <label for="telefone">Telefone</label>
            <input type="text" id="telefone" name="telefone" placeholder="(99) 99999-9999" required>
          </div>
          <div class="group-button">
            <button type="button" onclick="proximaEtapa()">PRÓXIMO</button>
          </div>
        </div>

        <div class="etapa" id="etapa2" style="display:none;">
          <div class="form-group">
            <label for="bairro">Bairro</label>
            <input type="text" id="bairro" name="bairro" required>
          </div>
          <div class="duplo">
            <div class="form-group">
              <label for="rua">Rua</label>
              <input type="text" id="rua" name="rua" required>
            </div>
            <div class="form-group">
              <label for="numero">Nº</label>
              <input type="text" id="numero" name="numero" required>
            </div>
          </div>
          <div class="form-group">
            <label for="complemento">Complemento</label>
            <input type="text" id="complemento" name="complemento">
          </div>
          <div class="triplo">
            <div class="form-group">
              <label for="uf">UF</label>
              <select id="uf" name="uf" required>
                <option value="">Selecione</option>
                <option value="AC">AC</option>
                <option value="AL">AL</option>
                <option value="AM">AM</option>
                <option value="BA">BA</option>
                <!-- outros estados -->
              </select>
            </div>
            <div class="form-group">
              <label for="cidade">Cidade</label>
              <input type="text" id="cidade" name="cidade" required>
            </div>
            <div class="form-group">
              <label for="cep">CEP</label>
              <input type="text" id="cep" name="cep" placeholder="00000-000" required>
            </div>
          </div>
          <div class="group-button">
            <button type="submit">CONFIRMAR</button>
          </div>
        </div>
      </form>
    </div>
  </div>

  <script>
    function proximaEtapa() {
      document.getElementById("etapa1").style.display = "none";
      document.getElementById("etapa2").style.display = "block";
      document.getElementById("subtitulo").textContent = "Endereço";
    }

    const senhaInputCadastro = document.getElementById('senha');
    const iconeOlhoCadastro = document.getElementById('iconeOlhoCadastro');

    iconeOlhoCadastro.addEventListener('click', () => {
      const tipo = senhaInputCadastro.type === 'password' ? 'text' : 'password';
      senhaInputCadastro.type = tipo;
      iconeOlhoCadastro.src = tipo === 'text'
        ? "{{ url_for('static', filename='olho-cadastro-fechado.png') }}"
        : "{{ url_for('static', filename='olho-cadastro.png') }}";
    });
  </script>
</body>
</html>
