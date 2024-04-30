#!/usr/bin/python
import argparse
import csv
from unittest import result
import pandas as pd
import requests


DOCUMENTATION = '''
---
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
'''

EXAMPLES = '''
- name: Buscando informações do Pikachu e gravando em /tmp/Pokemon.csv
  pokedex:
    pokemon_name: pikachu
    csv_folder_path: /temp/

- name: Obtendo os 10 pokemon da API e gravando em /var/lib/Pokemon.csv
  pokedex:
    poke10: True
    csv_folder_path: /var/lib/



'''

RETURN = '''
original_state:
    description: The original state of the param that was passed in
    type: str
changed_state:
    description: The output state that the module generates
    type: str
'''


# functions devem vir aqui


def getAbilities(pokemondata):
    ability_list = []
    abilities = pokemondata['abilities']       
    for ability in abilities:
        ability_list.append(ability['ability']['name'])
    return ability_list


def getType(pokemondata):
    type_list = []
    types = pokemondata['types']       
    for type in types:
        type_list.append(type['type']['name'])

    
    return type_list


def getPokemons(inputs):
    
    if str(inputs) == "True":
        request = requests.get("https://pokeapi.co/api/v2/pokemon?limit=10&offset=0")
        
    else:
        
        request = requests.get("https://pokeapi.co/api/v2/pokemon/{}".format(inputs.lower()))
        if request.status_code == 404:   
            result['changed'] = False
            result['message'] = "failed: ESTE POKEMON NAO EXISTE"
            raise ValueError("Pokemon não Encontrado")         

    json_response = request.json()

    return json_response


def defineInputs(**kwargs):
    

    if kwargs['poke10'] and kwargs['pokemon_name'] == 'False':
        return True
    else:
        return kwargs['pokemon_name']




from ansible.module_utils.basic import AnsibleModule


def main():
    

    # Manage the parameters
    module = AnsibleModule(
        argument_spec=dict(
            pokemon_name=dict(type="str", default=False),
            poke10=dict(type="bool", default=False, choices=[True, False]),
            csv_folder_path=dict(type="str", default="/tmp/"),
        ),
        required_if=([("pokemon_name", "False", ["poke10"])]),
    )

    # Manage the result, assume no changes
   
    result = dict(
        changed=False,
        original_message='',
        message=''
    )

    pokemon_name = module.params['pokemon_name']

    inputs = defineInputs(**module.params)


    filename = module.params['csv_folder_path'] + 'Pokemons.csv'
   
    f = open(filename, "w+")
    f.close()

    pokemondata = getPokemons(inputs)
    headerList = ['Name', 'Ability', 'Type']
    with open(filename, 'a', newline="") as file:
        dw = csv.DictWriter(file, delimiter=',', fieldnames=headerList)
        dw.writeheader()
    
    if str(inputs) == "True":
        for pokemon in pokemondata['results']:
            request = requests.get(pokemon['url'])
            json_response = request.json()

            ability_list = ' '.join(getAbilities(json_response))
            type_list =  ' '.join(getType(json_response))


            csv_data = [pokemon['name'] + ',' + ability_list + ',' + type_list]

            with open(filename, 'a', newline="") as file:
                csvwriter = csv.writer(file, quoting=csv.QUOTE_NONE, escapechar=' ')
                csvwriter.writerow(csv_data)
          
    else:
            ability_list = ' '.join(getAbilities(pokemondata))
            type_list =  ' '.join(getType(pokemondata))

            csv_data = [inputs.lower() + ',' + ability_list + ',' + type_list]        

            with open(filename, 'a', newline="") as file:
                csvwriter = csv.writer(file, quoting=csv.QUOTE_NONE, escapechar=' ')
                csvwriter.writerow(csv_data)

    data = pd.read_csv(filename)
    data.sort_values("Ability", axis=0, ascending=[True], inplace=True)


    
    data.to_csv(filename, index=False)

    result['changed'] = True
    result['message'] = "success"
    # exit with change state indicated
    module.exit_json(**result)


if __name__ == "__main__":
    main()