import re, json, functools, ipaddress
from fnmatch import fnmatch


def detect(record):
    return record.get("eventSource") == "config.amazonaws.com" and (
        record.get("eventName") in ("DeleteDeliveryChannel", "StopConfigurationRecorder")
    )
