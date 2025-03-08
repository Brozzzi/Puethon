class PüthonFehler(Exception):
    """Basis-Klasse für alle Püthon-Fehlermeldungen"""
    def __init__(self, nachricht):
        super().__init__(f"❌ Püthon-Fehler: {nachricht}")

class UndefinierteVariableFehler(PüthonFehler):
    def __init__(self, variable_name):
        super().__init__(f"Die Variable '{variable_name}' ist nicht definiert!")

class FalscherTypFehler(PüthonFehler):
    def __init__(self, erwartet, erhalten):
        super().__init__(f"Erwarteter Typ: {erwartet}, aber erhalten: {erhalten}")
