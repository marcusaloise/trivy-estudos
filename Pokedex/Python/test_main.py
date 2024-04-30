#!/bin/python3
import unittest
import json
from requests import get
from main import getAbilities
from main import getType
from main import getPokemons
from main import main
from csvvalidator import * 
import pathlib as pl
import pandas as pd

data = json.load(open('pikachu.json'))
data2 = open('Pokemons.csv')

class TestPokedex(unittest.TestCase):
    # Teste do getPokemon
    def test_getPokemon(self):
        self.assertRaises(ValueError, getPokemons, "marcus")
        teste_getPokemon = getPokemons("Pikachu")
        if "abilities" in teste_getPokemon:
            ability_key = True
        else:
            ability_key = False

        if "types" in teste_getPokemon:
            type_key = True
        else:
            type_key = False

        

        self.assertEqual(ability_key, True, "A chave ability não existe")
        self.assertEqual(type_key, True, "A chave type não existe")

    # Teste do GetType
    def test_getType(self):
        get_type = getType(data)
        self.assertIsInstance(get_type, list, "A função getType não retornou uma lista")
          
    # Teste do GetAbilities
    def test_getAbilities(self):
        get_abilities = getAbilities(data)
        self.assertIsInstance(get_abilities, list, "A função getType não retornou uma lista")
        

    # Veficando se o arquivo csv e criado
    def testCsv(self):
        main('ditto')


        def assertIsFile(self, path):
            if not pl.Path(path).resolve().is_file():
                raise AssertionError("O arquivo não existe: %s" % str(path))


        def test(self):
            path = pl.Path("Pokemons.csv")
            self.assertIsFile(path)

        csv_data = pd.read_csv("Pokemons.csv")
    
    def testeColumnName(self):
        csv_data = pd.read_csv("Pokemons.csv")

        if 'Name' in csv_data:
            column_name = True
        else:
            column_name = False
        
        
        self.assertEqual(column_name, True, "A coluna name não existe no csv")    
        
    def testeColumnAbility(self):
        csv_data = pd.read_csv("Pokemons.csv")

        if 'Ability' in csv_data:
            column_ability = True
        else:
            column_ability = False

        self.assertEqual(column_ability, True, "A coluna ability não existe no csv")

    def testeColumnType(self):
        csv_data = pd.read_csv("Pokemons.csv")

        if 'Type' in csv_data:
            column_type = True
        else:
            column_type = False
        
        
        
        self.assertEqual(column_type, True, "A coluna type não existe no csv")
       