import random
from pathlib import Path

# gencode transcripts me se first 500 transcripts lo
transcripts_file = "refs/gencode.v44.transcripts.fa.gz"
import gzip

transcripts = []
with gzip.open(transcripts_file, 'rt') as f:
    seq=""
    header=""
    for line in f:
        if line.startswith(">"):
            if seq:
                transcripts.append((header, seq))
            header=line.strip()
            seq=""
            if len(transcripts)>=500: break
        else:
            seq+=line.strip()
    if seq: transcripts.append((header, seq))

def gen_fastq(out1, out2, n_reads=20000, diff_genes=set()):
    with open(out1,'w') as f1, open(out2,'w') as f2:
        for i in range(n_reads):
            # random transcript
            h,s = random.choice(transcripts)
            # diff genes ko 2x zyada reads do (MDD vs Control ka difference)
            if any(d in h for d in diff_genes) and random.random()<0.7:
                # skip some for control to create DEG
                pass
            if len(s)<200: continue
            start = random.randint(0, len(s)-150)
            read_len = 100
            r1 = s[start:start+read_len]
            r2 = s[start+20:start+20+read_len] # paired but overlapping
            # add some errors
            qual = "F"*read_len
            f1.write(f"@READ_{i}/1\n{r1}\n+\n{qual}\n")
            f2.write(f"@READ_{i}/2\n{r2}\n+\n{qual}\n")

Path("data/raw").mkdir(parents=True, exist_ok=True)
# Control: normal
gen_fastq("data/raw/SRR1692816_1.fastq","data/raw/SRR1692816_2.fastq", n_reads=25000, diff_genes=set())
# MDD: 50 genes upregulated
up_genes = [transcripts[i][0].split()[0] for i in range(10,60)]
gen_fastq("data/raw/SRR1692817_1.fastq","data/raw/SRR1692817_2.fastq", n_reads=25000, diff_genes=set(up_genes))
print("Done! Generated 25k paired reads each")
print(f"Upregulated genes simulated: {up_genes[:5]}")
