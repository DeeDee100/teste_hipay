
# Desafio Shipay


## Como rodar o projeto localmente
 É necesário ter Python e o Docker instalado na máquina caso não tenha é possível obté-los na página de [download do Python](https://www.python.org/downloads/) e na página de [instruçoes do Docker](https://docs.docker.com/get-docker/) 

1. Clone o repositório:
```bash
    git clone https://github.com/shipay-pag/backend-challenge.git
```
2. Navegue até a pasta api/
3. Dentro da pasta, basta rodar o comando abaixo para iniciar localmente a API

```bash
    docker compose up
```
4. Abra seu navegador e no espaço de URL e digite para acessar as docs: ``` http://localhost:8000/docs#/```.


## Como realizar deploy do projeto 

Utilizando Github Actions, no arquivo yml de configuração do workflow é necessário criar uma ação dentro do step adequado para rodar o comando ```docker compose up`` .

Exemplo:

```yml
steps:
- name: Check Code
  uses: actions/checkout@v3
- name: Setup project
  run: docker compose up
```


---
<img src="https://img.shields.io/badge/Made%20with-python-1f425f.svg" />