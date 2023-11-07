package Jogo;
import java.util.Scanner;

public class Tabuleiro {
    public static void main(String[] args) {
        Scanner leia = new Scanner(System.in);
        System.out.println("Jogador 1 = X");
        System.out.println("Jogador 2 = O");

        JogoDaVelha jogoDaVelha = new JogoDaVelha();

        boolean ganhou = false; //flag
        char sinal;
        int linha = 0, coluna = 0;

        while(!ganhou) {
            if (jogoDaVelha.vezJogador1()) {
                System.out.println("Vez do jogador 1. \n--> Escolha linha e coluna");
                sinal = 'X';
            } else {
                System.out.println("Vez do jogador 2. \n--> Escolha linha e coluna");
                sinal = 'O';
            }
            linha = valor("Linha", leia);  //chamando o método que verifica linhas válidas
            coluna = valor("Coluna", leia); //chamando o método que verifica colunas válidas

            jogoDaVelha.validarJogada(linha, coluna, sinal);

            jogoDaVelha.imprimirTabuleiro();

            if (jogoDaVelha.verificarGanhador('X')) {
                ganhou = true;
                System.out.println("Parabéns, jogador 1 ganhou!");
            } else if (jogoDaVelha.verificarGanhador('O')) {
                ganhou = true;
                System.out.println("Parabéns, jogador 2 ganhou!");
            } else if (jogoDaVelha.jogada > 9) {
                ganhou = true;
                System.out.println("Ninguém ganhou essa partida");
                
            }
        }
    }
    
    static int valor(String tipoValor, Scanner leia) {   //médido para verificar entrada válida nas linhas
        int valorLinha = 0;
        boolean valorValido = false;
        while (!valorValido) {
            System.out.print("(1, 2 ou 3): ");
            valorLinha = leia.nextInt();
            if (valorLinha >=1 && valorLinha <= 3) {
                valorValido = true;
            } else {
                System.out.print("Entrada invalida, tente novamente.");
            }
        }
        valorLinha--;
        return valorLinha;
    }
}