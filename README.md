Steps for fresh install on new Windows PC:

1. Install docker-compose for Windows: https://docs.docker.com/docker-for-windows/install/
2. `docker-compose down -v && docker-compose build && docker-compose up -d && docker-compose logs -f app` to boot the app.
3. The container is running. Visit localhost:5000 to play the game.

Steps for fresh install on Linux PC:

1. Install docker-compose for Ubuntu: https://docs.docker.com/compose/install/
2. `docker-compose down -v && docker-compose build && docker-compose up -d && docker-compose logs -f app` to boot the app.
3. The container is running. Visit http://0.0.0.0:5000/ to play the game.

