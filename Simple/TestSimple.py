from random import randint

def Ordenador(lista = []):
    intercambiar = True
    while intercambiar:
        intercambiar = False
        for i in range(len(lista) - 1):
            if lista[i]['edad'] > lista[i + 1]['edad']:
                lista[i]['edad'], lista[i + 1]['edad'] = lista[i + 1]['edad'], lista[i]['edad']
                intercambiar = True
                
def GeneradorDiccionarios():
    Lista = []
    for i in range(10):
        Lista.insert(i,{
                    'id': i,
                    'edad': randint(1, 100)
                    })
    Ordenador(Lista)
    return Lista
print(GeneradorDiccionarios())
