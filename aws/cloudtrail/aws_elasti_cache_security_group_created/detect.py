import re, json, functools, ipaddress
from fnmatch import fnmatch


def detect(record):
    return (
        record.get("eventSource") == "elasticache.amazonaws.com"
        and record.get("eventName") == "CreateCacheSecurityGroup"
    )
