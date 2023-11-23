%{
#include <stdio.h>
extern int yylex(void);
void yyerror(const char *s);
%}

%token NUMBER
%token PLUS MINUS TIMES DIVIDE
%token EOL

%%
calc: /* empty */
    | calc expr EOL { printf("Result: %d\n", $2); }
    ;

expr: NUMBER
    | expr PLUS expr   { $$ = $1 + $3; }
    | expr MINUS expr  { $$ = $1 - $3; }
    | expr TIMES expr  { $$ = $1 * $3; }
    | expr DIVIDE expr { $$ = $1 / $3; }
    ;

%%

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}

int main(void) {
    return yyparse();
}
