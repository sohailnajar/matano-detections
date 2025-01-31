import re, json, functools, ipaddress
from fnmatch import fnmatch


def detect(record):
    return record.get("eventSource") == "rds.amazonaws.com" and (
        record.get("eventName")
        in (
            "AuthorizeDBSecurityGroupIngress",
            "CreateDBSecurityGroup",
            "DeleteDBSecurityGroup",
            "RevokeDBSecurityGroupIngress",
        )
    )
