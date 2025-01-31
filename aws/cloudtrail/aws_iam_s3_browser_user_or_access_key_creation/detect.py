import re, json, functools, ipaddress
from fnmatch import fnmatch


def detect(record):
    return (
        record.get("eventSource") == "iam.amazonaws.com"
        and (record.get("eventName") in ("CreateUser", "CreateAccessKey"))
        and "S3 Browser" in record.get("userAgent")
    )
