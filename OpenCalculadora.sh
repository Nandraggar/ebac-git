#!/bin/bash
# Script para executar a calculadora em python
# Captura o nome do usuário
read -p "Digite o seu nome: " nome
echo "Seja bem vindo, $nome"
# Definindo o caminho do executável
calc_dir="$HOME/Documentos/Projetos/Ebac/Calculadora/calculadora.py"
# Verifica se o arquivo existe
if [ -f "$calc_dir" ]; then
     python3 "$calc_dir" # Executa o arquivo caso exista
else
    echo "Erro: Arquivo não encontrado em $calc_dir" #Sai da execução em caso de erro.
    exit 1
fi
