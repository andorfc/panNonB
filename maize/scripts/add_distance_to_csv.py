import pandas as pd
import sys

# Read command line arguments
if len(sys.argv) != 3:
    print("Usage: python script.py input.csv output.csv")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

# Load the CSV file
df = pd.read_csv(input_file)

# Calculate the center of the element
df['center_of_element'] = ((df['element_start'] + (df['element_end'] - df['element_start']) / 2)).astype(int)

# Define a function to calculate distance to feature based on the strand
def calculate_distance(row):
    if row['reference_strand'] == "+":
        return row['center_of_element'] - row['reference_start']
    elif row['reference_strand'] == "-":
        return row['reference_start'] - row['element_start']
    else:
        return None  # In case there are any rows with unexpected strand symbols

# Apply the function to each row
df['distance_to_feature'] = df.apply(calculate_distance, axis=1)

# Save the updated DataFrame to a new CSV file
df.to_csv(output_file, index=False)

print(f"Processed file saved as: {output_file}")
