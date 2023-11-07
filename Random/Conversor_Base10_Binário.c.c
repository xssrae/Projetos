/* Programa para converter da base 10 para a base 2 */

int main() {
  int num,    /* numero dado (na base decimal)             */
      bin,	  /* numero dado convertido para base 2        */
      aux,	  /* auxiliar                                  */
      dig,	  /* guardara cada um dos digitos binarios     */
      pot;    /* potencia de 10                            */

  printf("Digite um numero natural: ");
  scanf("%d", &num);

  /* inicializacoes */
  aux = num;
  bin = 0;
  pot = 1;

  while (aux > 0) {
    dig = aux % 2;          /* proximo digito binario menos significativo  */
    aux = aux / 2;          /* remove esse digito do que resta             */
    bin = bin + dig * pot;  /* adiciona o digito como o mais significativo */
    pot = pot * 10;
  }
  printf("O numero %d escrito na base binaria: %d\n", num, bin);

  return 0;
}
