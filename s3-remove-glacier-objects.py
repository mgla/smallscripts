#!/usr/bin/env python3
# Removes s3 glacier objects from an s3 bucket
# Author: Maik Glatki <maik@glatki.eu>, 2018

from botocore import credentials
import botocore.session
import boto3
import os
import sys

# Boto3 MFA session magic
working_dir = os.path.join(os.path.expanduser('~'),'.aws/cli/cache')

session = botocore.session.get_session()
provider = session.get_component('credential_provider').get_provider('assume-role')
provider.cache = credentials.JSONFileCache(working_dir)

# Set Variables
s3_bucket="example"
s3_prefix="exampleprefix"

client = boto3.Session(botocore_session=session).client('s3')

objects_left = True
next_token = ''
iterated = 0
deleted = 0
while objects_left:
    if next_token is '':
        res = client.list_objects_v2(
            Bucket=s3_bucket,
            MaxKeys=1000,
            Prefix=s3_prefix
        )
    else:
        res = client.list_objects_v2(
            Bucket=s3_bucket,
            MaxKeys=1000,
            Prefix=s3_prefix
            ContinuationToken=next_token
        )

    glacier_keys = [{'Key': obj['Key']}  for obj in res['Contents'] if obj['StorageClass'] == 'GLACIER']
    iterated += len(res['Contents'])
    deleted += len(glacier_keys)
    if len(glacier_keys) > 0:
        client.delete_objects(
            Bucket=s3_bucket,
            Delete={'Objects': glacier_keys}
        )
# FIXME add this as debug        print("Deleted:\n\t %s" % "\n\t".join(map(lambda x: x['Key'], glacier_keys)))

    if res['IsTruncated']:
        next_token = res['NextContinuationToken']
    else:
        objects_left = False
#    print('.', end='', flush=True)
    sys.stdout.write("\r Iterated %s files, deleted %s files" % (iterated, deleted))
    sys.stdout.flush()
