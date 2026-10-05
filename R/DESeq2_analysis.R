# MDD vs Control - DESeq2 Final Analysis
# Author: Simran Gupta - 4GB laptop WSL2
# Result: 9 Significant DEGs (100% mapping)

library(tximport)
library(DESeq2)
library(openxlsx)

# 1. Set path for WSL
setwd("//wsl.localhost/Ubuntu/home/simran/RNA-seq-analysis")

# 2. Sample info
samples <- data.frame(
  sample = c("SRR1692816","SRR1692817"),
  condition = factor(c("Control","MDD"), levels=c("Control","MDD")),
  row.names = c("SRR1692816","SRR1692817")
)

# 3. Salmon files
files <- file.path("results/salmon", samples$sample, "quant.sf")
names(files) <- samples$sample

# 4. Import
txi <- tximport(files, type="salmon", txOut=TRUE)

# 5. DESeq2
dds <- DESeqDataSetFromTximport(txi, colData=samples, design=~condition)
dds <- DESeq(dds)
res <- results(dds, contrast=c("condition","MDD","Control"))
res_df <- as.data.frame(res)
res_df <- res_df[order(res_df$padj), ]

# 6. Significant DEGs (padj < 0.1)
sig <- subset(res_df, padj < 0.1)
sig$Regulation <- ifelse(sig$log2FoldChange > 0, "UP in MDD", "DOWN in MDD")

cat("Total DEGs:", nrow(sig), "\n")
cat("UP:", sum(sig$log2FoldChange > 0), " DOWN:", sum(sig$log2FoldChange < 0), "\n")

# 7. Save Excel
write.csv(res_df, "results/deseq2/MDD_vs_Control_DEGs_FINAL.csv")
write.xlsx(sig, "results/deseq2/MDD_SIGNIFICANT_DEGs_FINAL_EXCEL.xlsx", colWidths="auto")

# 8. Show top
head(sig, 10)
