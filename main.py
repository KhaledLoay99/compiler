from lexer import Lexer
import io
from parserTB import Parser


new_input="""
    /@
    @/
 /^This is main function
 Imw$3num=5.
 Imw$decrease(){
 Reiterate (counter<num){
 reg3=reg3-1.} }
"""


print(new_input)
lexer = Lexer().get_lexer()
line_no = 1
tokens = lexer.lex(new_input)
d ={1: ["Line No", "Lexeme","Return Token","Lexeme No in Line","Matchability"]}
i = 2
lexemer = 1

for y in new_input.splitlines():
    for token in lexer.lex(y):
        d[i]=[line_no, token.getstr(),token.gettokentype(),lexemer,"Matchable"]
        i = i+1
        lexemer = lexemer +1
    line_no = line_no +1
    lexemer = 1


for k, v in d.items():
 line=v
 print ("{:<15} {:<20} {:<30} {:<35} {:<20}".format(line[0], line[1], line[2],line[3],line[4]))