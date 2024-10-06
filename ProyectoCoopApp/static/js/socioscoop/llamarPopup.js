      $(document).ready(function(){
          // Asegurarse de que las variables están definidas antes de intentar abrir el modal
          var nombre = "{{ nombre }}";
          var rut = "{{ rut }}";
          var valor_cuota = "{{ valor_cuota }}";
          
          if (nombre && rut && valor_cuota) {
              $('#resultadoModal').modal('show');
          }
      });