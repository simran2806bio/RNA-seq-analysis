# RNA-seq Differential Expression Analysis: MDD vs Control

> End-to-end RNA-seq pipeline on 4GB RAM laptop (WSL2 + RStudio) - from FASTQ to DEG Excel report.

## Overview
Complete RNA-seq workflow for Major Depressive Disorder (MDD). Documents real challenge: 0% mapping due to yeast test data (taxid 4932) → 100% mapping with synthetic human reads.

## Pipeline
FASTQ -> FastQC -> Salmon -> tximport -> DESeq2 -> Excel

## Final Results
- Salmon: 100.00% mapping (24,099 / 24,099)
- DESeq2: 251,955 transcripts tested, 9 Significant DEGs (padj<0.1)
    - 4 UP in MDD: ENST00000623070.5 (log2FC +9.27, padj 1.5e-07)
    - 5 DOWN in MDD: ENST00000448629.8 (log2FC -9.59, padj 8.5e-08)
- - File: [results/deseq2/MDD_SIGNIFICANT_DEGs_FINAL_EXCEL.xlsx](results/deseq2/MDD_SIGNIFICANT_DEGs_FINAL_EXCEL.xlsx)

Disclaimer: DEG file in results/ is from a synthetic human-reads validation run created after discovering the test FASTQ was yeast. It demonstrates the full DESeq2 workflow, not differential expression from GSE255685's 279 samples.

## Troubleshooting
See docs/TROUBLESHOOTING.md - Yeast vs Human issue explained.

## Author
Simran Gupta - Bioinformatics - Agra, India


> Last updated: 6 Oct 2026 - Final lightweight version with 9 DEGs
