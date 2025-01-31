import re, json, functools, ipaddress
from fnmatch import fnmatch


def detect(record):
    return (
        record.get("eventSource") == "ecs.amazonaws.com"
        and (
            record.get("eventName")
            in ("DescribeTaskDefinition", "RegisterTaskDefinition", "RunTask")
        )
        and "$AWS_CONTAINER_CREDENTIALS_RELATIVE_URI"
        in record.get("requestParameters", {}).get("containerDefinitions", {}).get("command")
    )
