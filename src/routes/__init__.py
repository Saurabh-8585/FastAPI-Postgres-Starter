from src.db.connnection import get_session


def get_db():
    """
    does
    :return:
    """
    db = get_session()

    try:
        yield db
    finally:
        db.close()


def get_raw_db():
    """
    does
    :return:
    """
    from src.db.connnection import engine

    db = engine.raw_connection()
    try:
        # logging.debug("yeilding db")
        yield db
    finally:
        # logging.debug("closing db")
        db.close()
