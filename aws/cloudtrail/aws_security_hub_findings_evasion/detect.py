import re, json, functools, ipaddress
from fnmatch import fnmatch


def detect(record):
    return record.get("eventSource") == "securityhub.amazonaws.com" and (
        record.get("eventName")
        in ("BatchUpdateFindings", "DeleteInsight", "UpdateFindings", "UpdateInsight")
    )
