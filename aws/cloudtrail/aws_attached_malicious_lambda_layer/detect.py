import re, json, functools, ipaddress
from fnmatch import fnmatch


def detect(record):
    return record.get("eventSource") == "lambda.amazonaws.com" and (
        record.get("eventName")
        and record.get("eventName").startswith("UpdateFunctionConfiguration")
    )
