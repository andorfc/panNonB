import pandas as pd
import sys

gff_filename = sys.argv[1]
species = sys.argv[2]
type_ = sys.argv[3]  # type is a reserved keyword in Python, hence type_
inpath = sys.argv[4]
outpath = sys.argv[5]
formal_name = sys.argv[6]

# Initialize the counter
counter = 1

# Read the GFF file, modify it, and write results to a new file or overwrite
with open(inpath + gff_filename, 'r') as file:
    lines = file.readlines()

with open(outpath +  gff_filename, 'w') as file:
    for line in lines:
        if line.startswith('#'):
            file.write(line)  # Write the comment lines as is
        else:
            parts = line.strip().split('\t')
            attributes = parts[8]
            # Append the new attribute
            new_name = f"Name={species}.{type_}.{str(counter).zfill(6)}"
            attributes += ';' + new_name
            parts[8] = attributes
            # Write the modified line
            file.write('\t'.join(parts) + '\n')
            counter += 1

counter = 1
with open(outpath + formal_name, 'w') as file2:
    for line in lines:
        if line.startswith('#'):
            file.write(line)  # Write the comment lines as is
        else:
            parts = line.strip().split('\t')
            attributes = parts[8]
            # Append the new attribute
            new_name = f"Name={species}.{type_}.{str(counter).zfill(6)}"
            attributes += ';' + new_name
            parts[8] = attributes
            # Write the modified line
            file2.write('\t'.join(parts) + '\n')
            counter += 1
