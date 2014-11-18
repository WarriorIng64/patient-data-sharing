# This file is part of patient-data-sharing.
# Copyright (C) 2014 Christopher Kyle Horton <chorton@ltu.edu>

# patient-data-sharing is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# patient-data-sharing is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with patient-data-sharing. If not, see <http://www.gnu.org/licenses/>.


# MCS 5603 Intro to Bioinformatics, Fall 2014
# Christopher Kyle Horton (000516274), chorton@ltu.edu
# Last modified: 11/18/2014

import os

SUITE_NAME = "patient-data-sharing"
SUITE_VERSION = "v1.0.1"
POSITIVE = 1
NEGATIVE = 2
BORDERLINE = 3

def check_file_exists(path):
    '''Checks whether a file exists, and quits the program if not.'''
    if not os.path.exists(path):
        print "Error: {} does not exist".format(path)
        exit(1)
