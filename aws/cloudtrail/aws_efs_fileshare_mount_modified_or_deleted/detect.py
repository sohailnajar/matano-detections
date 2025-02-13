import re, json, functools, ipaddress
from fnmatch import fnmatch


def detect(record):
    return (
        record.get("eventSource") == "elasticfilesystem.amazonaws.com"
        and record.get("eventName") == "DeleteMountTarget"
    )
