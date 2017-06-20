$(function() {
    // ocultar div errores
    $("#div-errores").hide();
    // agregar eventos
    $("input[name=g]").click(validar);
    $("input[name=b]").click(confirmar);
});

function validar(){
    errores = 0;
    $('#df li').hide();
    if (!$("#dependencia").val()) {
        errores++;
        $('#ed').show();
    }
    if (!$("#interesado").val()) {
        errores++;
        $('#ei').show();
    }
    if (!$("#tipo").val() || $("#tipo").val() == '-') {
        errores++;
        $('#et').show();
    }
    if (!$("#fechaSolicitud").val()){
        errores++;
        $('#ef').show();
    }
    // errores
    if (errores) {
        $("#div-errores").show();
    }
    // si hay errores no se puede guardar
    return (errores == 0);
}
function confirmar(){
    var r = confirm("¿Está seguro que quiere eliminar la solicitud?");
    return r;
}
