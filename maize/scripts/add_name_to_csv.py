import pandas as pd
import sys

csv_filename = sys.argv[1]
species = sys.argv[2]
type_ = sys.argv[3]  # type is a reserved keyword in Python, hence type_
inpath = sys.argv[4]
outpath = sys.argv[5]
formal_name = sys.argv[6]

#df_csv = pd.read_csv(inpath + csv_filename)
df_csv = pd.read_csv(inpath + csv_filename, names=['chrom', 'start', 'end', 'strand', 'sequence'])

df_csv['name'] = [f"{species}.{type_}.{str(i+1).zfill(6)}" for i in range(len(df_csv))]

df_csv.to_csv(outpath + csv_filename, index=False)
df_csv.to_csv(outpath + formal_name, index=False)
