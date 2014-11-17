patient-data-sharing
====================

A collection of programs for Homework 4 in my Fall 2014 Intro to Bioinformatics class. These programs simulate secure patient data sharing for a breast cancer study. There are five activities that these programs need to be able to do, according to the original homework requirements reproduced below (from [here][1]):

> 1. Acting for the research team, using the file bcs.txt find research-IDs for the patients diagnosed at the selected ages.
1. Acting for the research team, using the file bcs-backlink.txt prepare a request file with a list of research-IDs and hashes for the selected patients.
1. Acting for the pathology database administrator, read the request file from the research team and using the file master-backlink.txt match the hashes with patient-IDs.
1. Acting for the pathology database administrator, using the file master-pathology.txt write a reply file of just the data lines for the selected patients with patient-ID replaced with the matching research-ID.
1. Acting for the research team, read the reply file and calculate the percentage of the selected patients who are negative for both estrogen and progesterone receptors.

This requires handling CSV data files and utilizing SHA hashing.

## Technical details ##
These programs are implemented using Python 2.7.

## License ##
GNU GPLv3

[1]: http://medicalopensource.net/mcs5603/recap.html#L11
