<script>
    function toggleMenu(event) {
      event.stopPropagation();
      document.getElementById("menuConta").classList.toggle("ativo");
    }
    window.addEventListener("click", function(e) {
      const menu = document.getElementById("menuConta");
      const toggle = document.querySelector(".dropdown-toggle");
      if (!toggle.contains(e.target)) {
        menu.classList.remove("ativo");
      }
    });

    let tamanhoSelecionado = null;

    function selecionarTamanho(btn) {
      document.querySelectorAll('.tamanhos button').forEach(b => b.classList.remove('selected'));
      btn.classList.add('selected');
      tamanhoSelecionado = btn.textContent;
    }

    function alterarQuantidade(delta) {
      const input = document.getElementById('qtd');
      let val = parseInt(input.value);
      if (isNaN(val)) val = 1;
      val = Math.max(1, val + delta);
      input.value = val;
    }

    function validarSelecao() {
      if (!tamanhoSelecionado) {
        alert("Selecione um tamanho!");
        return false;
      }
      const qtd = document.getElementById('qtd').value;
      // Preenche campos do carrinho
      document.getElementById('tamanhoSelecionadoInput').value = tamanhoSelecionado;
      document.getElementById('quantidadeSelecionadaInput').value = qtd;
      // Preenche campos do checkout
      document.getElementById('tamanhoSelecionadoInput2').value = tamanhoSelecionado;
      document.getElementById('quantidadeSelecionadaInput2').value = qtd;
      return true;
    }
  </script>
