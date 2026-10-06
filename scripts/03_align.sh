#!/bin/bash
# Step 3: Salmon quantification (GENCODE v44)
salmon index -t gencode.v44.transcripts.fa -i salmon_index/
salmon quant -i salmon_index/ -l A -r data/fastq/sample.fastq -o results/salmon/
