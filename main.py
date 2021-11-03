from Logic.crud import create
from Tests.test_crud import test_crud
from Tests.test_determinare_pret_minim import test_determinare_pret_minim
from Tests.test_modificare_gen import test_modificare_gen
from Tests.test_reducere import test_reducere
from UI.consola2 import run_ui2

from UI.console import run_ui



def main():
   lista_carti = []
   lista_carti = create(lista_carti, 1, 'titlu1', 'gen1', 35, 'silver')
   lista_carti = create(lista_carti, 2, 'titlu2', 'gen2', 100, 'silver')
   lista_carti = create(lista_carti, 3, 'titlu3', 'gen1', 25, 'none')
   lista_carti = create(lista_carti, 4, 'titlu4', 'gen3', 75, 'gold')
   lista_carti = create(lista_carti, 5, 'titlu5', 'gen3', 23, 'none')
   lista_carti = create(lista_carti, 6, 'titlu6', 'gen2', 145, 'gold')
   lista_carti = create(lista_carti, 7, 'titlu7', 'gen4', 20, 'none')
   run_ui2(lista_carti)



test_modificare_gen()
test_determinare_pret_minim()
test_reducere()
test_crud()
main()