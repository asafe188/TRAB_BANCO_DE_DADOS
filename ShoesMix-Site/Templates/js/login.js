<script>
    const senhaInput = document.getElementById('senha');
    const iconeOlho = document.getElementById('iconeOlhoLogin');

    iconeOlho.addEventListener('click', () => {
      const tipo = senhaInput.type === 'password' ? 'text' : 'password';
      senhaInput.type = tipo;
      iconeOlho.src = tipo === 'text'
        ? "{{ url_for('static', filename='olho-login-fechado.png') }}"
        : "{{ url_for('static', filename='olho-login.png') }}";
    });
  </script>

