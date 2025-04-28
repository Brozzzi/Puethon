import sys
from püthon.lexer import tokenize
from püthon.parser import parse
from püthon.transpiler import transpile

def main():
    if len(sys.argv) != 2:
        print("Nutzung: püthon <dateiname.pü>")
        sys.exit(1)

    filename = sys.argv[1]

    with open(filename, 'r', encoding='utf-8') as f:
        code = f.read()

    translated_code = tokenize(code)
    tree = parse(translated_code)
    python_code = transpile(tree)

    exec(python_code, globals())
