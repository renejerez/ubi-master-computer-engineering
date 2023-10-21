%{
#include <stdio.h>
%}

%%

[0-9]+[ ]?(\$) {
    printf("Moeda: USD (Dólar)\n");
    printf("Valor: %s\n", yytext);
}

[0-9]+[ ]?(€) {
    printf("Moeda: EUR (Euro)\n");
    printf("Valor: %s\n", yytext);
}

[0-9]+[ ]?(£) {
    printf("Moeda: Libra (British Pound)\n");
    printf("Valor: %s\n", yytext);
}

.|\n 

%%

int yywrap() {
    return 1;  
}

int main() {
    printf("Digite um valor com o simbolo da moeda (exemplo, 100 $ ou 50 €):\n");
    yylex();
    return 0;
}
