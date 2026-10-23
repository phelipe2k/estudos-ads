let botao = document.querySelector("#botao");

let estaQuebrado = false;
let contador = 0;


botao.style.backgroundColor = "red";
botao.style.color = "white";
botao.style.padding = "10px";
botao.style.borderRadius = "5px";
botao.style.fontWeight = "bold";

botao.addEventListener("mouseover",e => {
    if(!estaQuebrado){
    botao.style.backgroundColor = "green";
}
});

botao.addEventListener("mouseout",e => {
    if(!estaQuebrado){
        botao.style.backgroundColor = "blue";
    }
        });

    botao.addEventListener("click",e => {
        if(!estaQuebrado){
            botao.style.backgroundColor = "red";
            botao.innerHTML = "Quebrei";
            estaQuebrado = true;
        }
    });

    botao.addEventListener("click", e => {
       contador++; // Incrementa    o contador a cada clique
       if (contador >= 5) { // Verifica se o contador atingiu 5
           botao.style.backgroundColor = "gray"; // Muda a cor do botão para cinza
              botao.innerHTML = "Desativado"; // Altera o texto do botão
              estaQuebrado = true; // Define que o botão está quebrado
       }    
    }); 