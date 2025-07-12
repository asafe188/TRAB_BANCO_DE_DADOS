<script>
    // Ao clicar no botão de configurações, alternar a exibição do painel
    document.getElementById('config-button').addEventListener('click', function(event) {
      event.stopPropagation();
      const menuConfig = document.getElementById("menu-config");
      menuConfig.classList.toggle('ativo'); // Alterna a visibilidade do painel
    });

    // Fechar o painel se clicar fora dele
    window.addEventListener('click', function(e) {
      const menuConfig = document.getElementById("menu-config");
      const configButton = document.getElementById("config-button");
      if (!menuConfig.contains(e.target) && !configButton.contains(e.target)) {
        menuConfig.classList.remove('ativo');
      }
    });
  </script>
