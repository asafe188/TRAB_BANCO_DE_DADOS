<script>
    function atualizarTotal() {
      const checks = document.querySelectorAll(".checkbox-item:checked");
      let total = 0;
      let resumo = "";

      checks.forEach(cb => {
        const preco = parseFloat(cb.dataset.preco);
        const nome = cb.dataset.nome;
        total += preco;
        resumo += `<p>${nome} - R$ ${preco.toFixed(2)}</p>`;
      });

      document.getElementById("total").textContent = total.toFixed(2);
      document.getElementById("listaItensResumo").innerHTML = resumo;
    }

    function marcarTodos() {
      const todos = document.querySelectorAll('.checkbox-item');
      const checkAll = document.getElementById('checkAll');
      todos.forEach(cb => cb.checked = checkAll.checked);
      atualizarTotal();
    }

    document.getElementById("form-comprar").addEventListener("submit", function(event) {
      const checks = document.querySelectorAll(".checkbox-item:checked");
      if (checks.length === 0) {
        alert("Selecione pelo menos um produto para comprar.");
        event.preventDefault();
        return;
      }
      const ids = Array.from(checks).map(chk => chk.value);
      document.getElementById("itensSelecionadosInput").value = ids.join(",");
    });
  </script>
