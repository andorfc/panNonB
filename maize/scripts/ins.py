import sys


input_file = sys.argv[1]
output_file = sys.argv[2]


def filter_vcf(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # Write header lines (lines starting with #) directly to the output file
            if line.startswith('#'):
                outfile.write(line)
            else:
                columns = line.strip().split('\t')
                # Check if the line has at least 4 columns and if the length of the fourth column is > 1
                if len(columns) >= 4 and len(columns[3]) > 1:
                    outfile.write(line)


filter_vcf(input_file, output_file)
