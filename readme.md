
# Shipay Back-end Challenge


## Lista de conteúdos:

- [Questão 1](#questão-1)
- [Questão 2](#questão-2)
- [Questão 3](#questão-3)
- [Questão 4](#questão-4)
- [Questão 5](#questão-5)
- [Questão 6](#questão-6)
- [Questão 7](#questão-7)
- [Questão 8](#questão-8)

# Questão 1
A resposta para essa questão pode ser encontrada abaixo e no arquivo ```questao_1.sql```
```SQL
select usr.name, usr.email, cl.description as claims, rl.description as role from users usr, claims cl, roles rl, user_claims uc
where usr.id = uc.user_id 
and cl.id = uc.claim_id
and rl.id = usr.role_id;
```
# Questão 2
A resposta para essa questão pode ser encontrada abaixo e no arquivo ```api/app/routes/users.py``` ou no endpoint ``` localhost/users/roles```

```python
results = session.query(
    user.name,
    user.email,
    claims.description.label('claims'),
    roles.description.label('role')
).join(user_claims, user.id == user_claims.user_id
).join(claims, claims.id == user_claims.claim_id
).join(roles, roles.id == user.role_id
).all()
```

# Questão 3
A resposta para a questão pode ser encontrada no arquivo ```api/app/routes/users.py``` ou no endpoint ``` localhost/users/```
# Questão 4
A resposta para a questão pode ser encontrada no arquivo ```api/app/routes/users.py``` ou no endpoint ``` localhost/users/```
# Questão 5
O arquivo de README.md foi criado dentro do diretório ``` api/README.md``` com instruções de como rodar o projeto.
# Questão 6
Diante da stacktrace apresentada a provável causa de erro é a falta de uma variável chamada WALLET_X_TOKEN_MAX_AGE dentro do arquivo core.settings
# Questão 7

Melhorias sugeridas:
 
    * Criar variáveis de ambiente em um arquivo .env para valores hardcoded do código, como por exemplo a conexao com o banco de dados
    * Adicionar tratamento de erros quando tentar ler a variável no arquivo de configuração
    * Variável  "var1" com conme genérico, colocar um nome mais decritivo
    * Trocar nome da função "task1" para um nome que seja mais legivel e seja fácil de entender o que a função faz
    * Dentro de task1, pense em fazer a query pela orm do SQLAlchemy ao invés de usar SQL direto no código
    * Usar o logger para informações ao invés de print
    * Adicionar tratamento de erro para o export em excel 
    * Adicionar documentação 
    * Adicionar testes 
    * Adicinar uma função responsável apenas para o logging
    * Quebrar a função task1 em mais de uma para que cada uma tenha uma única função 

# Questão 8
Diante do problema proposto, utilizaria o Adapter Pattern ou padrão adaptador pois é um padrão utilizado para converter uma interface de uma classe em outra interface que o cliente espera receber.
Isso se torna muito útil quando lidamos com vários provedores de email e podemos criar uma classe EmailService por exemplo com uma função de enviar email(sendEmail) e criar adapdatores específicos para cada provedor que implemente sua própria versão do "sendEmail".
