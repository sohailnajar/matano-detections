import re, json, functools, ipaddress
from fnmatch import fnmatch


def detect(record):
    return (
        record.get("eventName") == "CreateInstanceExportTask"
        and record.get("eventSource") == "ec2.amazonaws.com"
        and not (
            (record.get("errorMessage") and record.get("errorMessage").startswith(""))
            or (record.get("errorCode") and record.get("errorCode").startswith(""))
            or "Failure" in record.get("responseElements")
        )
    )
