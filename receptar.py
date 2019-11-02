import os.path
print("--- Ukáže nejlepší recept. ---")


def nacti_recept(jmeno):
    """
    Když této funkci dáš jméno textového souboru ze složky recepty,
    tak vrátí text receptu jako řetězec.
    """
    tenhle_script = __file__
    adresar_projektu = os.path.dirname(tenhle_script)
    adresar_receptu = os.path.join(adresar_projektu, 'recepty')
    cesta_k_receptu = os.path.join(adresar_receptu, jmeno)
    with open(cesta_k_receptu, 'r') as f:
        return f.read()


NAZVY_RECEPTU = [
    'chlebova_pochoutka.txt',
]


# Máme zatím jen jeden recept, tak ho prostě ukážeme
print(nacti_recept(NAZVY_RECEPTU[0]))
