digit[0-9]
letter[a-zA-Z]
ID[a-zA-Z][a-zA-Z0-9]*
WHITESPACE[ ]
quebra[\n]
TAB[\t]

%{
    #define YY_DECL extern "C" int yylex()
    #include<string.h>
    #include<iostream.h>
    using namespace std;
    FILE *out ;
	int linha;
%}
%option yylineno
%x COMMENT

%%

{quebra}

"/*" { linha=yylineno; BEGIN(COMMENT); }

<COMMENT>"*/" { BEGIN(INITIAL); }

<COMMENT>(.|\n);

<COMMENT><<EOF>> {fprintf(out,"(%d,ERROR,\"/*\")\n",linha); return 0;}

else|if|int|return|void|while {fprintf(out,"(%d,KEY,\"%s\")\n",yylineno ,yytext);} 

"+"|"-"|"*"|"/"|"<"|"<="|">"|">="|"=="|"!="|"="|";"|","|"("|")"|"["|"]"|"{"|"}" {fprintf(out,"(%d,SYM,\"%s\")\n",yylineno,yytext);}

{WHITESPACE}+|{quebra}|{TAB}+
 
{digit}+ {fprintf(out,"(%d,NUM,\"%s\")\n",yylineno,yytext);}

{digit}+{ID}+ {fprintf(out,"(%d,ERROR,\"%s\")\n",yylineno,yytext); return 0;}

{ID}+ {fprintf(out,"(%d,ID,\"%s\")\n",yylineno,yytext);}

. {fprintf(out,"(%d,ERROR,\"%s\")\n",yylineno,yytext); return 0;}

%%

int yywrap();

int main(int argc, char *argv[]){
    FILE *arquivo = fopen(argv[1],"r");
    if (!arquivo) {
      cout << "Arquivo inexistente" << endl;
      return -1;
    }
    yyin = arquivo;
    out = fopen(argv[2],"w");
    yylex();
    return 0;
}

int yywrap(){
    return 1;
}