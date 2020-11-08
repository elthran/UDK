Steps for fresh install on new Windows PC:

1. Install docker-compose for Windows: https://docs.docker.com/docker-for-windows/install/
2. `docker-compose down && docker-compose build && docker-compose up -d && docker-compose logs -f` to boot the app.
3. The container is running. Visit localhost:5000 to play the game.

Steps for fresh install on Linux PC:

1. Install docker-compose for Ubuntu: https://docs.docker.com/compose/install/
2. `docker-compose down && docker-compose build && docker-compose up -d && docker-compose logs -f app` to boot the app.
3. The container is running. Visit http://0.0.0.0:5000/ to play the game.

To Run Vue
1. cd client/
2. `docker-compose down && docker-compose build && docker-compose up -d && docker-compose logs -f app`
3. Go to page http://localhost:8080/ping to see it



# Undying Kingdoms - UI

## Project setup

```
docker-compose build
```

### Compiles and hot-reloads for development

```
docker-compose up -d
# or
docker-compose run --rm app yarn serve
```

### Compiles and minifies for production

```
docker-compose run --rm app yarn build
```

### Run your tests

```
docker-compose run --rm app yarn test
```

### Lints and fixes files

```
docker-compose run --rm app yarn lint
```

### Customize configuration

See [Configuration Reference](https://cli.vuejs.org/config/).

