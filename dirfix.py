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


def get_files(path):
    """Non-hidden files without directories"""
    file_list = [x for x in os.listdir(path) if
                 not os.path.isdir(os.path.join(path, x)) and
                 not x.startswith('.')]
    return file_list

def get_dirs(path):
    dir_list = [x for x in os.listdir(path) if
                os.path.isdir(os.path.join(path, x)) and
                not x.startswith('.')]
    return dir_list

def run_dir(path, order, recursive):
    hidden_dir = os.path.join(path, '.dirfix')

    file_list = [os.path.join(path, x) for x in get_files(path)]
    if len(file_list) != 0:
        os.makedirs(hidden_dir)

        if order == 'random':
            shuffle(file_list)
        elif order == 'date':
            file_list.sort(key=os.path.getmtime)

        digits = len(str(len(file_list)))
        if digits < 3:
            digits = 3

        new_names = []
        index = 1

        for file in file_list:
            nname = ''.join((str(index).zfill(digits), os.path.splitext(file)[1]))
            os.rename(file, os.path.join(hidden_dir, nname))
            new_names.append(nname)
            index += 1

        for file in new_names:
            hidden_file_path = os.path.join(hidden_dir, file)
            file_path = os.path.join(path, file)
            os.rename(hidden_file_path, file_path)

        os.removedirs(hidden_dir)

    if recursive:
        dir_list = get_dirs(path)
        for dir in dir_list:
            run_dir(os.path.join(path, dir), order, recursive)

def main():
    parser = argparse.ArgumentParser(description="Directory structure fixer")
    parser.add_argument('-order', type=str, default='date',
                        help="Specify order (random, date [default])")
    parser.add_argument('-r', action='store_true', help="Process subdirectories")
    args = parser.parse_args()

    if args.order not in ('random', 'date'):
        print('`{}` order not found, `date` will be used'.format(args.order))
        args.order = 'date'

    run_dir('.', args.order, args.r)

if __name__ == '__main__':
    main()
