import psycopg2
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class PostgresDb:
    def __init__(self, psql_config):

        try:
            self.connection = psycopg2.connect(
                database=psql_config.POSTGRES_DB,
                host=psql_config.POSTGRES_HOST,
                port=psql_config.POSTGRES_PORT,
                user=psql_config.POSTGRES_USER,
                password=psql_config.POSTGRES_PASSWORD
            )

        except psycopg2.OperationalError as exception:
            logger.error("ERROR: Error connecting to the database")
            logger.error(exception)

    def save_many(self, query: bytes, data: tuple) -> None:
        try:
            cursor = self.connection.cursor()

            query += b','.join(cursor.mogrify("(%s, %s, %s, %s)", x) for x in data)
            cursor.execute(query, data)

            self.connection.commit()

        except Exception as exception:
            logger.error("Inserting data in transactions table")
            logger.error(exception)
            self.connection.rollback()

    def save(self, query: str, data: tuple) -> tuple:
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, data)
            self.connection.commit()

            return cursor.fetchone()

        except Exception as exception:
            logger.error("Error while save data from PostgreSQL")
            logger.error(exception)

    def get(self, query: str) -> tuple:
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)

            return cursor.fetchone()

        except Exception as exception:
            logger.error("Error while fetching data from PostgreSQL")
            logger.error(exception)
