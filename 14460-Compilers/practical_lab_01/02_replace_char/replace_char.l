%{
#include <stdio.h>
#include <string.h>

#define MAX_STRING_LENGTH 1024
char input_string[MAX_STRING_LENGTH];
char replacement_string[MAX_STRING_LENGTH];
char old_string[MAX_STRING_LENGTH];
int input_length = 0;
int replace_length = 0;

void replaceString() {
    char output_string[MAX_STRING_LENGTH];
    char* position = strstr(input_string, old_string);

    while (position != NULL) {
        int length = position - input_string;
        strncpy(output_string, input_string, length);
        output_string[length] = '\0';
        strcat(output_string, replacement_string);
        strcat(output_string, position + replace_length);
        strcpy(input_string, output_string);
        position = strstr(input_string, old_string);
    }
}

%}

%%
[a-zA-Z]   { }
.         { input_string[input_length++] = yytext[0]; }
\n        { 
             input_string[input_length] = '\0';
             return 0;
          }
%%

int yywrap() {
    return 1; // Indicate end of input
}

int main() {
    printf("Enter the string: ");
    fgets(input_string, MAX_STRING_LENGTH, stdin);
    input_length = strlen(input_string);
    printf("Enter the old string: ");
    scanf("%s", old_string);
    printf("Enter the replacement string: ");
    scanf("%s", replacement_string);
    replace_length = strlen(old_string);
    replaceString();
    printf("Final string changed: %s\n", input_string);
    return 0;
}
