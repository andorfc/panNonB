import pickle
from collections import defaultdict
import sys
import os
from collections import defaultdict
import bisect

def load_serialized_data_file(file_path):
    """
    Loads serialized data from a file.
    """
    with open(file_path, 'rb') as f:
        return pickle.load(f)

def load_serialized_data(folder_path):
    """
    Loads and merges serialized data from all pickle files in a folder.

    Args:
        folder_path (str): The path to the folder containing pickle files.

    Returns:
        list: A list containing the merged data from all pickle files.
    """
    merged_data = []
    total_snp_count = 0  # Initialize a counter for SNPs

    # Loop through all files in the folder
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        # Check if the file has a .pickle or .pkl extension
        if file_name.endswith('.pickle') or file_name.endswith('.pkl'):
            with open(file_path, 'rb') as f:
                data = pickle.load(f)
                merged_data.append(data)  # You can modify this to merge as needed

                # Count the number of SNPs in the current file
                for sublist in data:
                    total_snp_count += len(sublist)

    # Preview the first few records
    #print("Previewing the first few records of merged_data:")
    #for i, record in enumerate(merged_data[:5]):  # Print the first 5 records (or fewer if less data exists)
    #    print(f"Record {i + 1}: {record}")

    return merged_data, total_snp_count

def count_snp_distances(g4_positions, snp_positions, window=1000):
    """
    Counts the SNPs within a specified window around each G4 quadruplex start position.
    Returns a dictionary with distances from G4 start as keys and SNP counts as values.
    """
    distance_counts = defaultdict(int)

    print("Convert SNP positions to a dictionary for faster lookup", flush=True)
    # Convert SNP positions to a dictionary for faster lookup

    snp_dict = defaultdict(list)
    # Iterate through the sub-lists in snp_positions
    for sublist in snp_positions:
        for chrom, pos in sublist:  # Now this will unpack correctly
            snp_dict[chrom].append(pos)

#    snp_dict = defaultdict(list)
#    for chrom, pos in snp_positions:
#        snp_dict[chrom].append(pos)

    print("Sort SNP positions for each chromosome", flush=True)
    # Sort SNP positions for each chromosome
    for chrom in snp_dict:
        snp_dict[chrom].sort()


    print("Get SNP positions on the same chromosome within the window", flush=True)
    record_count = 0
    snp_hits = 0
    g4_size = 0

    for chrom, g4_start, g4_end in g4_positions:
        temp_size = g4_end - g4_start
        g4_size = g4_size + temp_size

        if chrom in snp_dict:
            # Get SNP positions on the same chromosome within the window
            snps = snp_dict[chrom]
            start_range = g4_start - window
            end_range = g4_end + window
            for snp_pos in snps:
                if start_range <= snp_pos <= end_range:
                    snp_hits = snp_hits +1

        # Increment record count and print status every 1000 records
        record_count += 1
        if record_count % 1000 == 0:
            print(f"Processed {record_count} G4 records",flush=True)

    return snp_hits, g4_size

def count_snp_distances_fast(g4_positions, snp_positions, window=1000):
    """
    Counts the SNPs within a specified window around each G4 quadruplex start position.
    Returns the total number of SNP hits and the cumulative size of all G4 regions.
    """
    distance_counts = defaultdict(int)

    print("Convert SNP positions to a dictionary for faster lookup", flush=True)
    # Convert SNP positions to a dictionary for faster lookup
    snp_dict = defaultdict(list)
    for sublist in snp_positions:
        for chrom, pos in sublist:
            snp_dict[chrom].append(pos)

    print("Sort SNP positions for each chromosome", flush=True)
    # Sort SNP positions for each chromosome
    for chrom in snp_dict:
        snp_dict[chrom].sort()

    print("Get SNP positions on the same chromosome within the window using binary search", flush=True)
    record_count = 0
    snp_hits = 0
    g4_size = 0

    for chrom, g4_start, g4_end in g4_positions:
        temp_size = g4_end - g4_start
        g4_size += temp_size

        if chrom in snp_dict:
            snps = snp_dict[chrom]
            start_range = g4_start - window
            end_range = g4_end + window

            # Find the left and right indices using bisect
            left_idx = bisect.bisect_left(snps, start_range)
            right_idx = bisect.bisect_right(snps, end_range)

            # The number of SNPs in the range is right_idx - left_idx
            snp_hits += (right_idx - left_idx)

        # Increment record count and print status every 1000 records
        record_count += 1
        if record_count % 1000 == 0:
            print(f"Processed {record_count} G4 records", flush=True)

    return snp_hits, g4_size

def save_distance_counts(out_file, snp_hits, g4_size,total_snp_count):
    """
    Saves the distance counts to a file.
    """
    with open(out_file, 'w') as out:
        out.write('G4_size\tSNP_Count\tTotal_SNPs\n')
        out.write(f'{g4_size}\t{snp_hits}\t{total_snp_count}\n')

def main(g4_file, snp_file, out_file):
    print("Start", flush=True)
    snp_hits = 0
    g4_size = 0
    # Load serialized data
    g4_positions = load_serialized_data_file(g4_file)
    snp_positions, total_snp_count = load_serialized_data(snp_file)

    # Count SNP distances from each G4 quadruplex
    snp_hits, g4_size = count_snp_distances_fast(g4_positions, snp_positions, 0)

    # Save the distance counts to an output file
    save_distance_counts(out_file, snp_hits, g4_size,total_snp_count)

    print(f"SNP distance counts saved to {out_file}")

# Example usage
g4_file = sys.argv[1]
snp_path = sys.argv[2]
out_file = sys.argv[3]

main(g4_file, snp_path, out_file)
