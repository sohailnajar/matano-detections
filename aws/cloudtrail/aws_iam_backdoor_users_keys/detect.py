import re, json, functools, ipaddress
from fnmatch import fnmatch


def detect(record):
    return (
        record.get("eventSource") == "iam.amazonaws.com"
        and record.get("eventName") == "CreateAccessKey"
        and not "responseElements.accessKey.userName" in record.get("userIdentity", {}).get("arn")
    )
