#!/bin/env python
#
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
#
"""
Utility to generate Fermat headers and icons from SVG files
"""

import argparse
import os
import shutil
import sys


def create_headers_dirs():
    os.makedirs('../high', exist_ok=True)
    os.makedirs('../medium', exist_ok=True)
    os.makedirs('../small', exist_ok=True)
    os.makedirs('../svg', exist_ok=True)


def create_icons_dirs():
    create_headers_dirs()
    os.makedirs('../mini', exist_ok=True)


def main():
    if shutil.which('inkscape') is None:
        sys.exit('Inkscape command line interface was not found')

    parser = argparse.ArgumentParser()
    parser.add_argument('type', help='wheter it is a header or an icon')
    parser.add_argument('code', help='the code of the platform')
    parser.add_argument('file', help='the SVG file')
    args = parser.parse_args()

    if not os.path.exists(args.file):
        sys.exit('The file `{}` doesn\'t exists'.format(args.file))

    if args.type not in ('header', 'icon'):
        sys.exit('Unrecognized type `{}`'.format(args.type))

    if args.type == 'header':
        create_headers_dirs()
        name = '{0}_logo'.format(args.code)
        os.rename(args.file, '{0}.svg'.format(name))
        os.system('inkscape -e ../high/{0}.png -d 360 {0}.svg'.format(name))
        os.system('inkscape -e ../medium/{0}.png -d 90 {0}.svg'.format(name))
        os.system('inkscape -e ../small/{0}.png -d 45 {0}.svg'.format(name))
        os.rename('{0}.svg'.format(name), '../svg/{0}.svg'.format(name))

    elif args.type == 'icon':
        create_icons_dirs()
        name = 'icon_{0}'.format(args.code)
        os.rename(args.file, '{0}.svg'.format(name))
        os.system('inkscape -e ../high/{0}.png -d 720 {0}.svg'.format(name))
        os.system('inkscape -e ../medium/{0}.png -d 90 {0}.svg'.format(name))
        os.system('inkscape -e ../small/{0}.png -d 45 {0}.svg'.format(name))
        os.system('inkscape -e ../mini/{0}.png -d 22 {0}.svg'.format(name))
        os.rename('{0}.svg'.format(name), '../svg/{0}.svg'.format(name))

if __name__ == '__main__':
    main()
