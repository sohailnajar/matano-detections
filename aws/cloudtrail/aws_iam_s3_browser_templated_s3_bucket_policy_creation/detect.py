import re, json, functools, ipaddress
from fnmatch import fnmatch


def detect(record):
    return (
        record.get("eventSource") == "iam.amazonaws.com"
        and record.get("eventName") == "PutUserPolicy"
        and "S3 Browser" in record.get("userAgent")
        and fnmatch(record.get("requestParameters"), '*"arn:aws:s3:::<YOUR-BUCKET-NAME>/*"*')
        and '"s3:GetObject"' in record.get("requestParameters")
        and '"Allow"' in record.get("requestParameters")
    )
