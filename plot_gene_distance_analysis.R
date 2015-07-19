data <- read.table('output_gene_distance_analysis.txt', header=FALSE)

library(hexbin)
library(RColorBrewer)
library(Cairo)

rf <- colorRampPalette(rev(brewer.pal(11,'RdYlBu')))

y = data[, 5]
x = data[, 3]
df = data.frame(x, y)
df = df[order(x), ]

#p <- hexbinplot(y~x, data=df, ylab='test', xbins=30, colramp = rf)
#print(p)

CairoPNG(file = 'gene_distance_analysis_log-pval.png', width = 2000, height = 1000, onefile = TRUE, bg = 'white', pointsize = 10, dpi=150)
plot(data[, 3], log(data[, 5]), pch=20, col=rgb(.5, .5, .5, alpha=0.1), ylab='log(p-value) of correlation', xlab='Distance between genes (bp)')
dev.off()

CairoPNG(file = 'gene_distance_analysis_correlation-coefficients.png', width = 2000, height = 1000, onefile = TRUE, bg = 'white', pointsize = 10, dpi=150)
plot(data[, 3], data[, 4], pch=20, col=rgb(.5, .5, .5, alpha=0.03), ylab='log(p-value) of correlation', xlab='Distance between genes (bp)')
dev.off()

CairoPNG(file = 'gene_distance_analysis_segment.png', width = 2000, height = 1000, onefile = TRUE, bg = 'white', pointsize = 10, dpi=150)
plot(df[1:20000, 1], log(df[1:20000, 2]), pch=20, col=rgb(.5, .5, .5, alpha=0.5), ylab='log(p-value) of correlation', xlab='Distance between genes (bp)')
dev.off()
