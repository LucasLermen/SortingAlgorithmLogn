#include<stdlib.h>
#include<stdio.h>
#include <time.h>

#define TAMREGISTROS 100000

void preencheRegistros(int *registros){
    int i;
    for (i = 0; i < TAMREGISTROS; ++i){
      registros[i] = rand() % (TAMREGISTROS+300);
    }
}

void swap(int *registros, int primeiro, int segundo){
  int aux;

  aux = registros[primeiro];
  registros[primeiro] = registros[segundo];
  registros[segundo] = aux;
}

//Usando pivo final

int rearranjaRegistros(int *registros, int inicial, int final){
  int pivo = registros[final];
  int j = inicial - 1;
  for (int i = inicial; i < final; i++) {
    if (pivo <= registros[i]) {
      j = j + 1;
      swap(registros, j, i);
    }
  }
  registros[final] = registros[j + 1];
  registros[j + 1] = pivo;

  return (j + 1);
}

//Ordena decrescente
void quickSort(int *registros, int inicial, int final){
  int auxFinal;

  if (inicial < final){
    auxFinal = rearranjaRegistros(registros, inicial, final);
    quickSort(registros, inicial, auxFinal-1);
    quickSort(registros, auxFinal+1, final);
  }
}

void imprimeRegistros(int *registros){
  int i;
  printf("\n\nREGISTROS\n");
  printf("--------------------------------------------------------------------------------------------------------------------------------------------\n" );
  for (i = 0; i < TAMREGISTROS; i++){
    printf("%d - ",registros[i]);
  }
}

int menu(){
  int op;
  printf("\n\n\n===================================================== MENU ==================================================================\n");
  printf("1 - Ordenar vetor \n");
  printf("2 - Printar o vetor\n");
  printf("0 - SAIR");
  printf("\n\n");
  printf("Digite a opcao desejada:");
  scanf("%d", &op);
  return op;
}


int main(){

  int registros[TAMREGISTROS], opcao;
  clock_t start, end;

  srand(time(NULL));

  preencheRegistros(registros);

  do{
    opcao = menu();
    switch (opcao) {
      case 0: printf("Encerrando ...\n");
      break;
      case 1:
        start = clock();
        quickSort(registros, 0, TAMREGISTROS-1);
        end = clock();
        printf ("Foram gastos %lf segundos para a ordenação\n",
               ((double)( end - start ) / ((double)CLOCKS_PER_SEC )));

      break;
      case 2: imprimeRegistros(registros);
      break;
      default:
        printf("Opcao Inexistente\n");
    }
  }while (opcao!=0);
  return 0;

}
