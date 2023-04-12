from random import randint

def Ordenador(lista = []):
    listaOrdenada = sorted(lista, key=lambda x: x["edad"], reverse=True)
    joven = listaOrdenada[-1]["id"]
    viejo = listaOrdenada[0]["id"]
    print(f"La persona más joven tiene id: {joven}")
    print(f"La persona más vieja tiene id: {viejo}")

    
                
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




