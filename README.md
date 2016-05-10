# apoio-piratas
Pequeno projeto de apoio ao Partido Pirata

# Rodando com Docker ou Docker-compose

Para instalar o docker siga: 

Mac: https://docs.docker.com/mac/
Linux: https://docs.docker.com/linux/
Windows: https://docs.docker.com/windows/


## Docker only

```
$ docker build -t piratas/apoio .
$ docker run -d -p 8000:8000 piratas/apoio
```

Montando o diretorio para desenvolvimento:

```
$ docker run -d -p 8000:8000 -v $PWD/apoio:/app/apoio piratas/apoio
```

## Docker compose

```
$ docker-compose up -d
```

Acesse via: http://127.0.0.1:8000 ou http://192.168.99.100:8000






