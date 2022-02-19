$(document).ready(function() {
    $("#password_reset").submit(function(e) {
        e.preventDefault();
        var form = $(this);
        $.ajax({
            type: "POST",
            url: "/password-reset/",
            data: form.serialize(),
            success: function(data) {
                if (data) {
                    Swal.fire({
                        title: 'Erro!',
                        html: data,
                        type: 'error',
                        showCloseButton: true,
                    });
                } else {
                    form[0].reset();
                    $("#modalSenha").modal('hide');
                    Swal.fire({
                        title: 'Sucesso!',
                        text: 'Se você está cadastrado em nosso site, nós enviamos um email com as intruções para alterar sua senha. Verifique sua caixa de entrada!',
                        type: 'success',
                        showCloseButton: true
                    });
                }
            }
        });
    });
});