#!/usr/bin/env python
import os.path
import sys

def je_ingredience_v_receptu(ingredience, recept):
    with open(recept) as fp:
        if ingredience in fp.read():
            return True
            
    return False
            
def najdi_recept_podle_ingredience(ingredience):
    tenhle_script = __file__
    adresar_projektu = os.path.dirname(tenhle_script)
    adresar_receptu = os.path.join(adresar_projektu, 'recepty')
    
    nalezene_recepty = []
    for f in os.listdir(adresar_receptu):
        if je_ingredience_v_receptu(ingredience, os.path.join(adresar_receptu, f)):
            nalezene_recepty.append(f)
            
    if nalezene_recepty:
        print("'{}' nalezen v nasledujicich receptech".format(ingredience))
        print("\n".join(nalezene_recepty))
    else:
        print("Takovy recept nemame")


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

if len(sys.argv) == 2:
    print("Hledam recept obsahujici:", sys.argv[1])
    najdi_recept_podle_ingredience(sys.argv[1])
