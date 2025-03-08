def übersetzen(code):
    übersetzungen = {
        "if": "wenn",
        "else": "sonst",
        "elif": "sowenn",
        "or": "oder",
        "pass": "erlasse",
        "return": "ausgabe",
        "await": "erwarte",
        "break": "unterbreche",
        "import": "importiere",
        "except": "ausgenommen",
        "in": "in",
        "raise": "erhebe",
        "class": "klasse",
        "finally": "endlich",
        "is": "ist",
        "and": "und",
        "continue": "fortsetzen",
        "for": "für",
        "lambda": "lambda",
        "try": "versuch",
        "as": "als",
        "def": "definiere",
        "from": "aus",
        "nonlocal": "außerorts",
        "while": "während",
        "assert": "behaupte",
        "del": "entferne",
        "global": "weltweit",
        "not": "nicht",
        "with": "mit",
        "async": "asynchron",
        "yield": "ergebe",
        "list": "liste",
        "dict": "wörterbuch",
        "False": "Falsch",
        "True": "Wahr",
        "None": "Nichts",
        "print": "drucke",
    }

    for python, deutsch in übersetzungen.items():
        if deutsch in code:
            code = code.replace(f" {deutsch} ", f" {python} ")
            code = code.replace(f"{deutsch} ", f"{python} ")  # Damit wir keine Leerzeichen verlieren
            code = code.replace(f" {deutsch}", f" {python}")  # Am Ende der Zeile
            code = code.replace(deutsch, python) 

    return code

def dolmetscher(code):
    python_code = übersetzen(code)
    exec(python_code)

# Beispiel: Deutscher Code
code_deutsch = """
definiere begrüßen(name):
    wenn name == "Welt":
        drucke("Hallo, Welt!")
    sonst:
        drucke("Hallo, " + name)

begrüßen("Max")
"""

dolmetscher(code_deutsch)