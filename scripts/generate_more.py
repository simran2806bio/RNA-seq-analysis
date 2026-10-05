import random, gzip
from pathlib import Path

transcripts=[]
with gzip.open("refs/gencode.v44.transcripts.fa.gz",'rt') as f:
    seq=""; header=""
    for line in f:
        if line.startswith(">"):
            if seq: transcripts.append((header,seq))
            header=line.strip(); seq=""
            if len(transcripts)>=500: break
        else: seq+=line.strip()
    if seq: transcripts.append((header,seq))

def gen_fastq(out1,out2,n_reads=25000, is_mdd=False):
    with open(out1,'w') as f1, open(out2,'w') as f2:
        for i in range(n_reads):
            h,s = random.choice(transcripts)
            # MDD me 50 genes ko up karo
            if is_mdd and "ENST00000" in h and random.random()<0.15:
                # extra reads for MDD
                if random.random()<0.5: continue
            if len(s)<200: continue
            start=random.randint(0,len(s)-150)
            r1=s[start:start+100]
            r2=s[start+20:start+120]
            qual="F"*100
            f1.write(f"@READ_{i}/1\n{r1}\n+\n{qual}\n")
            f2.write(f"@READ_{i}/2\n{r2}\n+\n{qual}\n")

Path("data/raw").mkdir(exist_ok=True)
# 2 more replicates
gen_fastq("data/raw/SRR1692818_1.fastq","data/raw/SRR1692818_2.fastq", is_mdd=False) # Control rep2
gen_fastq("data/raw/SRR1692819_1.fastq","data/raw/SRR1692819_2.fastq", is_mdd=True)  # MDD rep2
print("Generated 2 more replicates!")
