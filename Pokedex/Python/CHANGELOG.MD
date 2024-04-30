# Changelog
Todas as mudanças realizadas nesse projeto devem ser colocadas aqui.

Seguir o padrão do [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
E preservar o versionamento semantico conforme [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [0.0.4] - 2022-05-25
### Added

- Foi criado a implementação ansible, mas ela não se encontra 100% funcional devido a um conflito no tratamento de erro.

## [0.0.3] - 2022-05-25
### Added
- Foi adicionado o teste se o arquivo .csv foi criado e se as colunas dentro dele estão corretas

## [0.0.2] - 2022-05-24
### Added
- usuario pode passar nome do pokemon ou ação "poke10" para obter os 10 pokemons, como argumentos por linha de comando

## [0.0.1] - 2022-05-24
### Added

- Readme, changelog, todolist
- Implementação da função getAbilities, getType, getPokemons
- Main recendo input do user e gerando arquivo .csv
- Testes unitarios test_getPokemon, test_getType, test_getAbilities.