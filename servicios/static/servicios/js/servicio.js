$(function() {
	// ocultar div errores
  	$("#div-errores").hide();
  	// agregar eventos
  	$("input[name=g]").click(validar);
  	$("input[name=b]").click(confirmar);
  	$("#id_fondo").change(updateSecciones);
  	$("#id_seccion").change(updateSeries);
});

function validar(){
	errores = 0;
	$('#df li').hide();
	if (!$("#id_fondo").val() || $("#id_fondo").val() == '-') {
		errores++;
		$('#ef').show();
	}
	if (!$("#id_expediente").val()) {
		errores++;
		$('#ee').show();
	}
	if (!$("#id_destinatario").val()){
		errores++;
		$('#ed').show();
	}
	if (!$("#id_tipo").val()){
		errores++;
		$('#et').show();
	}
	// errores
	if (errores) {
		$("#div-errores").show();
	}
	// si hay errores no se puede guardar
	return (errores == 0);
}
function confirmar(){
	var r = confirm("¿Está seguro que quiere eliminar el servicio?");
    return r;
}
function updateSecciones(){
	$("#id_seccion").val("-");
	$("#id_serie").val("-");
	$("#id_seccion > option").hide().filter(function(index){
		return $(this).attr('data-padre') == $('#id_fondo').val();
	}).show();
}
function updateSeries(){
	$("#id_serie").val("-");
	$("#id_serie > option").hide().filter(function(index){
		return $(this).attr('data-padre') == $('#id_seccion').val();
	}).show();
}	