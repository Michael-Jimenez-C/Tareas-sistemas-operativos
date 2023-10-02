# Problema

Crear un cajero que atiende como maximo 5 solicitudes por cliente si se pasa el cliente debe devolverse al final de la cola, el cajero se define como una lista ciclica, se debe poder añadir usuarios y se debe poder visualizar su posición en la cola.

# Solucion
## información del cliente
El cliente es un objeto tipo diccionario que tiene nombre, apellido, y numero de solicitures.
## Lista
La lista se puede realizar mediante el elemento list de python, pues no tiene conflicto al incluirse a si mismo dentro de la lista, aunque otra alternativa es construir un nodo desde cero, en cuyo caso no es significativamente complicado