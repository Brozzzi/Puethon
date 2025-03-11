import re

TOKEN_SPEZIFIKATION = [
    
    # KONTROLLFLUSS
    ("WENN", r"wenn"),              # if
    ("SOWENN", r"sowenn")           # elif
    ("SONST", r"sonst"),            # else
    ("FÜR", r"für"),                # for
    ("SOLANGE", r"solange"),        # while
    ("UNTERBRECHE", r"unterbreche"),# break
    ("FORTSETZEN", r"fortsetzen"),  # continue
    ("VERSUCHE", r"versuche"),      # try
    ("AUSGENOMMEN", r"ausgenommen"),# except
    ("ENDLICH", r"endlich"),        # finally
    ("ERHEBE", r"erhebe"),          # raise
    ("BEHAUPTE", r"behaupte"),      # assert
    ("MIT", r"mit"),                # with
    ("ALS", r"als"),                # as
    
    # FUNKTION & KLASSEN
    ("DEFINIERE", r"definiere"),    # def
    ("KLASSE", r"klasse"),          # class
    ("AUSGABE", r"ausgabe"),        # return
    ("ERGEBE", r"ergebe"),          # yield

    # DATENFLUSS & TYPEN
    ("IMPORTIERE", r"importiere"),  # import
    ("AUS", r"aus"),                # from
    ("ALS", r"als"),                # as
    ("ERLASSE", r"erlasse"),        # pass
    ("ENTFERNE", r"entferne"),      # del
    ("WELTWEIT", r"weltweit"),      # global
    ("AUßERORTS", r"außerorts"),    # nonlocal
    ("LAMBDA", r"lambda"),          # lambda

    # BOOLESCHE WERTE & VERGLEICHEN
    ("WAHR", r"Wahr"),              # True
    ("FALSCH", r"Falsch"),          # False
    ("NICHTS", r"Nichts"),          # None
    ("UND", r"und"),                # and
    ("ODER", r"oder"),              # oder
    ("NICHT", r"nicht"),            # not
    ("IST", r"ist"),                # is
    ("IN", r"in"),                  # in

    # DATENTYP & LITERALE
    ("INT", r"int"),                # int
    ("FLOAT", r"float"),            # float
    ("KOMPLEX", r"komplex"),        # complex
    ("STRING", r"string"),          # str
    ("BYTES", r"bytes"),            # bytes
    ("BYTEARRAY", r"bytearray"),    # bytearray
    ("BOOL", r"bool"),              # bool
    ("LISTE", r"liste"),            # list
    ("TUPEL", r"tupel"),            # tuple
    ("SETZE", r"setze"),            # set
    ("WÖRTERBUCH", r"wörterbuch"),  # dict

    # REST
    ("DRUCKE", r"drucke"),          # print
    ("IDENT", r"[a-zA-Z_]\w*"),     # Variablen
    ("NUMBER", r"\d+"),             # Zahlen
    ("STRING", r"'[^']*'"),         # Strings
    ("OP", r"[+*/<>-]="),           # Operatoren
    ("PAREN", r"[():]"),            # Klammern
    ("WHITESPACE", r"\s+"),         # Leerzeichen (wird ignoriert)
]

def tokenize(code):
    tokens = []
    for typ, regex in TOKEN_SPEZIFIKATION:
        for match in re.finditer(regex, code):
            if typ != "WHITESPACE":
                tokens.append((typ, match.group))
    
    return tokens