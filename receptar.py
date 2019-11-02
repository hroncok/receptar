#!/usr/bin/env python
import os.path
import sys

def je_ingredience_v_receptu(ingredience, recept):
    with open(recept) as fp:
        if ingredience in fp.read():
            return True
            
    return False
            
def tiskni_recepty(recepty):
    print("\nTisknu nalezene recepty")
    for recept in recepty:
        print('='*50,'\nRECEPT: '+recept[0],'\n'+'='*50)
        
        with open(recept[1]) as fp:
            print(fp.read())
        print('\n'*3)
            
            
def najdi_recept_podle_ingredience(ingredience):
    tenhle_script = __file__
    adresar_projektu = os.path.dirname(tenhle_script)
    adresar_receptu = os.path.join(adresar_projektu, 'recepty')
    
    nalezene_recepty = []
    for f in os.listdir(adresar_receptu):
        recipe_fullpath = os.path.join(adresar_receptu, f)
        if je_ingredience_v_receptu(ingredience, recipe_fullpath):
            nalezene_recepty.append((f, recipe_fullpath))
            
    if nalezene_recepty:
        print("'{}' nalezen v nasledujicich receptech".format(ingredience))
        for recept in nalezene_recepty:
            print(recept[0])
        tiskni_recepty(nalezene_recepty)
        
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
else:
    print("Nebol zadany ziaden argument")