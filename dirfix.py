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
Utility to rename files as a secuence of numbers with trailing zeros
"""

import argparse
import os

from random import shuffle

if __name__ == '__main__':
    directory_name = '.dirfix'

    parser = argparse.ArgumentParser(description="Directory structure fixer")
    parser.add_argument('-order', type=str, default='date',
                        help="Specify order (random, date [default])")
    args = parser.parse_args()

    # Files without directories and hidden files
    file_list = [x for x in os.listdir()
                 if not os.path.isdir(x) and
                 not x.startswith('.')]

    os.makedirs(directory_name)

    if len(args.order) > 0:
        if args.order == 'random':
            shuffle(file_list)
        elif args.order == 'date':
            file_list.sort(key=os.path.getmtime)

    digits = len(str(len(file_list)))
    if digits < 3:
        digits = 3

    new_names = []
    n = 1

    for f in file_list:
        nname = ''.join((str(n).zfill(digits), os.path.splitext(f)[1]))
        os.rename(f, os.path.join(directory_name, nname))
        new_names.append(nname)
        n += 1

    for f in new_names:
        os.rename(os.path.join(directory_name, f), f)

    os.removedirs(directory_name)
