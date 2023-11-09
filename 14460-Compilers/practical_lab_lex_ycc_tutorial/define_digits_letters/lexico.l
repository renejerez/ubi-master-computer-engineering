%option noyywrap
digit [0-9]
letter [A-Za-z]

%{
// Definitions
int count;
%}

%%
{letter}({letter}|{digit})* count++;
%%

// sub-routines
int main(void) {
yylex();
printf("number of identifiers = %d\n", count);
return 0;
}