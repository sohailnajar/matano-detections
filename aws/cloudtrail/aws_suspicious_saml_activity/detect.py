import re, json, functools, ipaddress
from fnmatch import fnmatch


def detect(record):
    return (
        record.get("eventSource") == "sts.amazonaws.com"
        and record.get("eventName") == "AssumeRoleWithSAML"
        or record.get("eventSource") == "iam.amazonaws.com"
        and record.get("eventName") == "UpdateSAMLProvider"
    )
