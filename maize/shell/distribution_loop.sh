#!/bin/bash

date                          #optional, prints out timestamp at the start of the job in stdout file

# Define the arrays for each variable
species_array=("B73" "CML228" "CML322" "CML69" "Ki11" "M162W" "Ms71" "P39" "B97" "CML247" "CML333" "HP301" "Ki3" "M37W" "NC350" "Oh43" "Tx303" "CML103" "CML277" "CML52" "Il14H" "Ky21" "Mo18W" "NC358" "Oh7B" "Tzi8")
element_array=("APR" "DR" "GQ" "MR" "STR" "Z")
gtype_array=("tss" "cds" "exon" "end")
length_array=("2000")

mkdir ./lists/size${length_array}/
mkdir ./img/size${length_array}/

# Loop through all combinations of variables
for species in "${species_array[@]}"; do
  for element in "${element_array[@]}"; do
      if [ "$element" = "GQ" ]; then
          stype_array=("antisense" "sense")
      else
          stype_array=("all")
      fi
    for stype in "${stype_array[@]}"; do
      for gtype in "${gtype_array[@]}"; do
        for length in "${length_array[@]}"; do
            if [ "$element" = "APR" ]; then
                ymax_array=("1000")
            elif [ "$element" = "DR" ]; then
                ymax_array=("1000")
            elif [ "$element" = "GQ" ]; then
                ymax_array=("1000")
            elif [ "$element" = "MR" ]; then
                ymax_array=("2000")
            elif [ "$element" = "STR" ]; then
                ymax_array=("2000")
            elif [ "$element" = "IR" ]; then
                ymax_array=("4000")
            elif [ "$element" = "Z" ]; then
                ymax_array=("1000")
            fi
          for ymax in "${ymax_array[@]}"; do
            tss_file="./${gtype}_pan/${species}.csv"
            g4_file="./GFF/${species}/${element}.csv"

            echo "python make_distribution.py $species $element $stype $gtype $length $ymax $tss_file $g4_file"
            python ./scripts/make_distribution_lowmem.py $species $element $stype $gtype $length $ymax $tss_file $g4_file

          done
        done
      done
    done
  done
done

date
