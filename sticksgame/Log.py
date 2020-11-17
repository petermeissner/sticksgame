import sqlalchemy

class Log:
    """
    Class to collect key value entries (aka dict) into a list. 
    """

    d   = None
    log = None

    def __init__(self, **kwargs):
        self.d = dict(kwargs)
        self.log = []

    def append(self, log: dict):
        self.log.append({**self.d, **log})


class Log_db(Log):
    """
    Class to collect key value entries (aka dict) into a list and log them to a database too.
    """

    d   = None
    log = None
    sql = None

    def __init__(self, log_db, **kwargs):
        self.sql = sqlalchemy.create_engine('sqlite:///game.db', echo=True)
        self.d   = dict(kwargs)
        self.log = []

    def append(self, log: dict):
        sqlalchemy.sql.expression.Insert
        self.log.append({**self.d, **log})


