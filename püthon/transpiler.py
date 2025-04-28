import ast
import astor  # pip install astor

def transpile(tree):
    return astor.to_source(tree)
