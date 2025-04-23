#!/bin/bash

#SBATCH --array=0-27   # 7 types × 4 regions = 28 tasks; limit 5 running at once

date                          #optional, prints out timestamp at the start of the job in stdout file

types=(APR DR GQ IR MR STR Z)
regions=(TSS CDS EXON END)

# map the task ID to one (type,region) pair
idx=$SLURM_ARRAY_TASK_ID
nt=${#types[@]}
nr=${#regions[@]}

ti=$(( idx / nr ))
ri=$(( idx % nr ))

t=${types[$ti]}
r=${regions[$ri]}

python make_pangenome_figure.py "$t" "$r"
