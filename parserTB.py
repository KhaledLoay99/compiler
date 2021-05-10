from rply import ParserGenerator
from ast import Number, Sum, Print


class Parser():

    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['Condition', 'Integer', 'SInteger', 'Character',
              'Float','SFloat','Void','Loop','Return',
             'Break','Arithmetic_Operation','Logic_operators',
             'relational_operators','Assignment_operator','Braces',
             'Inclusion','Comment','Token_Delimiter',
             'Line_Delimiter','Start','End','IDENTIFIER','STR','String','Comma','semiComma','underscore','Text']
        )

    def parse(self) -> object:
          @self.pg.production('program : Start Line_Delimiter comment Line_Delimiter declaration_list Line_Delimiter'
                              ' End')
          def program(p):
                print("Valid Program")
          @self.pg.production('program : comment Line_Delimiter include_command')
          @self.pg.production('program : Start Line_Delimiter declaration_list Line_Delimiter End')
          def program(p):
                print("Valid Program")

            #Rule 2
          @self.pg.production('declaration_list : declaration')
          @self.pg.production('declaration_list : declaration_list declaration')
          def declaration_list(p):
                print("Valid Declaration List")

            #Rule 3
          @self.pg.production('declaration : fun_declaration')
          @self.pg.production('declaration : var_declaration')
          def declaration(p):
                print("Valid declaration")

            # Rule 4
          @self.pg.production('var_declaration : type_specifier Token_Delimiter IDENTIFIER Line_Delimiter ')
          def var_declaration(p):
            print("Valid var_declaration")

        # Rule 5
          @self.pg.production('type_specifier : SInteger')
          @self.pg.production('type_specifier : Character')
          @self.pg.production('type_specifier : String')
          @self.pg.production('type_specifier : Float')
          @self.pg.production('type_specifier : SFloat')
          @self.pg.production('type_specifier : Void')
          @self.pg.production('type_specifier : Integer')
          def type_specifier (p):
            print("Valid Type_Specifier")

        # Rule 6
          @self.pg.production('fun_declaration : comment Token_Delimiter IDENTIFIER')
          @self.pg.production('fun_declaration : type_specifier Token_Delimiter IDENTIFIER Braces params Braces compound_stmt')
          def fun_declaration(p):
                print("Valid fun_declaration")

        # Rule 5
          @self.pg.production('type_specifier : SInteger')
          @self.pg.production('type_specifier : Character')
          @self.pg.production('type_specifier : String')
          @self.pg.production('type_specifier : Float')
          @self.pg.production('type_specifier : SFloat')
          @self.pg.production('type_specifier : Void')
          @self.pg.production('type_specifier : Integer')
          def type_specifier(p):
                    print("Valid Type_Specifier")

        # Rule 7
          @self.pg.production('params : Void')
          @self.pg.production('params :  ''')
          @self.pg.production('params : param_list')
          def params(p):
            print("Valid params")
        # Rule 8
          @self.pg.production('param_list : param')
          @self.pg.production('param_list : param_list Comma param')
          def param_list(p):
            print("Valid param_list")

        # Rule 9

          @self.pg.production('param : type_specifier Token_Delimiter IDENTIFIER')
          def param(p):
            print("Valid param")

            # Rule 5

          @self.pg.production('type_specifier : SInteger')
          @self.pg.production('type_specifier : Character')
          @self.pg.production('type_specifier : String')
          @self.pg.production('type_specifier : Float')
          @self.pg.production('type_specifier : SFloat')
          @self.pg.production('type_specifier : Void')
          @self.pg.production('type_specifier : Integer')
          def type_specifier(p):
            print("Valid Type_Specifier")

            # Rule 10

          @self.pg.production('compound_stmt : Braces local_declarations statement_list Braces')
          @self.pg.production('compound_stmt : Braces comment Line_Delimiter local_declarations statement_list Braces')
          def compound_stmt(p):
            print("Valid compound_stmt")

            # Rule 11

          @self.pg.production('local_declarations :''')
          @self.pg.production('local_declarations : local_declarations var_declaration')
          def local_declarations(p):
            print("Valid local_declarations")



        # Rule 4
          @self.pg.production('var_declaration : type_specifier Token_Delimiter IDENTIFIER Line_Delimiter ')
          def var_declaration(p):
            print("Valid var_declaration")

        # Rule 12
          @self.pg.production('statement_list :''')
          @self.pg.production('statement_list : statement_list statement')

          def statement_list(p):
            print("Valid statement_list")

        # Rule 13
          @self.pg.production('statement : compound_stmt')
          @self.pg.production('statement : selection_stmt')
          @self.pg.production('statement : iteration_stmt')
          @self.pg.production('statement : jump_stmt')
          @self.pg.production('statement : expression_stmt')
          def statement(p):
            print("Valid statement")

         # Rule 10
          @self.pg.production('compound_stmt : Braces local_declarations statement_list Braces')
          @self.pg.production('compound_stmt : Braces comment Line_Delimiter local_declarations statement_list Braces')
          def compound_stmt(p):
            print("Valid compound_stmt")


        # Rule 14
          @self.pg.production('expression_stmt : expression')
          def expression_stmt(p):
            print("Valid expression_stmt")


        # Rule 15
          @self.pg.production('selection_stmt : Condition Braces expression Braces statement Condition statement')
          @self.pg.production('selection_stmt : Condition Braces expression Braces statement')
          def selection_stmt(p):
            print("Valid selection_stmt")

        # Rule 13
          @self.pg.production('statement : compound_stmt')
          @self.pg.production('statement : selection_stmt')
          @self.pg.production('statement : iteration_stmt')
          @self.pg.production('statement : jump_stmt')
          @self.pg.production('statement : expression_stmt')
          def statement(p):
            print("Valid statement")

        # Rule 16
          @self.pg.production('iteration_stmt : Reiterate_statement')
          @self.pg.production('iteration_stmt : Repeat_statement ')
          def iteration_stmt(p):
            print("Valid iteration_stmt")

        # Rule 17
          @self.pg.production('Repeat_statement : Loop Braces expression Braces statement')
          def Repeat_statement(p):
            print("Valid Repeat_statement")

        # Rule 13
          @self.pg.production('statement : compound_stmt')
          @self.pg.production('statement : selection_stmt')
          @self.pg.production('statement : iteration_stmt')
          @self.pg.production('statement : jump_stmt')
          @self.pg.production('statement : expression_stmt')
          def statement(p):
            print("Valid statement")


        # Rule 18
          @self.pg.production('Reiterate_statement : Loop Braces expression Comma expression Comma expression  Braces statement')
          def Reiterate_statement(p):
            print("Valid Reiterate_statement")

        # Rule 13
          @self.pg.production('statement : compound_stmt')
          @self.pg.production('statement : selection_stmt')
          @self.pg.production('statement : iteration_stmt')
          @self.pg.production('statement : jump_stmt')
          @self.pg.production('statement : expression_stmt')
          def statement(p):
            print("Valid statement")

        # Rule 19
          @self.pg.production(' jump_stmt : Return expression semiComma Break semiComma')
          @self.pg.production(' jump_stmt : Return expression semiComma')
          def jump_stmt(p):
            print("Valid jump_stmt")

        # Rule 21
          @self.pg.production(' id_assign : IDENTIFIER')
          def Reiterate_statement(p):
            print("Valid Reiterate_statement")

        # Rule 22
          @self.pg.production('simple_expression : additive_expression')
          @self.pg.production('simple_expression : additive_expression relop additive_expression  ')
          def simple_expression(p):
            print("Valid simple_expression")

        # Rule 23
          @self.pg.production('relop : Logic_operators')
          @self.pg.production('relop : Logic_operators')
          @self.pg.production('relop : relational_operators')
          @self.pg.production('relop : relational_operators')
          @self.pg.production('relop : relational_operators')
          @self.pg.production('relop : relational_operators ')
          def simple_expression(p):
            print("Valid simple_expression")

        # Rule 23
          @self.pg.production('additive_expression : term')
          @self.pg.production('additive_expression : additive_expression addop term ')
          def additive_expression(p):
            print("Valid additive_expression")

        # Rule 24
          @self.pg.production('addop : Arithmetic_Operation')
          @self.pg.production('addop : Arithmetic_Operation')
          def addop(p):
            print("Valid addop")

        # Rule 26
          @self.pg.production('term : factor')
          @self.pg.production('term : term mulop factor ')
          def term(p):
            print("Valid term")

        # Rule 27
          @self.pg.production('mulop : Arithmetic_Operation')
          @self.pg.production('mulop : Arithmetic_Operation')
          def mulop(p):
            print("Valid mulop")

        # Rule 28

          @self.pg.production('factor : id_assign')
          @self.pg.production('factor : call ')
          @self.pg.production('factor : num ')
          @self.pg.production('factor : Braces IDENTIFIER Braces ')
          def factor(p):
              print("Valid factor")

        # Rule 21
          @self.pg.production(' id_assign : IDENTIFIER')
          def id_assign(p):
            print("Valid id_assign")
        # Rule 29
          @self.pg.production('call : IDENTIFIER Braces args Braces ')
          def call(p):
            print("Valid call")

        # Rule 30
          @self.pg.production('args : ''')
          @self.pg.production('args : arg_list ')
          def args(p):
            print("Valid args")


        # Rule 31
          @self.pg.production('arg_list : expression')
          @self.pg.production('arg_list : arg_list Comma expression || expression')
          def arg_list(p):
            print("Valid arg_list")

        # Rule 32
          @self.pg.production('num : Unsigned_num')
          @self.pg.production('num : Signed_num ')
          def num (p):
            print("Valid num")


        # Rule 33
          @self.pg.production('Signed_num : neg_num')
          @self.pg.production('Signed_num : pos_num ')
          def Signed_num (p):
            print("Valid Signed_num")


        # Rule 34
          @self.pg.production('Unsigned_num :  value')
          def Unsigned_num (p):
            print("Valid Unsigned_num")

        # Rule 35
          @self.pg.production('pos_num : Arithmetic_Operation value')
          def pos_num (p):
            print("Valid pos_num")



        # Rule 36
          @self.pg.production('neg_num : Arithmetic_Operation value')
          def neg_num (p):
            print("Valid neg_num")

        # Rule 37
          @self.pg.production('value : Float underscore Integer')
          @self.pg.production('value : Integer underscore Integer')
          def value (p):
            print("Valid value")

        # Rule 38
        #   @self.pg.production('comment : Arithmetic_Operation Comment  String Comment Arithmetic_Operation ')
          @self.pg.production('comment :  Comment Comment ')
          def comment (p):
              print("Valid comment")


        # Rule 39
          @self.pg.production('include_command : Inclusion Braces F_name Text Braces semiComma')
          def include_command (p):
            print("Valid include_command")



        # Rule 40
          @self.pg.production('F_name : STR ')
          def F_name(x):
              print("Valid F_name")

        # Rule 41
          @self.pg.production('expression : simple_expression')
          @self.pg.production('expression : id_assign')
          @self.pg.production('expression : id_assign Assignment_operator expression ')
          def expression (p):
            print("Valid expression")

            # Rule 21

          @self.pg.production(' id_assign : IDENTIFIER')
          def id_assign(p):
            print("Valid id_assign")



        # Rule 22
          @self.pg.production('simple_expression : additive_expression')
          @self.pg.production('simple_expression : additive_expression relop additive_expression || additive_expression')
          def simple_expression(p):
            print("Valid simple_expression")



            @self.pg.error
            def error_handle(token):
                raise ValueError(token)

    def get_parser(self):
        return self.pg.build()