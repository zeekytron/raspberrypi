# -*- coding: utf-8 -*-
#!/usr/bin/env python

# This script is meant to be used with Raspberry pi, the Raspberry pi camera,
# and Motion.  It will take a file path as input and then upload it to
# an AWS S3 bucket.

# https://github.com/Motion-Project/motion/releases
# https://github.com/ccrisan/motioneyeos/wiki (not used, but looks interesting)
# pip install awscli
# pip install --upgrade google-api-python-client
# pip install boto3

import os
import boto3
import sys

filePath = sys.argv[1]
fileName = filePath[filePath.rfind("/")+1:]
bucketName = "ybs-motion-camera"

try:
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucketName).upload_file(filePath, fileName)
    print "Successfully uploaded the file [%s] to S3 bucket [%s]" % (filePath, bucketName)

except Exception,e:
    print str(e)
    print "Unable to upload the file [%s] to S3 bucket [%s]" % (filePath, bucketName)


