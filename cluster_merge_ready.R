tbl = read.table('union_for_cluster_test_new.txt',header = TRUE,  sep = '\t',row.names= 1)
library(gplots)
hc.rows <- hclust(as.dist((1-cor(t(tbl)))))
hc.cols <- hclust(dist(t(tbl)))
grp = cutree(hc.cols,h = 20)
output_table<-c()
for (i in 1:max(grp)){
  output = colnames(tbl[grp == i])
  cat(i,output,"\n", file = "output_new.txt", append = TRUE, sep = '\t')
}
