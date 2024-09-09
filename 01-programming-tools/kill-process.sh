#!/bin/bash

# Verifica se o nome do processo foi fornecido como argumento
if [ -z "$1" ]; then
  echo "Uso: $0 <nome_do_executavel>"
  exit 1
fi

# Encontra o PID do processo com base no nome
pid=$(ps aux | grep "[${1:0:1}]${1:1}" | head -n 1 | awk '{print $2}')
command=$(ps aux | grep "[${1:0:1}]${1:1}" | head -n 1 | awk '{for (i=11; i<=NF; i++) printf $i " "; print ""}')

# Verifica se o processo foi encontrado
if [ -z "$pid" ]; then
  echo "Processo '$1' não encontrado."
  exit 1
fi

echo "Process found: PID-$pid  command-$command "

# Mata o processo encontrado
kill -9 $pid

# Confirma que o processo foi morto
if [ $? -eq 0 ]; then
  echo "Processo '$1' (PID $pid) foi terminado."
else
  echo "Falha ao matar o processo '$1'."
fi
