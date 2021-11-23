import time
from datetime import datetime, timezone


utc = timezone.utc

def now():
    return datetime.now(tz=utc)

def epoch_now() -> int:
    return int(time.time())
