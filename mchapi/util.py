from datetime import datetime
from pytz import timezone
from mchapi.enum import LandEnum


def timestamp_fromdatetime(dt):
    return int(dt.timestamp()) if dt else None


def datetime_fromtimestamp(timestamp):
    return datetime.fromtimestamp(timestamp, tz=timezone('Asia/Tokyo')) if timestamp else None


def enum_value_to_name(enum, value):
    return enum(value).name if value else ''
