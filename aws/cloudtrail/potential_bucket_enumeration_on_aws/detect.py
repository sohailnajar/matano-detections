import re, json, functools, ipaddress
from fnmatch import fnmatch


def detect(record):
    return (
        record.get("eventSource") == "s3.amazonaws.com"
        and record.get("eventName") == "ListBuckets"
        and not record.get("userIdentity", {}).get("type") == "AssumedRole"
    )
