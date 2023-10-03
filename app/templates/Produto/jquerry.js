$(document).ready(function() {
    // Lidar com o envio do formulário
    $('#produto-form').submit(function(event) {
        event.preventDefault(); // Impede o envio padrão do formulário

        // Obter os valores do formulário
        var nome = $('#nome').val();
        var preco = $('#preco').val();
        var categoria = $('#categoria').val();
        var condicao = $('#condicao').val();
        var descricao = $('#descricao').val();
        var dimensoes = $('#dimensoes').val();
        var foto = $('#foto')[0].files[0];
        // Adicione campos adicionais do produto conforme necessário

        // Criar um objeto FormData para enviar dados binários (a imagem do produto)
        var formData = new FormData();
        formData.append('nome', nome);
        formData.append('preco', preco);
        formData.append('categoria', categoria);
        formData.append('condicao', condicao);
        formData.append('descricao', descricao);
        formData.append('dimensoes', dimensoes);
        formData.append('foto', foto);
        // Adicione campos adicionais do produto conforme necessário

        // Realizar uma solicitação POST para a rota do servidor Flask
        $.ajax({
            type: 'POST',
            url: '/produtos', // Certifique-se de definir a rota correta no seu Flask
            data: formData,
            contentType: false, // Importante: desabilitar o cabeçalho Content-Type
            processData: false, // Importante: não processar os dados
            success: function(response) {
                // Lógica a ser executada após o sucesso da criação do produto
                console.log(response); // Você pode exibir uma mensagem de sucesso ou redirecionar o usuário
            },
            error: function(error) {
                // Lógica para lidar com erros
                console.error(error);
            }
        });
    });
});