
## me leva junto com voce


# Pokedex
Desafio para C6 bank

# Sobre
Este e um projeto destinado a comprir o desafio C6 bank. 

Para resolução do desafio serão feitas 3 abordagens.

1. Python - Command line
2. Bash
3. Ansible


# O desafio

## Criar  um código (em qualquer linguagem) para consumir a APi resfull:  https://pokeapi.co/
 
### Esse código deve retornar a penas  os dez primeiros Pokémon, ordenado por habilidade. 
O Resultado deve apresentar:

- **Nome**
- **Habilidade**
- **Tipo**


### Deve ser possível informar um nome de pokemon para consulta, e o resultado deve trazer os mesmo  campos informados acima.

`Caso não encontre o Pokémon, é necessário um tratamento para informar isso ao usuário.`

 
### O resultado deve ser enviado para um .CSV, e o projeto deve ser salvo no git.

 
# APIs utilizadas

https://pokeapi.co/api/v2/pokemon?limit=10&offset=0

https://pokeapi.co/api/v2/pokemon/{id or name}/



# Implementação python

## WORKLOG
[TODOLIST](Python/TODOLIST.MD)

[CHANGELOG](Python/CHANGELOG.MD)

## Dependencias

As dependecia estão no arquivo [requirements.txt](Python/requirements.txt)

## Como usar

Acesse o diretorio Python e execute o arquivo main.py

Exemplos:
```Bash
# o script vai solicitar o nome do pokemon para o user
python3 main.py
```
```Bash
# passando o nome do pokemon como argumento
python3 main.py -pokemon=pikachu
```
```Bash
# Forçando o script a obter os 10 pokemons
python3 main.py -poke10=true
```
Durante a execução sera pedido o nome de um pokemon como input.
Caso o usuario não informe o nome de um pokemon o script buscara 10 pokemons na api `pokeapi.co`

Em seguida o script obtera o nome, habilidades e tipo do pokemon e fará a inserção ordenada por habilidade no arquivo `Pokemon.csv`

Exemplo Pokemon.csv:
```csv
Name,Ability,Type
charmander ,blaze  solar-power ,fire
charmeleon ,blaze  solar-power ,fire
charizard ,blaze  solar-power ,fire  flying
bulbasaur ,overgrow  chlorophyll ,grass  poison
ivysaur ,overgrow  chlorophyll ,grass  poison
venusaur ,overgrow  chlorophyll ,grass  poison
caterpie ,shield-dust  run-away ,bug
squirtle ,torrent  rain-dish ,water
wartortle ,torrent  rain-dish ,water
blastoise ,torrent  rain-dish ,water

```
# Implementação bash

## Dependencias

- curl
- jq

## Problemas na implementação
O loop "while read" não permite que as variaveis dentro dele sejam exportadas para uso externo.

Por esse motivo essa implementação ficou incompleta. até que eu encontre uma solução para essa limitação do bash



# Implementação Ansible

## Dependencias

- ansible
- pandas
- requests 
- argparse

## como usar

Acesse o diretorio Ansible e execute o Playbook

Exemplo:
```bash
ansible-playbook -i inventory site.yml 
```

Durante a execução o Ansible vai buscar dados do pokemon Pikachu e outros 10 pokemons na API `pokeapi.co`, para inserir e um arquivo .csv e ordenar por habilidade.
Os dados que serão coletados são nome, Habilidade e tipo.


Exemplo Pokemon.csv:
```csv
Name,Ability,Type
charmander ,blaze  solar-power ,fire
charmeleon ,blaze  solar-power ,fire
charizard ,blaze  solar-power ,fire  flying
bulbasaur ,overgrow  chlorophyll ,grass  poison
ivysaur ,overgrow  chlorophyll ,grass  poison
venusaur ,overgrow  chlorophyll ,grass  poison
caterpie ,shield-dust  run-away ,bug
squirtle ,torrent  rain-dish ,water
wartortle ,torrent  rain-dish ,water
blastoise ,torrent  rain-dish ,water

```

Obs: os arquivos serão armazenados em /tmp/
