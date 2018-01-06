# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 17:51:53 2018

@author: swamy
"""

import re
import os
import subprocess

basedir = ' /opt/data/daily/client_files'

pattern = 'error_log'

s3_bucket = 's3://my_bucket'

for file in os.listdir(basedir):
    if re.match(pattern,file):

        subprocess.call(['zip',os.path.join(basedir,file), os.path.join(basedir,file)+'.zip'])

        subprocess.call(['aws','s3','cp', os.path.join(basedir,file)+'.zip',s3_bucket])
