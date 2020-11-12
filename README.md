# Steps for fresh install:

1. Install docker-compose 
   - for Windows: https://docs.docker.com/docker-for-windows/install/
   - for Ubuntu: https://docs.docker.com/compose/install/
2. `docker-compose down -v && docker-compose build && docker-compose up -d && docker-compose logs -f` to boot the app. 
> Mostly you will just use `docker-compose down && docker-compose up -d && docker compose logs -f [app|client]`
3. Once the container is running visit http://localhost:5000/ to play the old version of the game.
4. Visit http://localhost:8080/ for the new Vue version of the game.

# General Help
- http://localhost:8080/ping to test if front/back-end is linked and running correctly

- For front-end routes see [client/src/routes.js](client/src/routes.js) e.g. http://localhost:8080/county/home
- For back-end routes see [app/api/routes.py](app/api/routes.py) e.g. http://localhost:5000/api/counties/1
- Install a new package
```bash
docker-compose up -d
# e.g. for back-end packages
docker-compose exec app pipenv install flask-restful
# e.g. for front-end packages
docker-compose exec client yarn add lodash
```

Basic Debug Commands:
Advance day (take your turn): http://localhost:5000/debug/advance_day
Buy Soldier: http://localhost:5000/debug/buy_footman
Buy Archer: http://localhost:5000/debug/buy_archer
