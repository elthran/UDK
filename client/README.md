# Undying Kingdoms - UI Client

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

### Install a New Package

```
docker-compose up -d
# e.g.
docker-compose exec app yarn add lodash
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
