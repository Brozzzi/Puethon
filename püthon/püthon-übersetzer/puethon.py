import json
import sys
from errors import UndefinierteVariableFehler, FalscherTypFehler

with open("keywords.json", "r", encoding="utf-8") as f:
    keywords = json.load(f)

de_to_en = {v: k for k, v in keywords.items()}

def püthon_to_python(code):
    for de, en in de_to_en.items():
        code = code.replace(de, en)
    return code

def run_püthon(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()

    python_code = püthon_to_python(code)

    try: 
        exec(python_code)
    except Exception as e:
        print("Fehler in Püthon:", e)

def prüfe_variable(var_name, variablen):
    if var_name not in variablen:
        raise UndefinierteVariableFehler(var_name)

def rechne(x, y):
    if not isinstance(x, int) or not isinstance(y, int):
        raise FalscherTypFehler("Ganzzahl", type(x).__name__)
    return x + y

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Verwendung: python püthon.py datei.pü")
        sys.exit(1)

    run_püthon(sys.argv[1])