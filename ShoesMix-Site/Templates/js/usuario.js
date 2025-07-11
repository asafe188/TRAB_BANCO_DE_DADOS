<script>
    function toggleMenu(event) {
      event.stopPropagation();
      const menu = document.getElementById("menuConta");
      menu.classList.toggle("ativo");
    }
    window.addEventListener("click", function (e) {
      const menu = document.getElementById("menuConta");
      const toggle = document.querySelector(".dropdown-toggle");
      if (!toggle.contains(e.target)) {
        menu.classList.remove("ativo");
      }
    });
  </script>

