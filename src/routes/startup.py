from src.db.connnection import connect_db
from time import sleep
from loguru import logger

DB_CONNECTION_RETRY_TIME = 5
REDIS_CONNECTION_RETRY_TIME = 5
RETRY_ERROR_FOR_CRITICAL_LOGS = 2


def init_all():
    """
    This function will be called on startup of the application
    :return:
    """
    init_db()


def init_db():
    """
    This function will be called on startup of the application to initialize the db connection
    :return:
    """
    connection_attempt = 0

    while True:
        logger.info(f"PSQL DB Connection Attempt: {connection_attempt}")

        try:
            status = connect_db()
            if status:
                logger.info(f"PSQL DB Connected at attempt: {connection_attempt}")
                break

        except Exception as e:
            if connection_attempt > RETRY_ERROR_FOR_CRITICAL_LOGS:
                logger.critical(f"PSQL DB Connection Error : {e}")
            else:
                logger.info(f"PSQL DB Connection Error : {e}")

            sleep(DB_CONNECTION_RETRY_TIME)
            connection_attempt += 1
        finally:
            pass
