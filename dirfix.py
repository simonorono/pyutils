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
Utility to rename files as a secuence of numbers with trailing zeros
"""

import argparse
import os
from random import shuffle


def main():
    directory_name = '.dirfix'

    parser = argparse.ArgumentParser(description="Directory structure fixer")
    parser.add_argument('-order', type=str, default='date',
                        help="Specify order (random, date [default])")
    args = parser.parse_args()

    # Non-hidden files without directories
    file_list = [x for x in os.listdir() if
                 not os.path.isdir(x) and
                 not x.startswith('.')]

    os.makedirs(directory_name)

    if args.order == 'random':
        shuffle(file_list)
    elif args.order == 'date':
        file_list.sort(key=os.path.getmtime)

    digits = len(str(len(file_list)))
    if digits < 3:
        digits = 3

    new_names = []
    index = 1

    for file in file_list:
        nname = ''.join((str(index).zfill(digits), os.path.splitext(file)[1]))
        os.rename(file, os.path.join(directory_name, nname))
        new_names.append(nname)
        index += 1

    for file in new_names:
        os.rename(os.path.join(directory_name, file), file)

    os.removedirs(directory_name)

if __name__ == '__main__':
    main()
