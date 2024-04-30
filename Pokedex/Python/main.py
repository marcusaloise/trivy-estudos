#!/bin/python3
from curses import def_prog_mode
import string
import requests
import json
import csv
import pandas as pd
import argparse


filename = 'Pokemons.csv'
csv_data = [] #[['bulbasaur', 'overgrow, chlorophyll', 'grass, poison']]

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
            
            raise ValueError("Pokemon não Encontrado")         

    json_response = request.json()

    return json_response

def main(inputs):


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

    data = pd.read_csv("Pokemons.csv")
    data.sort_values("Ability", axis=0, ascending=[True], inplace=True)


    
    data.to_csv("Pokemons.csv", index=False)

def parseArguments():

    parser = argparse.ArgumentParser()

    parser.add_argument("-pokemon", help="Nome do Pokemon", default=False)
    parser.add_argument("-poke10", help="Obter 10 Pokemons", default=False, type=bool)


    args = parser.parse_args()

    return args


def defineInputs(**kwargs):
    
    if not kwargs['pokemon'] and not kwargs['poke10']:
        qual_pokemon = input ('Informe o nome do pokemon para pesquisa ou aperte enter para obter 10 pokemons.')
        if not qual_pokemon:
            return True    
        else:    
            return qual_pokemon
    if kwargs['pokemon']:
        return kwargs['pokemon']
    else:
        return kwargs['poke10']
        


if __name__ == '__main__':

    args = parseArguments()
    inputs = defineInputs(**args.__dict__)
    

    main(inputs)
    
## Muda a , para ;

# text = open("Pokemons.csv", "r")
# text = ''.join([i for i in text]) 
# text = text.replace(",", ";") 
# x = open("Pokemons.csv","w")
# x.writelines(text)