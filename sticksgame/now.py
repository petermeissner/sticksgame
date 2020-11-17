from datetime import datetime

def now() -> str:
    """
    current timestamp in iso format
    """
    return datetime.now().isoformat()
