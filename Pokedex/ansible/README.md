# ansible_module_pokedex

Modulo Ansible que consulta a API Pokeapi.co e obtem informações de habilidade e tipo do pokemon informado, ou dos 10 pokemons que API informa por default, registrando tudo em um arquivo .csv ordenado pela habilidade do pokemon.

## Module info and inputs

```yml
module: pokedex
author:  Marcus Aloise
short_description: Consulta a API Pokeapi.co e obtem informações de habilidade e tipo do pokemon informado ou dos 10 pokemons que API informa por default, registrando tudo em um arquivo .csv
description:
    - Consulta a API Pokeapi.co e obtem informações de habilidade e tipo do pokemon informado ou dos 10 pokemons que API informa por default, registrando tudo em um arquivo .csv
options:
    pokemon_name:
        description:
            - O nome do pokemon que voce deseja para obter as habilidades e o tipo.
        required: False
        default: False
    poke10:
        description:
            - O usuario informa se deseja obter os 10 pokemons por default da API. Obrigatorio ser pokemon_name não for informado
        required: False
        choices: ['True', 'False']

    csv_folder_path:
        description:
            - Path da pasta onde o arquivo csv sera gerado. O nome do arquivo sera Pokemon.csv.
        required: False   
        default: /tmp/   

```

# Exemplos

```yml
- name: Buscando informações do Pikachu e gravando em /tmp/Pokemon.csv
  pokedex:
    pokemon_name: pikachu
    csv_folder_path: /temp/

- name: Obtendo os 10 pokemon da API e gravando em /var/lib/Pokemon.csv
  pokedex:
    poke10: True
    csv_folder_path: /var/lib/

```