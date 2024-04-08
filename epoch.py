
# - Importei o módulo time.
# - Usei time.time() para obter o tempo atual em segundos desde o epoch (1º de janeiro de 1970).
# - Converti o tempo para um número inteiro para uma representação mais simples.
# - Exibi o tempo do epoch usando print.

import time

epoch_time = int(time.time())
print("Tempo do epoch:", epoch_time)
