# AthleteAPI

O projeto é uma API REST para utilização de dados de atletas que participaram de olimpiadas.
Os dados utilizados para desenvolver este projeto podem ser encontrados no seguinte link https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results#athlete_events.csv

## Instalação

Para incializar o projeto é necessário ter uma versão do python 3 instalada.

*Com o python instalado recomenda-se a criar uma virtualenv para instalação das dependencias do projeto.*

Para instalar essas dependencias você deve rodar o seguinte comando na pasta raiz do projeto

```sh
pip install -r requirements.txt
```
Este comando instala no seu *environment* todas as dependencias do projeto

Com as dependencias instaladas você deve configurar o seu banco de dados `DATABASES` no arquivo settings.py.

```
DATABASES = {
    'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'athlete',
                'USER': 'Arthur',
                'PASSWORD': 'abc123',
                'HOST': '127.0.0.1',
                'PORT': '3307'
            }
}
```

*Configurar esta variável não irá criar o banco de dados automaticamente. Ele deve já estar acessivel pelo endereço e pelo usuário indicado*

Após a configuração do banco de dados deve-se rodar a *migrates* com a seguinte linha de comando

```sh
python manage.py migrate
```

Este comando irá criar as tabelas utilizadas no projeto

Com as migrates feitas o projeto está pronto para ser incializado com o comando

```sh
python manage.py runserver
```
Para popular o banco de dados com os dados de exemplo é necessário rodar mais um comando. O importScript.py recebe duas váriaveis sendo elas dois paths para arquivos `.csv` o primeiro para importação do arquivo noc_regions e o segundo para o arquivo athlete_events

```sh
python importScript.py noc_regions.csv athlete_events.csv
```

*Não é necessário que o servidor esteja rodando para a execução deste comando*


## Endpoints

Os endpoints são canais de comunicação da API. No caso deste projeto pode-se fazer 4 tipos de requisições para cada um deles `GET` `POST` `PUT` e `DELETE`, totalizando 5 para cada endpoint já que eles podem receber dois tipos de requisição `GET`.

Os endpoints disponiveis são :

1. NOC
2. Athlete
3. Event
4. Sport
5. City
6. Olympics
7. Participation

Para testar o acesso aos endpoints você pode acessar pelo seu browser a interface padrão do DRF e fazer requisições por lá.
Para isso basta acessar o host do seu servidor. Exemplo :
```
http://SeuHost:8000/Athlete/
```
*Para mexer na páginação utilizada pela API deve utilizar os parametros `page` e `page_size`*

Este link vai apresentar uma página com uma lista de atletas cadastrados no sistema. Para acessar um atleta em especifico e realizar requisições especifica a ele basta acessar esse link adicionando o id dele no final. Exemplo :
```
http://SeuHost:8000/Athlete/2222
```

Para realizar ações como `POST` e `PUT` os atributos devem ser enviados no corpo da requisição.

### Filtro e ordenação nas listagens

A filtragem utiliza-da no projeto é feita como as querysets feitas nos modelos do Django. Você pode acessar atributos dos modelos relacionados para realizar uma filtragem. Isso complica as requisições necessárias mas abre um leque de possibilidades para as filtragens.

Para realizar filtros nas listagens deve-se enviar parametros na requisição (query_params)

Para testar um filtro facilmente você pode adicionar no final de uma endpoint as váriaveis que você deseja filtrar.
```
http://SeuHost:8000/Athlete/?name=Arthur
```
*É póssivel utilizar variações nos filtros de texto como `_like`, que faz a query retornar coisas que contenham a sua váriavel na String, e `ilike` que faz a mesma função do outro mas não leva em consideração letras maiusculas*

*Para atributos numéricos essas variações são diferentes. Aas dispóniveis são : `_gt`,`_gte`,`_lt`,`_lte`*

Para filtrar por um atributo de um modeo relacionado você deve utilizar duas undelines `__ `.

```
http://SeuHost:8000/Athlete/?name_like=Arthur&noc__noc=BRA
```

A ordenação utiliza-se do parametro `order_by`, para ordenar por mais de um atributo basta separar o nome dos atributos por uma virgula `,` e para inverter a ordem, ou seja utilizar a ordem decrescente, adicione um meno `-` antes do nome do atributo

```
http://SeuHost:8000/Athlete/?name_like=Arthur&noc__noc=BRA&order_by=height,-weight
```
