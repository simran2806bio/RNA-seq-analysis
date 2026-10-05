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
