%{
#include <stdio.h>
%}

%token NUMBER

%%
line: exp '\n' { printf("%d\n", $1); }
    ;
exp: NUMBER { $$ = $1; }
   | exp '+' NUMBER { $$ = $1 + $3; }
   | exp '-' NUMBER { $$ = $1 - $3; }
   ;

%%

int main(void) {
    yyparse();
    return 0;
}

int yyerror(char *s) {
    fprintf(stderr, "error: %s\n", s);
    return 0;
}
