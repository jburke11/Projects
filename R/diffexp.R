library("DESeq2")
cts <- as.matrix(read.csv("/Users/burkej24/Desktop/SRR11012008.csv",row.names = "tracking_id"))
coldata <- read.csv("/Users/burkej24/Desktop/coldata.csv", row.names=1)
coldata <- coldata[,c("condition", "type")]
dds <- DESeqDataSetFromMatrix(countData = cts,
                              colData = coldata,
                              design = ~ condition)
dds <-DESeq(dds)
res <- results(dds)
plotMA(res, ylim=c(-2,2))

summary(res)
sum(res$padj < 0.1, na.rm=TRUE)
