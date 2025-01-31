import re, json, functools, ipaddress
from fnmatch import fnmatch


def detect(record):
    return (
        record.get("userIdentity", {}).get("type") == "AssumedRole"
        and record.get("userIdentity", {})
        .get("sessionContext", {})
        .get("sessionIssuer", {})
        .get("type")
        == "Role"
    )
