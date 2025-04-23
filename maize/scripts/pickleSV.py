import pickle
import sys

def parse_bed(bed_file):
    """
    Parses BED file and extracts chromosome, start, end positions, and feature types.
    Returns a dictionary with feature types as keys and a list of tuples with
    chromosome, start, and end positions as values.
    """
    bed_data = {'INV': [], 'DEL': [], 'KNOB180': [], 'INS': []}

    with open(bed_file, 'r') as bed:
        for line in bed:
            fields = line.strip().split('\t')
            chrom = fields[0]
            start = int(fields[1])
            end = int(fields[2])

            # Extract feature type
            info_fields = fields[4].split('\t')  # Split the info fields by tab
            feature_type = [f.split('=')[1] for f in info_fields if 'feature_type' in f][0]

            # Only store the data if feature type is one of INV, DEL, or KNOB180
            if feature_type in bed_data:
                bed_data[feature_type].append((chrom, start))
                bed_data[feature_type].append((chrom, end))

    return bed_data

def save_serialized_data(data, output_file):
    """
    Serializes and saves data to a file.
    """
    with open(output_file, 'wb') as f:
        pickle.dump(data, f)

def main(bed_file, output_prefix):
    # Parse the BED file
    bed_data = parse_bed(bed_file)

    # Save separate files for INV, DEL, and KNOB180
    for feature_type, positions in bed_data.items():
        output_file = f"./pickle/{output_prefix}_{feature_type}.pkl"
        save_serialized_data(positions, output_file)
        print(f"Data serialized and saved to {output_file}")

# Example usage
bed_file = sys.argv[1]
output_prefix = sys.argv[2]

main(bed_file, output_prefix)
