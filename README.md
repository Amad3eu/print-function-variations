# Variações da função print
- Respondido na atividade proposta por meio de um um forum
- Foi desenvolvido dois seguintes exemplos:

1. **Epoch time - demonstração:**

 - Importei o módulo time.
 - Usei **time.time()** para obter o tempo atual em segundos desde o **epoch (1º de janeiro de 1970)**.
 - Converti o tempo para um número inteiro para uma representação mais simples.
 - Exibi o tempo do epoch usando _print_.

   **Exemplo:**

   ```python
   import time

   epoch_time = int(time.time())
   print("Tempo do epoch:", epoch_time)

   ```

2. **ASCII art do tux do linux :)) - demonstração:**

 - Crei uma string multi-linha contendo o [ASCII art do Tux](http://www.ascii-art.de/ascii/jkl/linux.txt).
 - Usei a notação **r"""...""" para indicar uma string raw**, o que evita que caracteres especiais sejam interpretados.
 - Exibi o ASCII art do Tux usando _print_.

    **Exemplo:**
  
    ```python
    tux_art = r"""
  
                     .88888888:.
                    88888888.88888.
                  .8888888888888888.
                  888888888888888888
                  88' _`88'_  `88888
                  88 88 88 88  88888
                  88_88_::_88_:88888
                  88:::,::,:::::8888
                  88`:::::::::'`8888
                 .88  `::::'    8:88.
                8888            `8:888.
              .8888'             `888888.
             .8888:..  .::.  ...:'8888888:.
            .8888.'     :'     `'::`88:88888
           .8888        '         `.888:8888.
          888:8         .           888:88888
        .888:88        .:           888:88888:
        8888888.       ::           88:888888
        `.::.888.      ::          .88888888
       .::::::.888.    ::         :::`8888'.:.
      ::::::::::.888   '         .::::::::::::
      ::::::::::::.8    '      .:8::::::::::::.
     .::::::::::::::.        .:888:::::::::::::
     :::::::::::::::88:.__..:88888:::::::::::'
      `'.:::::::::::88888888888.88:::::::::'
    miK     `':::_:' -- '' -'-' `':_::::'`
    
    """
    print("ASCII Art do Tux:")
    print(tux_art)
  
  ```
