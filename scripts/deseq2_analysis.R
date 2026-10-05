library(tximport)
library(DESeq2)

samples <- data.frame(
  sample = c("SRR1692816","SRR1692817"),
  condition = c("Control","MDD"),
  row.names = c("SRR1692816","SRR1692817")
)

files <- file.path("results/salmon", samples$sample, "quant.sf")
names(files) <- samples$sample

tx2gene <- read.csv("refs/gencode.v44.tx2gene.csv", header=FALSE)
colnames(tx2gene) <- c("TXNAME","GENEID")

txi <- tximport(files, type="salmon", tx2gene=tx2gene, ignoreTxVersion=TRUE)

dds <- DESeqDataSetFromTximport(txi, colData=samples, design=~condition)
dds <- DESeq(dds)
res <- results(dds, contrast=c("condition","MDD","Control"))
resOrdered <- res[order(res$padj),]
write.csv(as.data.frame(resOrdered), "results/deseq2/MDD_vs_Control_DEGs.csv")
print(head(resOrdered, 20))
