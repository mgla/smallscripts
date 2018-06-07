#!/usr/bin/env python3
# Removes s3 glacier objects from an s3 bucket
# Author: Maik Glatki <maik@glatki.eu>, 2018

import os
import sys

from botocore import credentials
import botocore.session
import boto3

# Set Variables
S3_BUCKET = "example"
S3_PREFIX = "exampleprefix"

def get_session():
    """# Boto3 MFA session magic"""
    working_dir = os.path.join(os.path.expanduser('~'), '.aws/cli/cache')

    session = botocore.session.get_session()
    provider = session.get_component('credential_provider').get_provider('assume-role')
    provider.cache = credentials.JSONFileCache(working_dir)
    return session

def main():
    """Remove all matching objecs in storage class GLACIER from S3 bucket"""
    session = get_session()
    client = boto3.Session(botocore_session=session).client('s3')

    objects_left = True
    next_token = ''
    iterated = 0
    deleted = 0
    while objects_left:
        if next_token == '':
            res = client.list_objects_v2(
                Bucket=S3_BUCKET,
                MaxKeys=1000,
                Prefix=S3_PREFIX
            )
        else:
            res = client.list_objects_v2(
                Bucket=S3_BUCKET,
                MaxKeys=1000,
                Prefix=S3_PREFIX,
                ContinuationToken=next_token
            )

        glacier_keys = [{'Key': obj['Key']}
                        for obj in res['Contents']
                        if obj['StorageClass'] == 'GLACIER']
        iterated += len(res['Contents'])
        deleted += len(glacier_keys)
        if glacier_keys:
            client.delete_objects(
                Bucket=S3_BUCKET,
                Delete={'Objects': glacier_keys}
            )

        if res['IsTruncated']:
            next_token = res['NextContinuationToken']
        else:
            objects_left = False
        sys.stdout.write("\r Iterated %s files, deleted %s files" % (iterated, deleted))
        sys.stdout.flush()

main()
