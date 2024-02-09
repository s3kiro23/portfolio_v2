import os

from dotenv import load_dotenv


class Config():

    DEBUG = False
    SQLITE_PATH = '/opt/portfoliov2/db.sqlite3'
    LOG_ERROR_PATH = '/var/log/portfoliov2/error.log'

    IS_POSTGRESQL_BACKEND = True
    PG_DATABASE_ENGINE = 'django.db.backends.postgresql_psycopg2'
    PG_DATABASE_NAME = 'portfoliov2'
    PG_DATABASE_USER = 'portfoliov2'
    PG_DATABASE_PASSWORD = 'portfoliov2'
    PG_DATABASE_HOST = '172.17.0.1'
    PG_DATABASE_PORT = '5432'