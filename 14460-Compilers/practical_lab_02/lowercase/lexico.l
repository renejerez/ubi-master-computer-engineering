%{
    /*definitions */

%}

%%
[a-z] {printf("Single lowercase character\n");}
. {printf("Not a lowercase character\n");}
\n {return 0;}

%%
yywrap() {}

int main() {
    printf("Enter string: ");
    yylex();

    return 0;

}