from datetime import datetime, timedelta


def push_periods():
    periods = []
    starts_at = datetime(2021,1,1,0,0)
    a_day = timedelta(days=1)
    periods.append(starts_at)
    return periods