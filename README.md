# Book Suggestion

# Running the Project:
To run the project, you need to create a .env file in the project's root directory and enter the required values. (Instructions are provided below)

To run the project on your local system, follow these steps:
1. Create a file named `.env` in the root directory of the project.
2. Open the `.env` file and enter the necessary configuration values.

Next, open your terminal and enter the following command:

To build the database and Redis containers, run the following command:
```
docker-compose --file docker-compose-development.yml up -d
```

To deploy the project in a production environment, use the following command:
```
docker-compose up -d
```

## Setting Environment Variables

This project relies on environment variables to configure database, sms service settings etc. 

Create a `.env` file in the root directory and add the following(Value is a sample):

```
SECRET_KEY='django-insecure-hf9k^z=8a5j((f379d^7694sreo%c!wa%(%85(=bs$vcpl@(6^'

DEBUG=False

WEB_DOMAIN=localhost:8000
WEB_FRONT_DOMAIN=localhost:3000

DB_NAME=my_database
DB_USER=root
DB_PASS=mypassword
DB_PORT=5439
DB_HOST=myhost
DB_HOST_DEBUG=localhost

REDIS_HOST=redis_bio_host
REDIS_HOST_DEBUG=localhost
REDIS_PASSWORD=redis_bio_password
REDIS_PORT=6389

DJANGO_PORT=8000
```
