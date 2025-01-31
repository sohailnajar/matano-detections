import re, json, functools, ipaddress
from fnmatch import fnmatch


def detect(record):
    return (
        record.get("eventSource") == "ec2.amazonaws.com"
        and record.get("eventName") == "CreateRoute"
    )
