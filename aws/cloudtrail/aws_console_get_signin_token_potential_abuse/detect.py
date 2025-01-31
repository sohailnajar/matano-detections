import re, json, functools, ipaddress
from fnmatch import fnmatch


def detect(record):
    return (
        record.get("eventSource") == "signin.amazonaws.com"
        and record.get("eventName") == "GetSigninToken"
        and not "Jersey/${project.version}" in record.get("userAgent")
    )
