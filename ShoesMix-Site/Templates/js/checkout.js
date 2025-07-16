<script>  
    const radios = document.querySelectorAll('input[name="pagamento"]');  
    const btn = document.getElementById('btnContinuar');  
  
    radios.forEach(radio => {  
      radio.addEventListener('change', () => {  
        btn.classList.add('ativo');  
        btn.style.cursor = 'pointer';  
        btn.style.opacity = '1';  
        btn.onclick = function() {  
          alert('Pedido realizado com sucesso!');  
        };  
      });  
    });  
  </script>
