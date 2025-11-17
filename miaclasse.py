from dataclasses import dataclass

# Anziché definire il metodo __init_() ed altri metodi dunder per la classe,
# sfrutto il decoratore @dataclass

# Con questa configurazione, definisce due attributi, crea un costruttore per
# inizializzarli, e definisce metodi per confronto ed ordinamento sui parametri;
# non serve quindi che sia io a definire __eq__() e __lt__()

@dataclass(eq=True, order=True) # specifico eq= , order= per confronto e ordinamento
class MiaClasse:
    attributo1 : int # specifico il tipo di dato che sono gli attributi
    attributo2 : str