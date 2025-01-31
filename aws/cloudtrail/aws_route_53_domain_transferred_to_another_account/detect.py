import re, json, functools, ipaddress
from fnmatch import fnmatch


def detect(record):
    return (
        record.get("eventSource") == "route53.amazonaws.com"
        and record.get("eventName") == "TransferDomainToAnotherAwsAccount"
    )
