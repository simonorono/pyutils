#!/bin/env python
# Copyright 2016 Simón Oroño
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Utility to download files with common extensions from the Internet
"""

import argparse
import os

from urllib.request import urlopen


def download(url):
    print('GET: {}'.format(url))
    resp = urlopen(url)
    return resp.read()


def zerofill(tstr, n):
    l = len(tstr)
    for _ in range(n - l):
        tstr = '0' + tstr
    return tstr

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='The base URL')
    parser.add_argument('count', help='The number of files', type=int)
    parser.add_argument('ext', help='The files extension')
    parser.add_argument('-lz', '--leadingzeros', type=int, default=0,
                        help='The number of leading zeros in the name')
    parser.add_argument('-0', '--zeroindexed', help='start counting from 0',
                        action='store_true')
    parser.add_argument('-o', '--output', default='',
                        help='directory to store the files')
    args = parser.parse_args()

    if args.output != '':
        os.makedirs(args.output, exist_ok=True)

    lz = args.leadingzeros

    if args.zeroindexed:
        start = 0
        end = args.count
    else:
        start = 1
        end = args.count + 1

    for i in range(start, end):
        file_name = '{}.{}'.format(zerofill(str(i), lz), args.ext)

        url = '{}{}'.format(args.url, file_name)
        data = download(url)

        if args.output != '':
            file_name = os.path.join(args.output, file_name)

        with open(file_name, 'wb') as f:
            f.write(data)
