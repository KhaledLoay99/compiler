from lexer import Lexer
import io
from parserTB import Parser
import re

input = """
#
/@ 
This is main function@/
    ->
    fdghgsdffhf
    /@ dfghfhdsfdxgfhfgf
        @/
        )
      ;
 /^Imw$3num=5.
 /^Imw$decrease(){
 /^Reiterate (counter<num){
 reg3=reg3-1.} }"""
temp_input="""
"""

# s = '<@ """@$ /@FSDF >something@/ something <more noise>'
# t = re.sub('/@.*?@/', ' ', s)
# print(t)


#Remove The Single Comments
for y in input.splitlines():
    if("/^" in y):
        temp_input = temp_input+y[0:y.find("/^")+2]+"\n"
    else:
        temp_input = temp_input + y + "\n"

#Remove The Multiple Comments
temp_input = re.sub('/@.*?@/', '/@@/ ', temp_input , flags=re.DOTALL)




lexer = Lexer().get_lexer()
line_no = 1
tokens = lexer.lex(temp_input)
d ={1: ["Line No", "Lexeme","Return Token","Lexeme No in Line","Matchability"]}
i = 2
lexemer = 1
Allerrors = 0


for y in temp_input.splitlines():
    for token in lexer.lex(y):
        if(token.gettokentype() != "ERROR"):
          d[i]=[line_no, token.getstr(),token.gettokentype(),lexemer,"Matchable"]
        else:
          d[i] = [line_no, token.getstr(), token.gettokentype(), lexemer, "Non Matchable"]
          Allerrors = Allerrors + 1
        i = i+1
        lexemer = lexemer +1
    line_no = line_no +1
    lexemer = 1

for k, v in d.items():
 line=v
 print ("{:<15} {:<20} {:<30} {:<35} {:<20}".format(line[0], line[1], line[2],line[3],line[4]))
print ("\nNUMBER OF ERRORS ",Allerrors,"\n")

# pg = Parser()
# pg.parse()
# parser = pg.get_parser()
# parser.parse(tokens)
