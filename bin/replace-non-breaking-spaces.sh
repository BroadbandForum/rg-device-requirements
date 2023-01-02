#!/bin/bash
#
# Replace non-breaking spaces (0xc2a0) with normal spaces
#
# Run the script from the directory that contains the files to be edited
# (only *.yaml files are changed)

for file in *.yaml; do
    echo "---- $file ----"
    perl -pe 's/\xc2\xa0/ /g' $file >$file.edited
    /bin/mv -f $file.edited $file
done
