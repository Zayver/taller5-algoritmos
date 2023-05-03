# Taller No. 5
## Solución de un sudoku con 2 algoritmos
## Autores
- Santiago Zúñiga
- Mauren Ribera

# Ejecución

```sh
$ python main.py [filename] [(optional) generator?]
```
Donde 'generator' es simplemente un flag para usar las corrutinas de python para que el kernel no mate el proceso que seguramente saturará la memoria al intentar subir todas las permutaciones al mismo tiempo a ram. Si se indica, se usan los generators de python para realizar 'lazy-loading'.
El algoritmo de fuerza bruta fallará a los 1000 intentos para no hacer necesario la modificación del codigo.

## Dependencias

- python 3.x
