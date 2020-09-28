Steps for fresh install on new PC:
    Install dependencies one by one via.

1. `docker-compose down -v && docker-compose build && docker-compose up -d && docker-compose logs -f app` to boot the app.
2. In a new terminal run `dc exec app bash` to get into the app.
3. Then hit the app in the browser at.
   `http://localhost:5000/`
4. `pipenv install <missing-package>`
5. Repeat steps 3-4 until the app boots perfectly.

If you have previously run this docker container:
1. `docker-compose down -v --remove-orphans`

Now you will have a minimal list of dependencies and version locking!
