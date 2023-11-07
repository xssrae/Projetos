let fii_user = [];
let fii_table = [];



async function carregarDadosUser(url){
    await fetch(url)
            .then(resp => resp.json())
            .then(json => fii_user = json);
    carregarDadosFundos();
}

async function carregarDadosFundos(){
    
    for (let fii of fii_user){
        let json = await fetch(`https://api-simple-flask.herokuapp.com/api/${fii.nome}`)
                        .then(resp => resp.json());
        fii_table.push(json);
    }
    exibirTabela();

}

carregarDadosUser("json/fii.json");

function exibirTabela(){ 
    let dadosTabela = ""

    let limite_percentual = 0.9; // limite de corte - fundos abaixo disso não valem apena
    let total_cotas = 0; // percorrer com for e somar todas as cotas
    let total_investido = 0; //soma da carteira local todos os gastos para ter os fundos
    let total_proventos = 0; // exemplo do calculo fundo[n] += (qtdeCotas)*(proventoMes) 
    let provento = 0; // PAGAMENTO DO FUNDO POR COTA
    let data_base = 0; // extrair do JSON
    let data_pagamento = 0; // extrair do JSON
    let percentual = 0; // FUNÇÃO
    let preco_medio = 0;


    for (let fii of fii_user) {
        let dados_fii = fii_table.find((item) => 
                        item.fundo.indexOf(fii.nome.toUpperCase()) >= 0);
        
        if (dados_fii.proximoRendimento.rendimento != "-"){
            provento = dados_fii.proximoRendimento.rendimento;
            data_base = dados_fii.proximoRendimento.dataBase;
            data_pagamento = dados_fii.proximoRendimento.dataPag;
        }else{
            provento = dados_fii.ultimoRendimento.rendimento;
            data_pagamento = dados_fii.ultimoRendimento.dataPag;
        }

        total_proventos += provento * fii.qtde;
        total_investido += fii.totalgasto;
        total_cotas += fii.qtde;
        percentual = (provento*100 / dados_fii.valorAtual).toFixed(2);
        preco_medio = gasto_total/cotas_total;

        let classe = (percentual <= limite_percentual)?"negativo":"positivo"
        dadosTabela += `<tr class ='${classe}'>
        <td>${fii.nome}</td>
        <td>${dados_fii.setor}</td>
        <td>${data_base}</td>
        <td>${data_pagamento}</td>
        <td>${provento}</td>
        <td>${dados_fii.valorAtual}</td>
        <td>${total_cotas}</td>
        <td>${total_investido}</td>
        <td>-</td>
        <td>${percentual}</td>
        <td>${dados_fii.dividendYield}</td>
        <td>${dados_fii.rendimentoMedio24M}</td>
        <td>${dados_fii.pvp}</td>
        <td>${dados_fii.valorPatrimonioPCota}</td>
        </tr>`
    }
    document.querySelector("table").innerHTML += dadosTabela;

    //ULTIMA LINHA: TOTAL
    document.querySelector("table")
            .innerHTML += `<tr class='fundo_total'>
            <td colspan='4'>Total Geral</td>
            <td>-</td>
            <td>${total_cotas}</td>
            <td>R$ ${total_investido.toFixed(2)} </td>
            <td>-</td><td>-</td><td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td></tr>`;
    document.querySelector("#loading").style.display = "none";
}



