import re, json, functools, ipaddress
from fnmatch import fnmatch


def detect(record):
    return record.get("eventSource") == "glue.amazonaws.com" and (
        record.get("eventName") in ("CreateDevEndpoint", "DeleteDevEndpoint", "UpdateDevEndpoint")
    )
