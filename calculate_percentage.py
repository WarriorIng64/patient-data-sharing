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

import argparse
import csv

import suite

desc = suite.SUITE_NAME + "/calculate_percentage " + suite.SUITE_VERSION
desc += """\nCalculates the percentage of selected patients who are negative
 for both estrogen and progesterone receptors."""

#============================================================================
# Main program code
#============================================================================

parser = argparse.ArgumentParser(
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description=desc
            )
parser.add_argument("reply", help="Input reply file.")
args = parser.parse_args()

suite.check_file_exists(args.reply)

# Get the number of patients in the reply and tally those negative for both
# estrogen and progesterone receptors
total_rows = 0
total_both_negative = 0
total_er_negative = 0
total_pgr_negative = 0
with open(args.reply, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        total_rows += 1
        if row['er'] == suite.NEGATIVE:
            if row['pgr'] == suite.NEGATIVE:
                total_both_negative += 1
            else:
                total_er_negative += 1
        else:
            if row['pgr'] == suite.NEGATIVE:
                total_pgr_negative += 1
any_negative_total = total_both_negative + total_er_negative + total_pgr_negative
both_percentage = float(total_both_negative) / float(total_rows)
er_percentage = float(total_er_negative) / float(total_rows)
pgr_percentage = float(total_pgr_negative) / float(total_rows)
any_negative_percentage = float(any_negative_total) / float(total_rows)
print "{} total patients were examined for this calculation.".format(total_rows)
print "{:.2%} of patients are negative for only estrogen receptors.".format(er_percentage)
print "{:.2%} of patients are negative for only progesterone receptors.".format(pgr_percentage)
print "{:.2%} of patients are negative for both estrogen and progesterone receptors.".format(both_percentage)
print "{:.2%} of patients are not negative for both estrogen and progesterone receptors.".format(both_percentage)

exit(0)
