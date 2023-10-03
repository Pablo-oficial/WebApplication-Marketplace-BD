<><script src="../jquery.js"></script><script>
    $(document).ready(function() {$('#criar-usuario-form').submit(function (event) {
        event.preventDefault(); // Evitar o comportamento padrão de envio do formulário


        // Coletar os dados do formulário
        var data = {
            nome: $('#nome').val(),
            email: $('#email').val(),
            senha: $('#senha').val(),
            conta_bancaria: $('#conta_bancaria').val(),
            endereco: $('#endereco').val(),
            telefone: $('#telefone').val()
        };

        // Enviar os dados para o Flask
        $.ajax({
            url: '/usuarios',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(data),
            success: function (response) {
                alert(response.mensagem); // Exibir mensagem de sucesso
            },
            error: function (error) {
                alert('Erro ao criar usuário: ' + error.responseJSON.erro); // Exibir mensagem de erro
            }
        });
    })};
    {"}"});
</script></>