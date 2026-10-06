#!/bin/bash
# Step 2: QC with FastQC
fastqc data/fastq/*.fastq -o results/qc/
multiqc results/qc/ -o results/qc/
