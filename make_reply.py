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
import hashlib

import suite

desc = suite.SUITE_NAME + "/make_reply " + suite.SUITE_VERSION
desc += """\nMakes a reply file consisting of research IDs for the requested
 patients."""

#============================================================================
# Main program code
#============================================================================

parser = argparse.ArgumentParser(
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description=desc
            )
parser.add_argument("request", help="Input request file.")
parser.add_argument("master_backlink", help="Input master backlink file.")
parser.add_argument("master_pathology", help="Input master pathology file.")
parser.add_argument("-o",
                    "--outfile",
                    type=str,
                    default="reply.txt",
                    help="Output reply file name (default: reply.txt).")
args = parser.parse_args()

suite.check_file_exists(args.request)
suite.check_file_exists(args.master_backlink)
suite.check_file_exists(args.master_pathology)

# Read in request file.
request_rows = []
with open(args.request, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        request_rows.append(row)
# Locate matching patient ID's using SHA256 and record links
links = []
with open(args.master_backlink, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Compute hash from patient ID and salt
        source = row['patientid'] + row['salt']
        computed_hash = hashlib.sha256(source).hexdigest()
        for request_row in request_rows:
            if request_row['hash'] == computed_hash:
                links.append({'resid': request_row['resid'],
                              'patientid': row['patientid']})
# Get additional data from patient ID's and construct reply file
pathology_data = []
with open(args.master_pathology, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # See if patient ID's match, and record data if so
        for link in links:
            if link['patientid'] == row['patientid']:
                # Merge dictionaries while excluding patient ID
                data_dict = {key: value for key, value in 
                             dict(link.items() + row.items()).items()
                             if key != 'patientid'}
                pathology_data.append(data_dict)
with open(args.outfile, 'w') as f:
    # Write back out the contents of our reply
    f.write('"resid","grade","nodesexam","nodespos","extent","nodalstatus","size","pgr","er"\n')
    for row in pathology_data:
        f.write('"{}","{}","{}","{}","{}","{}","{}","{}","{}"\n'.format(
                row['resid'],
                row['grade'],
                row['nodesexam'],
                row['nodespos'],
                row['extent'],
                row['nodalstatus'],
                row['size'],
                row['pgr'],
                row['er']))
exit(0)
