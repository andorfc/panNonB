#!/bin/bash

date                          #optional, prints out timestamp at the start of the job in stdout file

echo "$1 $2"
python pickleNonB.py $1 $2

date                          #optional, prints out timestamp when the job ends
#End of file
