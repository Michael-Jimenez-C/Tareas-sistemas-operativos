#!/bin/bash

# Crea un array vacío para almacenar los números primos
primos=()

# Inicializa el bucle for para iterar sobre los números del 2 al 100
for n in $(seq 2 100); do

  # Comprueba si n es divisible por cualquier número menor que él mismo
  for i in $(seq 2 $((n - 1))); do

    # Si n es divisible por i, no es primo
    if (( n % i == 0 )); then
      break
    fi
  done

  # Si n no es divisible por ningún número menor que él mismo, es primo
  if (( i == n )); then

    # Añade n al array de números primos
    primos+=($n)
  fi
done

# Imprime los números primos
for primo in "${primos[@]}"; do
  echo "$primo"
done