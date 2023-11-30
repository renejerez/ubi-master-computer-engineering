%option noyywrap
%{
    #include<stdio.h>
	#include<stdlib.h>
    #include<string.h>

%}

%%


o\ benfica\ nao\ presta   {
    printf("FACT CHECK o benfica presta\n");
}

.   {
}

\n  {
}

%%

int main(int argc, char *argv[]) {
 yyin = fopen(argv[1], "r");
 yylex();
 fclose(yyin);
 } 