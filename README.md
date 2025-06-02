# weather_db_dbmate

To view this project locally:

### `git clone git@github.com:AvrilMaleham/weather_db_dbmate.git`

Clone the app into the directory of your choice.

Make sure **Docker** is installed locally.

### `docker compose up --build`

Sets up one Docker container for the DB one for the API, and one to run dbmate.

Open [http://localhost:8000/docs](http://localhost:8000/docs) to view the Swagger docs in the browser.

### `docker exec -it weather_db_dbmate-db-1 psql -U postgres -d weatherdb`

Programatically access the DB.

### `docker compose run --rm dbmate new <table_name>`

Create a new migration file.

# Key project skills:

- Dbmate
- Docker
- FastAPI
- DB Design
- Migration Scripts
- API Integration
