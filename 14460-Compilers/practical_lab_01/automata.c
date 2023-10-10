#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

struct estado
{
    bool start;
    bool finish;
    int id;
    char transicoes[2];
    struct estado *trans[2];
};

int main()
{
    struct estado *zero = malloc(sizeof(struct estado));
    struct estado *uno = malloc(sizeof(struct estado));
    struct estado *dos = malloc(sizeof(struct estado));
    struct estado *tres = malloc(sizeof(struct estado));
    struct estado *quatro = malloc(sizeof(struct estado));
    zero->id = 0;
    uno->id = 1;
    dos->id = 2;
    tres->id = 3;
    quatro->id = 4;
    zero->start = true;
    uno->start = false;
    dos->start = false;
    tres->start = false;
    quatro->start = false;
    zero->finish = false;
    uno->finish = false;
    dos->finish = false;
    tres->finish = true;
    quatro->finish = true;
    zero->transicoes[0] = 'a';
    zero->transicoes[1] = 'b';
    uno->transicoes[0] = 'd';
    uno->transicoes[1] = 'b';
    dos->transicoes[0] = 'a';
    dos->transicoes[1] = 'b';
    tres->transicoes[0] = 'a';
    tres->transicoes[1] = 'b';
    quatro->transicoes[0] = 'a';
    quatro->transicoes[1] = 'b';
    zero->trans[0] = uno;
    zero->trans[1] = dos;
    uno->trans[0] = uno;
    uno->trans[1] = tres;
    dos->trans[0] = quatro;
    dos->trans[1] = dos;
    tres->trans[0] = quatro;
    tres->trans[1] = dos;
    quatro->trans[0] = uno;
    quatro->trans[1] = tres;

    char letra;
    scanf("%c", &letra);
    char elcamino1[10] = "";
    char elcamino2[10] = "";
    
    struct estado* path1;
    struct estado* path2;
    if (letra == zero->transicoes[0])
    {
        path1 = zero->trans[0];
    }
    else if(letra == zero->transicoes[1]){
        path1 = zero->trans[1];
    }
    else{
        printf("letra mal lida");
        return 0;
    }
    sprintf(elcamino1, "%d%d%d", zero->id, path1->id, path1->trans[0]->id);
    sprintf(elcamino2, "%d%d%d", zero->id, path1->id, path1->trans[1]->id);
    path2 = path1->trans[1];
    path1 = path1->trans[0];
    
    if (path1->trans[0]->finish)
    {
        sprintf(elcamino1, "%s%d", elcamino1, path1->trans[0]->id);
    }
    else
    {
        sprintf(elcamino1, "%s%d", elcamino1, path1->trans[1]->id);
    }

    if (path2->trans[0]->finish)
    {
        sprintf(elcamino2, "%s%d", elcamino2, path2->trans[0]->id);
    }
    else
    {
        sprintf(elcamino2, "%s%d", elcamino2, path2->trans[1]->id);
    }
    
    

    printf("caminho 1:%s\ncaminho 2:%s\n", elcamino1, elcamino2);
}