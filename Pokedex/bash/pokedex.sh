#!/bin/bash
#set -x
# consultado a API para obter os 10 pokemons com seu nome, habilidade e tipo.
# Armazenando a resposta em uma variavel.

CSVPATH=/tmp/pokedex.csv
> $CSVPATH

POKEMONS=`curl -s --request GET 'https://pokeapi.co/api/v2/pokemon?limit=10&offset=0' | jq .results`

# Inicializando variavel para fazer apend das habilidades.


echo $POKEMONS | jq -c '.[]'  | while read i; do
# Obtendo o nome do pokemon e sua URL para obter mais detalhes sobre o pokemon.
# Removendo as aspas duplas da string.
#já inserindo o nome do pokemon no arquivo csv
echo " "
echo $i | jq .name | tr -d '"' | sed -e "s/$/;/"




POKEMON_URL=`echo $i | jq .url | tr -d '"'`

# POR INCRIVEL Q PARECA E MAIS PERFORMATICO CONSULTAR A API DUAS VEZES.
POKEMON_ABILITIES=`curl -s --request GET $POKEMON_URL | jq .abilities `
POKEMON_TYPES=`curl -s --request GET $POKEMON_URL | jq .types `


echo $POKEMON_ABILITIES | jq -c '.[]'  | while read habilidade; do
    
    HABILIDADES=`echo $habilidade | jq .ability.name | tr -d '"'`
    export OUTPUT_HABILIDADE+=`echo -n $HABILIDADES | sed -e "s/$/,/"`

    
echo $OUTPUT_HABILIDADE | sed -e "s/$/;/"
    
done


echo $POKEMON_TYPES | jq -c '.[]'  | while read tipo; do
    
    TIPOS=`echo $tipo | jq .type.name | tr -d '"'`
    export OUTPUT_TIPOS+=`echo -n $TIPOS | sed -e "s/$/,/"`

   
echo $OUTPUT_TIPOS
done


#echo $POKEMON_ABILITIES | jq
#echo $POKEMON_TYPES


#echo "$POKEMON_NAME;$HABILIDADES"
#echo $POKEMON_URL
done


