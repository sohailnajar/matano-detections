import re, json, functools, ipaddress
from fnmatch import fnmatch


def detect(record):
    return (
        record.get("eventSource") == "rds.amazonaws.com"
        and (
            record.get("responseElements", {})
            .get("pendingModifiedValues", {})
            .get("masterUserPassword")
            and record.get("responseElements", {})
            .get("pendingModifiedValues", {})
            .get("masterUserPassword")
            .startswith("")
        )
        and record.get("eventName") == "ModifyDBInstance"
    )
