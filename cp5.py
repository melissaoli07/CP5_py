#melissa de oliveira pecoraro rm98698

import time

def obter_tempo():
    inicio = time.time()
    for i in range(1000000):
        print (f'i: {i}')
    fim = time.time()
    return fim-inicio

#principal
print(f'tempo de execução: {obter_tempo()}')