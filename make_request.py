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

import suite

desc = suite.SUITE_NAME + "/make_request " + suite.SUITE_VERSION
desc += """\nMakes a request file consisting of research IDs for the requested
\n patients."""

#============================================================================
# Main program code
#============================================================================

parser = argparse.ArgumentParser(
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description=desc
            )
parser.add_argument("infile", help="Input request file.")
parser.add_argument("lower_age",
                    type=int,
                    help="Low end of age range (inclusive).")
parser.add_argument("upper_age",
                    type=int,
                    help="High end of age range (inclusive).")
parser.add_argument("-o",
                    "--outfile",
                    type=str,
                    help="Output request file name (default: request.txt).")
args = parser.parse_args()

if os.path.exists(args.infile):
    # Read in file contents
    # TODO
    exit(0)
else
    print "Error: {} does not exist".format(args.infile)
    exit(1)
