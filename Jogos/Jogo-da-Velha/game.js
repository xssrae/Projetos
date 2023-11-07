const currentPlayer = document.querySelector(".currentPlayer");

let selected;
let player = "X";
let positions = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [1,4,7],
    [2,5,8],
    [3,6,9],
    [1,5,9],
    [3,5,7]
]

function init(){
    selected = [];

    currentPlayer.innerHTML = `CURRENT PLAYER: ${player}`;

    document.querySelectorAll(".game button").forEach((item) => {
        item.innerHTML = "";
        item.addEventListener("click", novaJogada);
    });
}

init();

function novaJogada(e) /*evento como atributo*/ {
    const index = e.target.getAttribute("btn-i") /*pegando a localização de cada botão*/
    e.target.innerHTML = player; /*atribuindo o player correspondente ao botão selecionado*/
    e.target.removeEventListener("click", novaJogada);
    selected[index] = player;

    setTimeout(() => {
        verificaGanhador();
    }, [100]);

    player = player === "X" ? "O" : "X";
    currentPlayer.innerHTML = `JOGADA DA VEZ: ${player}`;
}

function verificaGanhador() {
    let playerLastMove = player === "X" ? "O" : "X";

    const itens = selected 
    .map((item, i) => [item,i]) /*rastreando itens selecionados */
    .filter((item) => item[0] === playerLastMove)/*verifica as possibilidades de acerto do array positions*/
    .map(item => item[1]); /*e atribui ao array selected para comparar*/

    for (pos of positions) {
        if (pos.every((item) => itens.includes(item))) {
            alert("O JOGADOR '" + playerLastMove + " GANHOU!");
            init();
            return;
        } else if (selected.filter((item) => item).length === 9) {
            alert("DEU EMPATE!");
            init();
            return;
        }
    }
}