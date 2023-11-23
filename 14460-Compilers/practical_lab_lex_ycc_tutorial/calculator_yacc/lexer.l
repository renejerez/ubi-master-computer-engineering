%{
#include "y.tab.h"
extern int yylval;
%}

%%
[0-9]+   { yylval = atoi(yytext); return NUMBER; }
\+       { return PLUS; }
\-       { return MINUS; }
\*       { return TIMES; }
\/       { return DIVIDE; }
\n       { return EOL; }
[ \t]    { /* ignore whitespace */ }
.        { printf("Unexpected character: %s\n", yytext); }
%%

int yywrap(void) {
    return 1;
}
