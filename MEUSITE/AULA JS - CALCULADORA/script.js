
const campo1 = document.querySelector("#campo1");
const campo2 = document.querySelector("#campo2");
const operacao = document.querySelector("#operacao");
const resultado = document.querySelector("#resultado");

operacao.addEventListener("change",calcular);
campo1.addEventListener("keyup",calcular);
campo2.addEventListener("keyup",calcular);


function calcular() {
    if(campo1.value!="" && campo2.value !=""){ 
    const valor1 = Number(campo1.value);
    const valor2 = Number(campo2.value);
    const tipoOperacao = operacao.value;

    if (tipoOperacao == "somar") {
        resultado.innerHTML = valor1 + valor2;
    } else if (tipoOperacao == "subtrair") {
        resultado.innerHTML = valor1 - valor2;
    } else if (tipoOperacao == "multiplicar") {
        resultado.innerHTML = valor1 * valor2;
    } else if (tipoOperacao == "dividir") {
        resultado.innerHTML = valor1 / valor2;
    }
}}
