import re, json, functools, ipaddress
from fnmatch import fnmatch


def detect(record):
    return record.get("eventSource") == "cloudtrail.amazonaws.com" and (
        record.get("eventName") in ("StopLogging", "UpdateTrail", "DeleteTrail")
    )
