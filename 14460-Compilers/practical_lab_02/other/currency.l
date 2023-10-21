%{
#include <stdio.h>
%}

%%

[\!\@\#\$\%\^\&\*\(\)\_\+\[\]\{\};:,.\/<>?\\|`] { printf("Special character: %s\n", yytext); }
.                                              { /* Ignore all other characters */ }
\n                                             { /* Ignore newline */ }

%%

int yywrap() {
    // Return 1 to indicate the end of input.
    return 1;
}

int main() {
    printf("Enter text (special characters will be identified):\n");
    yylex();
    return 0;
}
