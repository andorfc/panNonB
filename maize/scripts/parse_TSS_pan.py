# Import the required libraries
import pandas as pd
import sys
import re

# Set up empty dictionary
my_dict = {}

# Open file and read in lines
with open('./panid/MaizeGDB_maize_pangene_2020_08.tsv', 'r') as file:
    lines = file.readlines()

# Loop through each line in the file
for i, line in enumerate(lines):
    # Split the line by tabs
    values = re.split("\s+", line)
    # iterate over the array using a for loop
    for word in values:
        # print each word on a separate line
        my_dict[word] = i

# Read the GFF file and create a DataFrame
df = pd.read_csv(sys.argv[1], sep='\t', header=None, names=['chr', 'source', 'feature', 'start', 'end', 'score', 'strand', 'frame', 'attributes'])


# Filter the DataFrame to include only rows where the 'feature' column is 'gene'
df = df[df['feature'] == 'mRNA']

# Create a new column called 'start_pos'
df['start_pos'] = df['start']

# Set the value of 'start_pos' based on the value of 'strand'
df.loc[df['strand'] == '+', 'start_pos'] = df['start']
df.loc[df['strand'] == '-', 'start_pos'] = df['end']

# Print the resulting dataframe
#print(df)



df[['attr_1','attr_2','attr_3','attr_4','attr_5']] = df['attributes'].str.split(';', expand=True)
delimeter='_='
df[['gm_name','gm','trans']] = df['attr_1'].str.split('[' + delimeter + ']', expand=True)

df = df[df['trans'] == 'T001']

df["pan_id"] = df["gm"].map(my_dict)
df['pan_id'] = df['pan_id'].fillna(-1).astype(int).astype(str)

# Extract the 'chr' and 'start' columns
df = df[['pan_id', 'gm','chr', 'start_pos','strand']]
# Convert the 'start' column to an integer
df['start_pos'] = df['start_pos'].astype(int)

# Write the DataFrame to a CSV file
df.to_csv(sys.argv[2], header=False, index=False)
