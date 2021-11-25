import time
from datetime import datetime, timezone


utc = timezone.utc


def now() -> datetime:
    return datetime.now(tz=utc)


def epoch_now() -> int:
    return int(time.time())
