# Import the required modules
import pandas as pd
import sys
import matplotlib.pyplot as plt
from intervaltree import IntervalTree

# Read command-line arguments
species = sys.argv[1]
element = sys.argv[2]
stype = sys.argv[3]
gene_body = sys.argv[4]
distribution_size = int(sys.argv[5])
distribution_size_neg = 0 - distribution_size
ymax = int(sys.argv[6])
tss_file1 = sys.argv[7]
gf_file1 = sys.argv[8]

# Read the first file and create a DataFrame
custom_column_names = ['pan','gm','chr', 'start','strand']
df1 = pd.read_csv(tss_file1, sep=',', header=0, names=custom_column_names)
df1['chr'] = df1['chr'].astype(str)

# Read the third file and create a DataFrame
#custom_column_names = ["Sequence_name", "Source", "Type", "Start", "Stop", "Length", "Score", "Strand", "Repeat", "Spacer", "KVScore", "Subset", "Composition", "Sequence"]
custom_column_names = ["chr", "start", "end", "strand", "seq", "seq.id"]
df3 = pd.read_csv(gf_file1, sep=',', header=0, names=custom_column_names)
#df3.rename(columns={"Sequence_name": "chr", "Start": "start", "Stop": "end", "Strand": "strand", "Sequence": "seq"}, inplace=True)
df3['chr'] = df3['chr'].astype(str)

print(df1,flush=True)

print(df3,flush=True)

# Build an interval tree using df3
interval_trees = {}
for index, row in df1.iterrows():
    if row['chr'] not in interval_trees:
        interval_trees[row['chr']] = IntervalTree()
    # Store a tuple (strand, start) along with the interval
    interval_data = row['strand'], row['start'], row['pan'], row['gm']
    interval_trees[row['chr']][(row['start'] - distribution_size - 1):(row['start'] + distribution_size + 1)] = interval_data

print("int_tree is built")
#print(interval_trees["chr1"],flush=True)

# Create an empty array to store the distances
count_value = [0 for i in range(0, distribution_size * 2 + 1)]
merged_data = []

# Loop through the rows in df1
for index, row in df3.iterrows():
    #print(row['chr'])

    if row['chr'] in interval_trees:
        # Query the interval tree for the specific chromosome
        overlapping_intervals = interval_trees[row['chr']][int(row['start']):int(row['end'])]

        # Calculate distances and update count values
        for interval in overlapping_intervals:
            if isinstance(interval, int):
                # Handle cases where interval_data is an integer
                strand, start = 'N/A', interval  # Assign default values
            else:
                #interval_main, strand, start = interval   # Extract strand and start position
                interval_start, interval_end, strand, start, pan, gm = interval.begin, interval.end, interval.data[0],interval.data[1],interval.data[2],interval.data[3]
                hit_flag = False
                for i in range(int(row['start']), int(row['end'])+1):
                    if strand == "+":
                        distance = i - start
                    elif strand == "-":
                        distance = start - i
                    if abs(distance) <= distribution_size:
                        if stype == "antisense" and strand != row['strand'] :
                            count_value[distance + distribution_size] = count_value[distance + distribution_size] + 1
                            hit_flag = True
                        if stype == "sense" and strand == row['strand'] :
                            count_value[distance + distribution_size] = count_value[distance + distribution_size] + 1
                            hit_flag = True
                        if stype == "all":
                            count_value[distance + distribution_size] = count_value[distance + distribution_size] + 1
                            hit_flag = True

                if hit_flag :
                    merged_data.append({'pan': pan, 'gm': gm, 'chr': row['chr'], 'reference_start': start, 'reference_strand': strand,
                        'seqid': row['seq.id'], 'element_start': row['start'], 'element_end': row['end'], 'element_strand': row['strand'], 'seq': row['seq']})

# At this point, count_value contains the count of distances within the desired range
# Rest of your code for plotting or processing count_value as needed


# At this point, count_value contains the count of distances within the desired range

# Rest of your code for plotting or processing count_value as needed

x = range(distribution_size_neg,distribution_size + 1)
y = count_value

# Plot the bar chart
plt.bar(x, y, width=1, bottom=None, align='center')

# Add a title and labels to the axes
plt.title('')
plt.xlabel('Distance')
plt.ylabel('Count')

plt.xlim([distribution_size_neg, distribution_size])
plt.ylim([0, ymax])

# Find the index of the highest point (maximum Y value)
max_index = y.index(max(y))

# Get the (X, Y) coordinates of the highest point
max_x = x[max_index]
max_y = max(y)

# Annotate the highest point with its coordinates
plt.annotate(f'({max_x}, {max_y})', xy=(max_x, max_y), xytext=(max_x + 100, max_y + 10),
             arrowprops=dict(arrowstyle='->'))

# Show the plot
print("./img/size" + str(distribution_size) + "/" + species + "." + element + "." + stype + "." + gene_body + ".png")
#plt.show()
plt.savefig("./img/size" + str(distribution_size) + "/" + species + "." + element + "." + stype + "." + gene_body + ".png")
df10 = pd.DataFrame(merged_data)
df10.to_csv("./lists/size" + str(distribution_size) + "/" + species + "." + element + "." + stype + "." + gene_body + ".csv",  header=True, index=False)
