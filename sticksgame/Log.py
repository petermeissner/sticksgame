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


