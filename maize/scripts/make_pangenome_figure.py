#!/usr/bin/env python3
import os
import sys
import math
import pickle

import pandas as pd
import numpy as np
from difflib import SequenceMatcher
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------
# PARAMETERS & PATHS
# ------------------------------------------------------------------------
element_type = sys.argv[1]              # e.g. "promoter"
NONB         = sys.argv[2].upper()      # one of: "TSS", "CDS", "EXON", "END"
CACHE_FILE   = f"./pickle/cache_{NONB}_{element_type}.pkl"
PAN_TSV      = "./panid/MaizeGDB_maize_pangene_2020_08.tsv"
REF_CSV      = f"./lists/B73.{element_type}.data.csv"
NAM_GENOMES  = [
    "B97","CML228","CML277","CML333","CML69","HP301","Ki11","Ky21","M37W",
    "NC350","Oh43","P39","Tx303","CML103","CML247","CML322","CML52","Il14H",
    "Ki3","M162W","Mo18W","Ms71","NC358","Oh7B","Tzi8"
]
PERCENT_BINS   = list(range(0, 101, 10))
POSITION_RANGE = 10001  # for positions -5000..+5000

# ------------------------------------------------------------------------
# LOAD pan-counts (how many NAM lines per pangene)
# ------------------------------------------------------------------------
pancount = {}
pan_type = "nam"
if pan_type == "nam":
    # Open file and read in lines
    with open(PAN_TSV, 'r') as file:
        lines = file.readlines()

    # Loop through each line in the file
    for i, line in enumerate(lines):
        # Split the line by tabs
        count = 0
        if 'Zm00001eb' in line:
            count = count + 1
        if 'Zm00018ab' in line:
            count = count + 1
        if 'Zm00021ab' in line:
            count = count + 1
        if 'Zm00022ab' in line:
            count = count + 1
        if 'Zm00023ab' in line:
            count = count + 1
        if 'Zm00024ab' in line:
            count = count + 1
        if 'Zm00025ab' in line:
            count = count + 1
        if 'Zm00026ab' in line:
            count = count + 1
        if 'Zm00027ab' in line:
            count = count + 1
        if 'Zm00028ab' in line:
            count = count + 1
        if 'Zm00029ab' in line:
            count = count + 1
        if 'Zm00030ab' in line:
            count = count + 1
        if 'Zm00031ab' in line:
            count = count + 1
        if 'Zm00032ab' in line:
            count = count + 1
        if 'Zm00033ab' in line:
            count = count + 1
        if 'Zm00034ab' in line:
            count = count + 1
        if 'Zm00035ab' in line:
            count = count + 1
        if 'Zm00036ab' in line:
            count = count + 1
        if 'Zm00037ab' in line:
            count = count + 1
        if 'Zm00038ab' in line:
            count = count + 1
        if 'Zm00039ab' in line:
            count = count + 1
        if 'Zm00040ab' in line:
            count = count + 1
        if 'Zm00041ab' in line:
            count = count + 1
        if 'Zm00042ab' in line:
            count = count + 1

        pancount[int(i)]=count
# ------------------------------------------------------------------------
# LOAD & FILTER REFERENCE
# ------------------------------------------------------------------------
reference_df = pd.read_csv(REF_CSV)
reference_df = reference_df[pd.notna(reference_df["pan"])].reset_index(drop=True)

# ------------------------------------------------------------------------
# HELPERS
# ------------------------------------------------------------------------
def is_similar(s1, s2, thresh=0.9):
    if not isinstance(s1, str): s1 = ""
    if not isinstance(s2, str): s2 = ""
    return SequenceMatcher(None, s1, s2).ratio() >= thresh

def is_within(val, tgt, tol=250):
    return abs(val - tgt) <= tol

# ------------------------------------------------------------------------
# PROCESS ONE GENOME FILE → build gm_counter
# ------------------------------------------------------------------------
def process_file(fn, species, gm_counter):
    df = pd.read_csv(fn)
    df = df[pd.notna(df["pan"])]
    merged = pd.merge(reference_df, df, on="pan", how="inner")
    seen = set()
    dist_col = NONB.lower()  # "tss", "cds", "exon", or "end"
    for _, r in merged.iterrows():
        if not is_similar(r["element_sequence_x"], r["element_sequence_y"]):
            continue
        dx = r[f"distance_{dist_col}_x"]
        dy = r[f"distance_{dist_col}_y"]
        if not is_within(dx, dy):
            continue
        gid = f"{r['gm_x']}{r['element_id_x']}"
        key = (gid, species)
        if key not in seen:
            seen.add(key)
            gm_counter[gid] = gm_counter.get(gid, 0) + 1

# ------------------------------------------------------------------------
# MAIN: load or build caches
# ------------------------------------------------------------------------
if os.path.exists(CACHE_FILE):
    print(f"Loading cache from {CACHE_FILE}", flush=True)
    with open(CACHE_FILE, "rb") as pf:
        data = pickle.load(pf)
    gm_counter = data["gm_counter"]
    counters   = data["counters"]
else:
    # 1) build gm_counter
    print("Building gm_counter …", flush=True)
    gm_counter = {}
    for sp in NAM_GENOMES:
        fn = f"./master_list/{sp}.{element_type}.data.csv"
        process_file(fn, sp, gm_counter)

    # 2) build per-position counters
    print("Building counters …", flush=True)
    counters = {p: np.zeros(POSITION_RANGE, dtype=int) for p in PERCENT_BINS}

    for _, r in reference_df.iterrows():
        gid     = f"{r['gm']}{r['element_id']}"
        matches = gm_counter.get(gid, 0)
        pan_idx = int(r["pan"]) if not pd.isna(r["pan"]) else None
        denom   = pancount.get(pan_idx, 0)

        pct = (100 * matches / denom) if denom else 0.0
        pct = max(0.0, min(pct, 100.0))        # clamp
        perc = int(pct // 10) * 10             # decile bin

        # choose offset column based on NONB
        if NONB == "TSS":
            offset = r["TSS_start"]
        elif NONB == "CDS":
            offset = r["CDS_start"]
        elif NONB == "EXON":
            offset = r["INTRON1_start"]
        else:  # END
            offset = r["gm_end"]

        if r["gm_strand"] == "+":
            start = r["element_start"] - offset
            end   = r["element_end"]   - offset
        else:
            start = offset - r["element_start"]
            end   = offset - r["element_end"]

        i0 = int(start) + 5000
        i1 = int(end)   + 5000

        if 0 <= i0 <= 10000 and 0 <= i1 <= 10000:
            counters[perc][i0:i1+1] += 1

    # 3) save cache
    with open(CACHE_FILE, "wb") as pf:
        pickle.dump({
            "gm_counter": gm_counter,
            "counters":   counters
        }, pf)
    print(f"Saved cache to {CACHE_FILE}", flush=True)

# ------------------------------------------------------------------------
# PLOTTING: raw counts per bin
# ------------------------------------------------------------------------
def plot_distribution_all(outfile):
    fig, axs = plt.subplots(1, 5, figsize=(30, 4), sharey=True,
                            gridspec_kw={"wspace": 0.15})
    bins = [(0,20), (20,40), (40,60), (60,80), (80,100)]
    xvals = np.arange(-5000, 5001)

    for ax, (lo, hi) in zip(axs, bins):
        summed = np.zeros(POSITION_RANGE, dtype=int)
        for p in range(lo, hi+1, 10):
            summed += counters.get(p, 0)

        ax.bar(xvals, summed, width=1.0)
        ax.axvline(0, color='grey', linestyle='--')
        ax.set_xlim(-2000, 2000)
        ax.set_xticks([])
        ax.set_title(f"{lo}–{hi}%")

    plt.tight_layout()
    plt.savefig(outfile)
    plt.close()

# ------------------------------------------------------------------------
# RUN
# ------------------------------------------------------------------------
print("Plotting …", flush=True)
plot_distribution_all(f"{element_type}_{NONB}_perc_All_counts.png")
print("Done.", flush=True)
