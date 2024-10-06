$(document).ready(function(){
    $('.datepicker').datepicker({
        format: 'dd/mm/yyyy',  // Formato de fecha para países de habla hispana
        todayHighlight: true,
        autoclose: true,
        language: 'es',  // Establecer el idioma en español
        startDate: new Date()  // Solo permite seleccionar fechas a partir de hoy
    });
});