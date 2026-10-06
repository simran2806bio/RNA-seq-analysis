#!/bin/bash
# Step 1: Download test data - GSE255685
# Note: Original SRR6357070 was yeast (taxid 4932), so we used synthetic human reads
# fastq-dump --split-files SRR6357070
python3 scripts/generate_human_reads.py
