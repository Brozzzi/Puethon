class ASTNode:
    pass

class IfStatement(ASTNode):
    def __init__(self, condition, then_block, else_block=None):
        self.condition = condition
        self.then_block = then_block
        self.else_block = else_block

class PrintStatement(ASTNode):
    def __init__(self, value):
        self.value = value