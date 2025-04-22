#!/bin/bash

date                          #optional, prints out timestamp at the start of the job in stdout file

# change to the directory containing the files

# loop through the files in the directory
for file in $(ls ./data/annotations/)
do
    # print the filename
    echo $file
    python ./scripts/parse_END_pan.py ./data/annotations/$file ./end_pan/${file}.csv
done


date                          #optional, prints out timestamp when the job ends
#End of file
