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
