#!/bin/bash

date                          #optional, prints out timestamp at the start of the job in stdout file

python get_SNP_freqs_MB.py $1 $2 $3

date                          #optional, prints out timestamp when the job ends
#End of file
