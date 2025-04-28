import ast

def parse(code):
    try:
        return ast.parse(code)
    except SyntaxError as e:
        raise Exception(f"Syntaxfehler: {e}")
