$(document).ready(function() {
    // Lidar com o envio do formulário
    $('#carrinho-form').submit(function(event) {
        event.preventDefault(); // Impede o envio padrão do formulário

        // Obter os valores do formulário
        var quantidade = $('#quantidade').val();
        var preco = $('#preco').val();
        var compradorId = $('#comprador_id').val();

        // Criar um objeto de dados a serem enviados ao servidor
        var data = {
            quantidade: quantidade,
            preco: preco,
            comprador_id: compradorId
        };

        // Realizar uma solicitação POST para a rota do servidor Flask
        $.ajax({
            type: 'POST',
            url: '/carrinhos',
            contentType: 'application/json',
            data: JSON.stringify(data),
            success: function(response) {
                // Lógica a ser executada após o sucesso da criação do carrinho
                console.log(response); // Você pode exibir uma mensagem de sucesso ou redirecionar o usuário
            },
            error: function(error) {
                // Lógica para lidar com erros
                console.error(error);
            }
        });
    });
});