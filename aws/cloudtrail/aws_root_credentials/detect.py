import re, json, functools, ipaddress
from fnmatch import fnmatch


def detect(record):
    return (
        record.get("userIdentity", {}).get("type") == "Root"
        and not record.get("eventType") == "AwsServiceEvent"
    )
