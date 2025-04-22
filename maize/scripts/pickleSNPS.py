import pickle
import sys

def parse_vcf(vcf_file):
    """
    Parses VCF file and extracts chromosome and start positions.
    Returns a list of tuples with chromosome and start positions.
    """
    vcf_positions = []
    with open(vcf_file, 'r') as vcf:
        for line in vcf:
            if line.startswith('#'):
                continue
            fields = line.strip().split('\t')
            chrom = fields[0]
            start = int(fields[1])
            vcf_positions.append((chrom, start))
    return vcf_positions

def save_serialized_data(data, output_file):
    """
    Serializes and saves data to a file.
    """
    with open(output_file, 'wb') as f:
        pickle.dump(data, f)

def main(vcf_file, output_file):
    # Parse the VCF file
    vcf_positions = parse_vcf(vcf_file)

    # Save the parsed data to a serialized file
    save_serialized_data(vcf_positions, output_file)

    print(f"Data serialized and saved to {output_file}")


# Example usage
vcf_file = sys.argv[1]
output_file = sys.argv[2]

main(vcf_file, output_file)
