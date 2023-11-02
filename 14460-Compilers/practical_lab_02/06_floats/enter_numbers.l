%{
#include <stdio.h>
%}

%%
[0-9]+\.[0-9]+           { printf("Float: %s\n", yytext); }
[0-9]+                   { /* Ignore integer values */ }
.                        { /* Ignore all other characters */ }
\n                       { /* Ignore newline */ }

%%

int yywrap() {
    // Return 1 to indicate the end of input.
    return 1;
}

int main() {
    printf("Enter numbers with spaces (integers or floats):\n");
    yylex();
    return 0;
}
