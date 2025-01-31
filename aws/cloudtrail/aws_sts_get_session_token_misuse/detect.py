import re, json, functools, ipaddress
from fnmatch import fnmatch


def detect(record):
    return (
        record.get("eventSource") == "sts.amazonaws.com"
        and record.get("eventName") == "GetSessionToken"
        and record.get("userIdentity", {}).get("type") == "IAMUser"
    )
