import re, json, functools, ipaddress
from fnmatch import fnmatch


def detect(record):
    return re.match(r".+:assumed-role/aws:.+", record.get("userIdentity", {}).get("arn")) and not (
        record.get("eventSource") == "ssm.amazonaws.com"
        or record.get("eventName") == "RegisterManagedInstance"
        or record.get("sourceIPAddress") == "AWS Internal"
    )
