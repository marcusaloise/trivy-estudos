
Projeto voltado para observabilidade.
===
Repositório voltado para projetos de infraestrutura e observabilidade


# Início de tudo

### A ideia inicial do projeto era apenas ter, neste repositório, os arquivos .tf

### Onde seria configurada uma VPC que contém uma subnet, security group, tabela de roteamento, Internet Gateway e uma EC2.

### Então, assim que postei a ideia do projeto no LinkedIn, pensei: "Por que não fazer algo a mais?" E me surgiu a ideia de subir o Zabbix usando o Ansible.


# Parte 2

### A segunda parte desse projeto foi justamente: "Como vou subir o zabbix usando o ansible?" Logo de início, fui pesquisar a documentação oficial do Zabbix e vi que era algo simples de se fazer, basicamente foi só copiar e colar os comandos que são disponibilizados no site para módulos Ansible. Demorei umas 2 horas para fazer esse "copiar e colar", porque fazia muito tempo que não usava o Ansible em si.

### Depois desse tempo, refinei o código pensando no que faltava. Aí me liguei que, por padrão, não vem configurado o MySQL no servidor que estava subindo. A partir disso, corri atrás de como vou instalar e configurar o MySQL para o zabbix? Depois de muitas horas de pesquisa, tentativas e erros, eu consegui fazer uma role que instala e configura o MySQL.


# Como usar ?

### Entende-se que na sua máquina já tenha configurado o aws-cli e tenha uma chave ssh cadastrada na aws. Siga os passos abaixo:

**Entre no diretorio** [infratf](./infratf/)

### De início, é preciso criar a nossa infraestrutura na AWS. Podemos utilizar o comando a seguir para subir a infra citada acima:

```Bash
# Exemplo de comando para executar o .tf

$ terraform apply --auto-approve 

# Particulamente gosto de usar o argumento --auto-approve
```

**Após a criação da infraestrutura, serão apresentados no terminal os IPs privados e públicos como no exemplo abaixo:**

```Bash

Apply complete! Resources: 8 added, 0 changed, 0 destroyed.

Outputs:

ip_privado = "10.0.1.143" # Apenas um exemplo!
ip_publico = "54.210.43.205" # Apenas um exemplo!


```
### Após isso, copie o IP público e cole no arquivo [hosts.yml](./infratf/Ansible/hosts.yml)

**Exemplo:**

```yml

[ec2-user]
54.210.43.205

```

### Com o arquivo [Hosts](./infratf/Ansible/hosts.yml) "configurado", está na hora de rodar o nosso [playbook.yml](./infratf/Ansible/playbook.yml).

**Exemplo:**

```bash

$  ansible-playbook playbook.yml -u ec2-user --private-key id_rsa.pem -i hosts.yml 

# Os argumentos utlizados acima são:
# -u de usuario que por padrão vamos usar o ec2-user
# --private-key a chave privada cadastrada na criação da ec2
# -i aponta o arquivo hosts.yml mostrando o ip dos servidores que vão ser afetados pelo playbook

```
### De final e jogar o ip publico da nossa maquina no navegador "54.210.43.205/zabbix" e fazer a configuração inicial do zabbix