
document.addEventListener("DOMContentLoaded", function() {
    var actualizarUrl = "{% url 'actualizar_cantidad' %}";
    var eliminarUrl = "{% url 'eliminar_del_carrito' %}";
    var csrfToken = "{{ csrf_token }}";

    document.querySelectorAll('.btn-actualizar').forEach(function(button) {
        button.addEventListener('click', function() {
            var elementoId = this.getAttribute('data-id');
            var action = this.getAttribute('data-action');
            fetch(actualizarUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken
                },
                body: JSON.stringify({
                    'elemento_id': elementoId,
                    'action': action
                })
            })
            .then(response => response.json())
            .then(data => {
                document.querySelector('#elemento-' + elementoId + ' .cantidad').textContent = data.cantidad;
                document.querySelector('#elemento-' + elementoId + ' .precio_total').textContent = '$' + data.precio_total;
                document.querySelector('#carrito-total').textContent = data.total;
            })
            .catch(error => console.error('Error:', error));
        });
    });

    document.querySelectorAll('.btn-eliminar').forEach(function(button) {
        button.addEventListener('click', function() {
            var elementoId = this.getAttribute('data-id');
            fetch(eliminarUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken
                },
                body: JSON.stringify({
                    'elemento_id': elementoId
                })
            })
            .then(response => response.json())
            .then(data => {
                document.querySelector('#elemento-' + elementoId).remove();
                document.querySelector('#carrito-total').textContent = data.total;
            })
            .catch(error => console.error('Error:', error));
        });
    });
});

