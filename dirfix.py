#!/bin/env python

"""
Utility to rename files as a secuence of numbers with trailing zeros
"""

import argparse
import os

from random import shuffle

if __name__ == '__main__':
    directory = '.dirfix'

    parser = argparse.ArgumentParser(description="Directory structure fixer")
    parser.add_argument('-order', type=str, default='',
                        help="Specify order (random, date)")
    args = parser.parse_args()

    file_list = [x for x in os.listdir()
                 if not os.path.isdir(x) and
                 not x.startswith('.')]

    os.makedirs(directory)

    if len(args.order) > 0:
        if args.order == 'random':
            shuffle(file_list)
        elif args.order == 'date':
            file_list.sort(key=os.path.getmtime)

    digits = len(str(len(file_list)))
    new_names = []
    n = 1

    for f in file_list:
        nname = ''.join((str(n).zfill(digits), os.path.splitext(f)[1]))
        os.rename(f, os.path.join(directory, nname))
        new_names.append(nname)
        n += 1

    for f in new_names:
        os.rename(os.path.join(directory, f), f)

    os.removedirs(directory)
