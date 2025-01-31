import re, json, functools, ipaddress
from fnmatch import fnmatch


def detect(record):
    return (
        record.get("eventSource") == "iam.amazonaws.com"
        and record.get("eventName") == "DeleteSAMLProvider"
        and record.get("status") == "success"
    )
