from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Print

        self.lexer.add('Condition', r'IfTrue')

        self.lexer.add('Condition', r'Otherwise')

        self.lexer.add('Integer', r'Imw')

        self.lexer.add('SInteger', r'SIMw')

        self.lexer.add('Character', r'Chj')

        self.lexer.add('String', r'Series')

        self.lexer.add('Float', r'IMwf')

        self.lexer.add('SFloat', r'SIMwf')

        self.lexer.add('Void', r'NOReturn')

        self.lexer.add('Loop', r'RepeatWhen')

        self.lexer.add('Loop', r'Reiterate')

        self.lexer.add('Return', r'GetBack')

        self.lexer.add('Break', r'OutLoop')

        self.lexer.add('Struct', r'Loli')

        self.lexer.add('Comment',r'[/]' + r'\^')
        self.lexer.add('Comment', r'\/@')
        self.lexer.add('Comment', r'\@/')



        self.lexer.add('Assignment_operator', r'\=')

        self.lexer.add('Access Operator', r'\->')

        self.lexer.add('Arithmetic_Operation', r'[+*\/-]')

        self.lexer.add('Logic operators', r'\&&')
        self.lexer.add('Logic operators', r'\|{2}')
        self.lexer.add('Logic operators', r'\~')

        self.lexer.add('relational operators', r'\==')
        self.lexer.add('relational operators', r'<=')
        self.lexer.add('relational operators', r'>=')
        self.lexer.add('relational operators', r'\<')
        self.lexer.add('relational operators', r'\>')
        self.lexer.add('relational operators', r'\!=')



        self.lexer.add('Braces', r'\[')
        self.lexer.add('Braces', r'\]')
        self.lexer.add('Braces', r'\{')
        self.lexer.add('Braces', r'\}')
        self.lexer.add('Braces', r'\(')
        self.lexer.add('Braces', r'\)')

        self.lexer.add('Constant', r'\d+')

        self.lexer.add('Quotation Mark', r'\"')

        self.lexer.add('Inclusion', r'Include')



        self.lexer.add('Token_Delimiter', r'\$')

        self.lexer.add('Line_Delimiter', r'\.')

        self.lexer.add('Start', r'Start')

        self.lexer.add('End', r'Last')

        self.lexer.ignore('\s+')
        self.lexer.add('IDENTIFIER', r'[A-Za-z0-9\-\_]+')
        self.lexer.add('STR', r'[A-Za-z0-9=]+')

        self.lexer.add('ERROR', r'[\w\[\]`!@#$%\^&*()={}:;<>,+\'-]*')

        self.lexer.add('Comma', r'\,')
        self.lexer.add('semiComma', r'\;')
        self.lexer.add('underscore', r'\_')
    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()