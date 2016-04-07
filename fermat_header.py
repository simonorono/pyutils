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

import os
import sys


if __name__ == '__main__':
    if (len(sys.argv) != 2):
        sys.exit(1)

    nm = sys.argv[1]

    os.mkdir('high')
    os.mkdir('medium')
    os.mkdir('small')
    os.mkdir('svg')

    os.system('inkscape -e high/{0}_logo.png -d 360 {0}_logo.svg'.format(nm))
    os.system('inkscape -e medium/{0}_logo.png -d 90 {0}_logo.svg'.format(nm))
    os.system('inkscape -e small/{0}_logo.png -d 45 {0}_logo.svg'.format(nm))
    os.rename('{0}_logo.svg'.format(nm), 'svg/{0}_logo.svg'.format(nm))
