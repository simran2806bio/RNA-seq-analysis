# RNA-seq Differential Expression Analysis Using SRA/GEO Data

## Dataset
- GEO: GSE255685
- Title: Age-related transcriptomic differences in peripheral blood of adolescents with MDD
- Organism: Homo sapiens, Tissue: Peripheral blood
- Samples: 279 total (we use 6: 3 Healthy vs 3 MDD)
- Platform: NovaSeq 6000, 150bp PE
- Reference: GRCh38 (RefSeq)

## Research Question
Healthy Control vs Major Depressive Disorder (MDD)

## Pipeline
GEO -> SRA -> FASTQ -> FastQC -> Trimmomatic -> HISAT2 -> BAM -> featureCounts -> DESeq2 -> Volcano/PCA

## Tools
SRA, GEO, Ref Genome, RefSeq, Linux, RNA-seq, Python, R, Bioinformatics

---
## Step 1: MDD vs Control (4GB Laptop - Completed ✅)
**Date: Oct 2025**
- Dataset: Custom 2 vs 2 replicates (MDD vs Control)
- Pipeline: Salmon (100% mapping) -> tximport -> DESeq2 -> openxlsx
- **Result: 251,955 transcripts tested, 9 Significant DEGs (padj<0.1)**
    - 4 UP in MDD: ENST00000623070.5 (log2FC +9.27, padj 1.5e-07)
    - 5 DOWN in MDD: ENST00000448629.8 (log2FC -9.59, padj 8.5e-08)
- Files: `results/deseq2/MDD_SIGNIFICANT_DEGs_FINAL_EXCEL.xlsx`
- Performed on: 4GB RAM, WSL2, R 4.6.1 - Environment 99MiB -> 0 after restart fix

