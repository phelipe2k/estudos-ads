
/* exemplo de objeto em JavaScript */
let pessoa= {
    nome: "João",
    idade: 30,
    cidade: "Rio de Janeiro",
    estado: "Rio de Janeiro"
};


/* exemplo de array em JavaScript */
let listaDesejos = ["Viajar", "Aprender programação", "Comprar um carro", "Ter uma casa própria"];


/* exemplo de loop em JavaScript */
for (let i = 0; i < listaDesejos.length; i++) {
    console.log(listaDesejos[i]);
}
console.log(listaDesejos[2]); 

let paragrafo = document.querySelector("#paragrafo");

/* exemplo de evento em JavaScript */
paragrafo.addEventListener("mouseout", trocaTexto);
paragrafo.addEventListener("mouseover", mudaCor);

function mudaCor() {
    paragrafo.style.backgroundColor = "yellow";
    paragrafo.style.fontWeight = "bold";
    paragrafo.style.padding = "10px";
    paragrafo.style.color = "blue";
    paragrafo.style.fontSize = "20px";
}


/* exemplo de função que altera o texto do parágrafo e aplica estilos CSS */
function trocaTexto() {
    paragrafo.textContent = "O texto foi alterado!";
    paragrafo.style.color = "red";
    paragrafo.style.fontSize = "24px";}
    

primeiroNome = prompt("Digite seu primeiro nome");
sobrenome = prompt("Digite seu sobrenome");
idade = prompt("Digite sua idade");
cidade = prompt("Digite sua cidade");
estado = prompt("Digite seu estado");

console.log("Nome: " + primeiroNome + " " + sobrenome);
console.log("Idade: " + idade);
console.log("Cidade: " + cidade);
console.log("Estado: " + estado);

let mensagem = "Olá, meu nome é " + primeiroNome + " " + sobrenome + ", tenho " + idade + " anos e moro em " + cidade + ", " + estado + ".";
console.log(mensagem);

if (idade >= 18) {
    console.log(" Vocé é maior de idade.");
}

else{
    console.log(" Vocé é menor de idade.");}

/*
let cidade = 'Capitão Andrade';

console.log("Nome: " + nome);
console.log("Idade: " + idade);
console.log("Cidade: " + cidade);

if (idade >= 18) {
    console.log("Você é maior de idade.");
}

else{
    console.log(" Vocé é menor de idade.");}

let mensagem = "Olá, meu nome é " + nome + ", tenho " + idade + " anos e moro em " + cidade + ".";
console.log(mensagem);  
*/