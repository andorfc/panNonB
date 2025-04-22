import pickle
import sys

def parse_gff(gff_file):
    """
    Parses GFF file and extracts G4 quadruplex start positions.
    Returns a list of tuples with chromosome, start, and end positions.
    """
    g4_positions = []
    with open(gff_file, 'r') as gff:
        for line in gff:
            if line.startswith('#'):
                continue
            fields = line.strip().split('\t')
            chrom = fields[0]
            start = int(fields[3])
            end = int(fields[4])
            g4_positions.append((chrom, start, end))
    return g4_positions

def save_serialized_data(data, output_file):
    """
    Serializes and saves data to a file.
    """
    with open(output_file, 'wb') as f:
        pickle.dump(data, f)

def main(gff_file, output_file):
    # Parse the GFF file
    g4_positions = parse_gff(gff_file)

    # Save the parsed data to a serialized file
    save_serialized_data(g4_positions, output_file)

    print(f"Data serialized and saved to {output_file}")


# Example usage
gff_file = sys.argv[1]   #'path_to_gff_file.gff'
output_file = sys.argv[2] #'serialized_g4_positions.pkl'

main(gff_file, output_file)
