%{
#include <stdio.h>
int alphabet_count = 0;
int digit_count = 0;
int whitespace_count = 0;
int space_count = 0;
int tab_count = 0;
int line_count = 0;
int other_count = 0;
%}

%%
[A-Za-z]   { alphabet_count++; }
[0-9]      { digit_count++; }
[ \t]      { whitespace_count++; }
' '        { space_count++; }
'\t'       { tab_count++; }
\n         { line_count++; }
.          { other_count++; }
%%

int main(int argc, char* argv[]) {
    if (argc != 2) {
        printf("Usage: %s <input_file>\n", argv[0]);
        return 1;
    }

    FILE* input_file = fopen(argv[1], "r");

    if (input_file == NULL) {
        perror("Error opening the input file");
        return 1;
    }

    int c;
    while ((c = fgetc(input_file)) != EOF) {
        // Pass the character to the Flex lexer
        yyinput(&c, 1);
    }

    fclose(input_file);

    printf("Alphabetic characters: %d\n", alphabet_count);
    printf("Digit characters: %d\n", digit_count);
    printf("Whitespace characters: %d\n", whitespace_count);
    printf("Space characters: %d\n", space_count);
    printf("Tab characters: %d\n", tab_count);
    printf("Line count: %d\n", line_count);
    printf("Other characters: %d\n", other_count);

    return 0;
}
