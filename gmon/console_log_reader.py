# dockserver console log monitor

import re
import time
import os

REGEX = re.compile(
    '(\d{8}T\d{6}) - DockServer received DETECTION event ' + 
    'for glider: (ce_\d{3}) on channel net/(\d)-network-multiple\n')


def main(filename):
    with open(filename, 'r') as fid:
        data = fid.read()
        file_size = fid.tell()
    while 1:
        # compare file size
        
        if os.stat(filename).st_size > file_size:
            with open(filename, 'r') as fid:
                fid.seek(filept)
                data = fid.read()
                file_size = fid.tell()
            for line in data:
                #regex the glider connection
                match = REGEX.match(line)
        time.sleep(10)