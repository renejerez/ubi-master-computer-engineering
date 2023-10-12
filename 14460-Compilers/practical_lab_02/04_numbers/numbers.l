%{
#include <stdio.h>
#include <stdlib.h>
%}

%%
[0-9]+\.[0-9]+    { printf("Number: %s\n", yytext); }
[0-9]+            { printf("Number: %s\n", yytext); }
[^0-9\n]+         { /* Ignore non-numeric characters */ }
\n                { /* Ignore newline */ }

%%

int yywrap() {
    // Return 1 to indicate the end of input.
    return 1;
}

int main() {
    printf("Enter numbers and strings:\n");
    while (1) {
        int c = getchar();
        if (c == EOF || c == '\n') {
            break;
        }
        unput(c);
        yylex();
    }
    return 0;
}
