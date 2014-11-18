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
# Last modified: 11/17/2014

import argparse
import csv

import suite

desc = suite.SUITE_NAME + "/make_request " + suite.SUITE_VERSION
desc += """\nMakes a request file consisting of research IDs for the requested
 patients."""

#============================================================================
# Main program code
#============================================================================

parser = argparse.ArgumentParser(
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description=desc
            )
parser.add_argument("bcs", help="Input bcs file.")
parser.add_argument("bcs_backlink", help="Input bcs-backlink file.")
parser.add_argument("lower_age",
                    type=int,
                    help="Low end of age range (inclusive).")
parser.add_argument("upper_age",
                    type=int,
                    help="High end of age range (inclusive).")
parser.add_argument("-o",
                    "--outfile",
                    type=str,
                    default="request.txt",
                    help="Output request file name (default: request.txt).")
args = parser.parse_args()

suite.check_file_exists(args.bcs)
suite.check_file_exists(args.bcs_backlink)

# Read in bcs.txt file contents
bcs_rows = []
bcs_backlink_rows = []
outrows = []
# Find research ID's corresponding to age range
with open(args.bcs, 'r') as b:
    reader = csv.DictReader(b)
    for row in reader:
        # Don't select NA's or anything else which is not a number
        if row['ageatdiagnosis'].isdigit():
            if args.lower_age <= int(row['ageatdiagnosis']) <= args.upper_age:
                bcs_rows.append(row['resid'])
# Find hashes for selected research ID's
with open(args.bcs_backlink, 'r') as bb:
    reader = csv.DictReader(bb)
    for row in reader:
        use_hash = False
        for resid in bcs_rows:
            if resid == row['resid']:
                outrows.append({'resid': resid, 'hash': row['hash']})
if len(outrows) < 1:
    print "No research ID's found matching criteria."
    exit(2)
with open(args.outfile, 'w') as f:
    # Write back out the contents of our request
    f.write('"resid","hash"\n')
    for row in outrows:
        f.write('"{}","{}"\n'.format(row['resid'], row['hash']))
exit(0)
