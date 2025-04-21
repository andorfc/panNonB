# 🌽 Non-B DNA Structures in the Maize Pan-Genome

**Genome-wide Analysis of A-Phased Repeats, Direct Repeats, G-Quadruplexes, Inverted Repeats, Mirror Repeats, Short Tandem Repeats, and Z-DNA across 26 Maize Genomes**

This repository provides datasets, scripts, and tools used in our pan-genome-wide analysis of non-B DNA structures in maize, focusing on their distribution, conservation, and functional relevance across the B73 reference genome and 25 NAM founder lines.

---

## 🧬 Project Overview

Non-B DNA structures differ from canonical B-form DNA and contribute to genome regulation, chromatin accessibility, and genetic stability. This project systematically characterizes seven types of non-B DNA motifs across 26 maize genomes:

- **A-Phased Repeats (APR)**
- **Direct Repeats (DR)**
- **G-Quadruplexes (GQ)**
- **Inverted Repeats (IR)**
- **Mirror Repeats (MR)**
- **Short Tandem Repeats (STR)**
- **Z-DNA motifs**

These elements were mapped, quantified, and analyzed in gene bodies, promoters, chromatin regions, and TF-binding sites. Outputs are provided as downloadable data and genome browser tracks at [MaizeGDB](https://www.maizegdb.org/).

---

## 📁 Repository Structure

```text
non-B-DNA-atlas/maize/
│
├── data/                         # Reference & output files
│   ├── gff/                      # GFF files for all motifs per genome
│   ├── csv/                      # Summary CSVs per motif and genome
│   └── tracks/                   # Files for genome browser visualization
│
├── scripts/                      # Custom Python scripts for processing
│   ├── call_nonb_structures.py   # Wrapper for non-B_gfa + GFF conversion
│   ├── make_NAM_perc_figure.py   # Generates positional conservation figures
│   ├── enrichments/              # Enrichment & overlap analysis scripts
│   └── utils/                    # SNP/SV analysis, expression parsing, etc.
│
├── results/                      # Figures and summary plots
│   └── nonB_conservation_plots/  # Frequency plots by motif and region
│
├── logs/                         # Slurm job logs
│
├── README.md
└── environment.yml               # Conda environment with required packages
```

## 🗃️ Datasets
All genomes, annotations, and variation data were sourced from MaizeGDB:

- Genomes: B73 v5 reference + 25 NAM founders
- Gene models: Zm00001eb.1 annotation
- Non-B DNA motif calls: via non-B_gfa
- SNPs/INDELs: MaizeGDB 2024 High-Coverage + NAM panel
- SVs: Insertions, deletions, inversions, knobs (Hufford et al., 2021)
- TFBS / Chromatin: Ricci et al., Tu et al., ATAC-seq, DAP-seq
- Expression: B73 v5 RNA-seq from qTeller (MaizeGDB)

## ⚙️ Tools & Scripts
- 🧰 non-B_gfa – Non-B motif prediction
- 🧬 GFF & BED utilities – Conversion & coordinate normalization
- 📈 Positional conservation figures – Sliding window counts by motif and gene boundary
- 📊 Enrichment scripts – Gene ontology, domains, traits, TFs (Fisher’s exact test)
- 🧪 Variant analysis – SNP/SV enrichment in motif-overlapping regions
- 🎨 Plotting – Custom matplotlib boxplots, fold-change plots, heatmaps

## 🚀 How to Use
Run the core pipeline for a specific motif and region:

bash
Copy
Edit
python scripts/make_NAM_perc_figure.py <element_type> <region_type>
Example:

bash
Copy
Edit
python scripts/make_NAM_perc_figure.py GQ TSS
To submit many jobs via SLURM:

bash
Copy
Edit
sbatch run_make_NAM_perc_figure.sbatch
🧾 Key Findings (from the paper)
Non-B motifs make up ~15% of the maize genome

IRs and STRs are the most prevalent, but GQ and Z-DNA are highly enriched in TSS regions

Motifs are conserved across diverse NAM lines and enriched in TFBS and accessible chromatin

Non-B regions are depleted of SNPs but enriched for structural variants

Expression and GO enrichment support functional roles in stress, metabolism, and regulation

## 📢 Citation
Andorf CM, et al. (2024).
Functional Implications for Genome-Wide Analysis of Non-B DNA in Maize: Forward and Reverse Repeats, G-Quadruplex Sequences, and Z-DNA.
[Link to publication]

## 🔗 Additional Resources
- 📊 Interactive genome tracks: MaizeGDB Track Hub
- 📜 Full metadata: data/README_datasets.tsv
- 🧬 non-B_gfa GitHub
- 📖 MaizeGDB Pan-genome resources
