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
│   ├── annotations/              # Gene model annotations (GFF)
│   ├── gff/                      # GFF files for all motifs per genome
│   ├── csv/                      # Summary CSVs per motif and genome
│   ├── counts/                   # Counts of overlaps
│   ├── fa/                       # Chromosome FASTA files
│   ├── TF/                       # Transcript factor binding or other regulatory feature peaks BED files
│   ├── fa/                       # Chromosome FASTA filessualization
│   └── vcf/                      # VCF files
|
├── tss_pan/                      # The TSS positions for the pan-gene member in a given genome
├── cds_pan/                      # The CDS positions for the pan-gene member in a given genome
├── exon_pan/                     # The EXON positions for the pan-gene member in a given genome
├── end_pan/                      # The END positions for the pan-gene member in a given genome
|
├── lists/                        # Contains CSV lists of distribution sizes that can be used for analysis or figures
|
├── pickle/                       # Pickle files for improved performance
|
├── scripts/                      # Custom shell scripts for batch processing
│   ├── names.sh                  # Add Names to the nonB predictions
│   ├── parse_TSS_pan.sh          # Create the TSS positions for the pan-gene member in a given genome
│   ├── parse_CDS_pan.sh          # Create the CDS positions for the pan-gene member in a given genome
│   ├── parse_EXON_pan.sh         # Create the EXON positions for the pan-gene member in a given genome
│   ├── parse_END_pan.sh          # Create the END positions for the pan-gene member in a given genome
│   ├── del.sh                    # Calcuulate deletion frequencies
│   ├── ins.sh                    # Calcuulate insertion frequencies
│   ├── SNPS.sh                   # Get SNP frequencies
│   ├── pickle_NonB.sh            # Make pickle file for NonB elements
│   ├── pickle_SNPs.sh            # Make pickle file for SNPS
│   └── distribution_loop.sh      # Makes CSV lists of distribution sizes that figures

|
├── scripts/                         # Custom Python scripts for processing
│   ├── add_distance_to_csv.py       # Add distance from nonB-element to gene feature
│   ├── call_nonb_structures.py      # Wrapper for non-B_gfa + GFF conversion
│   ├── make_NAM_perc_figure.py      # Generates positional conservation figures
│   ├── parse_TSS_pan.py             # Create the TSS positions for the pan-gene member in a given genome
│   ├── parse_CDS_pan.py             # Create the CDS positions for the pan-gene member in a given genome
│   ├── parse_EXON_pan.py            # Create the EXON positions for the pan-gene member in a given genome
│   ├── parse_END_pan.py             # Create the END positions for the pan-gene member in a given genome
│   ├── make_distribution_lowmem.py  # Makes CSV lists of distribution sizes that figures
│   ├── del.py                       # Calcuulate deletion frequencies
│   ├── ins.py                       # Calcuulate insertion frequencies
│   ├── get_SNP_freqs_all.py         # Get SNP frequencies
│   ├── pickleNonB.py                # Make pickle file for NonB elements
│   ├── pickleSNPs.py                # Make pickle file for SNPS
│   └── utils/                       # SNP/SV analysis, expression parsing, etc.
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

- [Genomes](https://download.maizegdb.org/Genomes/NAM_Founders/): B73 v5 reference + 25 NAM founders
- [Gene models](https://download.maizegdb.org/Genomes/NAM_Founders/): Zm00001eb.1 annotation
- [Non-B DNA motif calls](https://ars-usda.app.box.com/v/maizegdb-public/folder/230993831603): via non-B_gfa
- [SNPs/INDELs](https://ars-usda.app.box.com/v/maizegdb-public/folder/255390517505): MaizeGDB 2024 High-Coverage + NAM panel
- [SVs](https://ars-usda.app.box.com/v/maizegdb-public/folder/165655341912): Insertions, deletions, inversions, knobs (Hufford et al., 2021)
- [TF Binding sites / Chromatin](https://ars-usda.app.box.com/v/maizegdb-public/folder/165408692531): Ricci et al., Tu et al., ATAC-seq, DAP-seq
- [Expression](https://ars-usda.app.box.com/v/maizegdb-public/folder/165363728937): B73 v5 RNA-seq from qTeller (MaizeGDB)

## ⚙️ Tools & Scripts
- 🧰 non-B_gfa – Non-B motif prediction
- 🧬 GFF & BED utilities – Conversion & coordinate normalization
- 📈 Positional conservation figures – Sliding window counts by motif and gene boundary
- 📊 Enrichment scripts – Gene ontology, domains, traits, TFs (Fisher’s exact test)
- 🧪 Variant analysis – SNP/SV enrichment in motif-overlapping regions
- 🎨 Plotting – Custom matplotlib boxplots, fold-change plots, heatmaps

## 🚀 How to Use

Set up the conda environment

<pre> conda env create -f environment.yml  </pre>

Run the non_B GFA code

<pre> ./gfa -skipWGET -seq ./data/fa/chr1.fa -out ./data/csv/maize_chr1  </pre>

Add Names to the nonB predictions

<pre> ./shell/names.sh  </pre>

Make CSV files of gene model positions (Get data as *.gff3.gz from[ MaizeGDB](https://download.maizegdb.org/Genomes/)
<pre>./shell/parse_TSS_pan.sh
./shell/parse_END_pan.sh
./shell/parse_exon_pan.sh
./shell/parse_CDS_pan.sh  </pre>

Calculate and make iamges for distributions of elements against gene features

<pre> ./shell/dist_loop.sh  </pre>

Add distance to feature to CSV files:

<pre> python ./scripts/add_distance_to_csv.py ./lists/B73.APR.tss.csv ./lists/B73.APR.tss.distance.csv  </pre>

Find intersections with epigentics and DNA binding features with each non-B element (APR, DR, GQ, IR, MR, STR, Z)

<pre> bedtools intersect -a ./data/TF/EREB138.bed -b ./GFF/B73/APR.gff -c  </pre>


Make Pickle files for improved performance
<pre> ./shell/pickle_NONB.sh ./gff/Zm-B73-REFERENCE-NAM-5.0_GQ.gff ./pickle/B73_GQ.pkl  </pre>
<pre> ./shell/pickle_SNPS.sh ../vcf/chr10_clean.vcf ./pickle/B73_SNP_chr10.pkl

Find  intesections with non-B elemetns and SNP data
<pre> ./shell/SNPS.sh ./pickle/B73_GQ.pkl ./pickle/B73_SNP_HQ_chr10.pkl ./data/counts/B73_GQ_HQ_chr10_snps.tsv  </pre>
<pre> ./shell/ins.sh ./pickle/B73_GQ.pkl ./pickle/B73_SNP_HQ_chr10.pkl ./data/counts/B73_GQ_HQ_chr10_ins.tsv  </pre>
<pre> ./shell/del.sh ./pickle/B73_GQ.pkl ./pickle/B73_SNP_HQ_chr10.pkl ./data/counts/B73_GQ_HQ_chr10_del.tsv  </pre>


Make INDEL files

<pre> ./my_ins.sh ../WGS_chr/final_validate/chr1_high_quality.vcf  ./ins/chr1_ins.vcf  </pre>
<pre> ./my_del.sh ../WGS_chr/final_validate/chr1_high_quality.vcf  ./del/chr1_del.vcf  </pre>
<pre> ./my_pickle_SNPS.sh ./ins/chr1_ins.vcf ./ins/chr1_ins.pkl  </pre>
<pre> ./my_pickle_SNPS.sh ./del/chr1_del.vcf ./del/chr1_del.pkl  </pre>

<pre> ./my_MB_all.sh ./pickle/B73_APR.pkl ./ins/  ./snp_counts_NAM//B73_APR_HQ_MBFreq_INS_fast.tsv  </pre>
<pre> ./my_MB_all.sh ./pickle/B73_APR.pkl ./del/  ./snp_counts_NAM//B73_APR_HQ_MBFreq_DEL_fast.tsv  </pre>

<pre> ./my_SV_pickle.sh ./SVS/Zm-B97-REFERENCE-NAM-1.0_SV_knobs_centromeres_vs_B73_coordinates.bed ./SV_pickle/B97  </pre>
<pre> ./my_MB_all.sh ./pickle/B73_APR.pkl ./INS_pickle/  ./snp_counts_NAM//B73_APR_HQ_MBFreq_SV_INS_fast.tsv  </pre>
<pre> ./my_MB_all.sh ./pickle/B73_APR.pkl ./INV_pickle/  ./snp_counts_NAM//B73_APR_HQ_MBFreq_SV_INV_fast.tsv  </pre>
<pre> ./my_MB_all.sh ./pickle/B73_APR.pkl ./DEL_pickle/  ./snp_counts_NAM//B73_APR_HQ_MBFreq_SV_DEL_fast.tsv  </pre>
<pre> ./my_MB_all.sh ./pickle/B73_APR.pkl ./KNOB_pickle/  ./snp_counts_NAM//B73_APR_HQ_MBFreq_SV_KNOB_fast.tsv  </pre>


<pre> ./shell/my_pickle_NONB_atlas.sh ./Zm-B73-REFERENCE-NAM-5.0/Zm-B73-REFERENCE-NAM-5.0_GQ.gff ./pickle/B73_GQ.pkl  </pre>

<pre> ./my_SNPS_atlas.sh ./pickle/B73_GQ.pkl ./pickle/B73_SNP_chr10.pkl ./counts/B73_GQ_chr10.tsv  </pre>


## 🧾 Key Findings (from the paper)
- Non-B motifs make up ~15% of the maize genome
- IRs and STRs are the most prevalent, but GQ and Z-DNA are highly enriched in TSS regions
- Motifs are conserved across diverse NAM lines and enriched in TFBS and accessible chromatin
- Non-B regions are depleted of SNPs but enriched for structural variants
- Expression and GO enrichment support functional roles in stress, metabolism, and regulation

## 📢 Citation
Andorf CM, et al. (2024).
Functional Implications for Genome-Wide Analysis of Non-B DNA in Maize: Forward and Reverse Repeats, G-Quadruplex Sequences, and Z-DNA.

## 🔗 Additional Resources
- 📊 [MaizeGDB Genome Browser](https://jbrowse.maizegdb.org/)
- 🧬 [non-B_gfa GitHub](https://github.com/abcsFrederick/non-B_gfa)
- 🌽 [NAM genome project](https://maizegdb.org/NAM_project)
- 📖 [MaizeGDB Pan-genome resources](https://maizegdb.org/genome)
