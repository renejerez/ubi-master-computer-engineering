%{
/* Definitions */
int letter_count = 0;
%}

%%
[a-zA-Z]   { letter_count++; }
.         {/* Ignore all other characters */}
\n        { printf("Number of letters in the input string: %d\n", letter_count); return 0; }
%%

int yywrap() {
    return 1; // Indicate end of input
}

int main() {
    printf("Enter a string: ");
    yylex();
    return 0;
}
