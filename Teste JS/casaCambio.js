/*função principal*/
function criarMoeda(nome, sigla, valor) {
    return{nome,sigla,valor};
}

let moedas = {
    usd: criarMoeda('Dólar','USD', 5.56810),
    eur: criarMoeda('Euro', 'EUR', 6.63457),
    gbp: criarMoeda('Libra', 'GBP', 7.6738),
    jpy: criarMoeda('Iene', 'JPY', 0.05093),
    ars: criarMoeda('Peso', 'ARS', 0.06033),
}

/* porcentagem de taxa de aplicação */
let casa = {  /* this.taxa = casa e taxa */
    taxa: 0.10
}


/* função para realizar a compra - conversão */
casa.proporCompra = function (moeda, quantidade) {
    let valorAjustado = moeda.valor - (moeda.valor*this.taxa)
    return valorAjustado * quantidade;
}

/* função para realizar a venda - conversão inversa (retirando o valor % da taxa) */
casa.proporVenda = function (moeda, quantidade) {
    let valorAjustado = moeda.valor * (1+this.taxa);
    return valorAjustado * quantidade;
}

/* função para realizar troca */
casa.proporTroca = function (moeda1, qtd1, moeda2, qtd2) {
    let valorCompra = this.proporCompra(moeda1,qtd1)
        valorVenda = this.proporVenda(moeda2, qtd2)
    return valorVenda - valorCompra
}

/* tabela para entrada de dados e visualização*/
casa.criarTabela = function (moeda){
    let tabela = [];

    for (let moeda in moedas) {
        tabela.push( {
            'Moeda': moedas[moeda].nome + '(' + moedas[moeda].sigla + ')',
            'Valor de veda': this.proporVenda(moedas[moeda],1),
            'Valor de compra': this.proporCompra(moedas[moeda],1),
        } );
    }
/* tabela principal */
    return tabela;

}

console.table(casa.criarTabela(moedas));