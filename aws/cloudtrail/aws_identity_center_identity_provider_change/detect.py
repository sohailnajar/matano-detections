import re, json, functools, ipaddress
from fnmatch import fnmatch


def detect(record):
    return (record.get("eventSource") in ("sso-directory.amazonaws.com", "sso.amazonaws.com")) and (
        record.get("eventName")
        in (
            "AssociateDirectory",
            "DisableExternalIdPConfigurationForDirectory",
            "DisassociateDirectory",
            "EnableExternalIdPConfigurationForDirectory",
        )
    )
