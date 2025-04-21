# 🧬 panNonB
A pangenome-wide workflow for the identification, distribution, conservation, and functional annotation of non-canonical DNA structures.

---

## 📚 Overview

This repository hosts data, code, and results from our comparative genomics project focused on **non-B DNA structures**, including:

- A-Phased Repeats (APR)
- Direct Repeats (DR)
- G-Quadruplexes (GQ)
- Inverted Repeats (IR)
- Mirror Repeats (MR)
- Short Tandem Repeats (STR)
- Z-DNA motifs

Our goal is to provide a standardized, pan-genome–wide resource to explore the distribution and functional impact of these motifs across agriculturally important species.

---

## 🔬 Included Species

| Species    | Folder            | Status     |
|------------|-------------------|------------|
| 🌽 Maize     | [`/maize`](./maize)           | ✅ Submitted for publication |

Each subfolder contains a species-specific README, datasets, code, and results.

---

## ⚙️ Technical Features

- Reproducible motif calling using `non-B_gfa`
- Pan-genome positional conservation analysis
- SNP/INDEL/SV enrichment
- Transcriptomic correlations (RNA-seq)
- Gene ontology, TF, domain, and trait enrichment
- Slurm-compatible batch processing

---

## 📥 How to Use

```bash
cd maize/
python scripts/make_NAM_perc_figure.py GQ TSS
