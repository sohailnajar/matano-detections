import re, json, functools, ipaddress
from fnmatch import fnmatch


def detect(record):
    return (
        record.get("eventName") == "SendCommand"
        and record.get("eventSource") == "ssm.amazonaws.com"
        and record.get("responseElements", {}).get("command", {}).get("status") == "Success"
    )
