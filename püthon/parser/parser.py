from ast import *


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0

    def parse(self):
        return self.parse_statement()

    def parse_statement(self):
        if self.match("WENN"):
            return self.parse_if
        elif self.match("DRUCKE"):
            return self.parse_print()
        else:
            raise SyntaxError("Unerwartetes Token: " + self.peek()[1])

    def parse_if(self):
        condition = self.consume("IDENT")[1] + " " + self.consume("OP")[1] + " " + self.consume("NUMBER")[1]
        self.consume("PAAREN")
        then_block = self.parse_statement()
        else_block = None
        if self.match("SONST"):
            self.consume("PAREN")  # Doppelpunkt `:`
            else_block = self.parse_statement()
        return IfStatement(condition, then_block, else_block)

    def parse_print(self):
        value = self.consume("STRING")[1]
        return PrintStatement(value)