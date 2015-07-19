library(gplots) # for plotCI
require(graphics)

library("Cairo");
CairoSVG(file = "correlations.svg",
         width = 6, height = 6, onefile = TRUE, bg = "transparent",
         pointsize = 12)
		 
#par(mfrow=c(3,3), mar=c(4,4,.4,.1))

xDataT = read.table('UBC')
yDataT = read.table('ZDHHC6')

xData = unlist(xDataT)
yData = unlist(yDataT)
		
plot(
  x <- xData,
  y <- yData,

  pch=21, # symbol (plotting character) type: see help(pch); 24 = filled triangle pointing up
#  pt.bg="black", # fill colour for symbol
  cex=1, # symbol size multiplier
  lty=1, # line type: see help(par)
  type="p", # p=points, l=lines, b=both, o=overplotted points/lines, etc.; see help(plot.default)

  xlim=c(min(xData), max(xData)), # x axis limits
#  xaxp=c(-6,9.5,0.5), # x-min tick mark, x-max tick mark, number of intervals between tick marks
  xlab='UBC Expression', # x axis label
  ylim=c(min(yData), max(yData)),
#  yaxp=c(0,100,5),
  ylab='ZDHHC6 Expression',

  las=0, # axis labels horizontal (default is 0 for always parallel to axis)
  font.lab=2, # 1 plain, 2 bold, 3 italic, 4 bold italic, 5 symbol
#  bty = "l", # box type
)

res <- lm(yData~xData);
print(res);
intercept = res$coefficients[1];
slope = res$coefficients[2];

segments(min(xData), slope*min(xData) + intercept,
		 max(xData), slope*max(xData) + intercept);
		
prediction <- predict.lm(res, as.data.frame(xData), interval="confidence",level=0.95);
topCImatrix = cbind(xData, prediction[,2]);
sortedTopCImatrix = topCImatrix[sort.list(topCImatrix[,1]),];
bottomCImatrix = cbind(xData, prediction[,3]);
sortedBottomCImatrix = bottomCImatrix[sort.list(bottomCImatrix[,1]),];

#lines(sortedBottomCImatrix[,2]~sortedBottomCImatrix[,1], col="grey");
#lines(sortedTopCImatrix[,2]~sortedTopCImatrix[,1], col="grey");

# Generate an example dataset
#		x <- c(1:10)
#		e <- rnorm(n=10,0,1)
#		y <- 5+2*x+e
#		# Fit linear regression
#		mylm <- lm(y~x)
#		# Plot observations
#		plot(y~x)
# Get confidence interval
#mypredict <- predict.lm(mylm,as.data.frame(x),interval="confidence",level=0.95)
#lines(mypredict[,1]~x,col="blue")	# fitted line
#lines(mypredict[,2]~x,col="green")	# lower CI curve
#lines(mypredict[,3]~x,col="green")	# upper CI curve
		 
pearson = round(cor(yData, xData, method="pearson"), digits=3);
spearman = round(cor(yData, xData, method="spearman"), digits=3);
pearsonTest = cor.test(yData, xData, method="pearson");
spearmanTest = cor.test(yData, xData, method="spearman");

#		text(max(xData)-(max(xData)-min(xData))*0.2, max(yData)-(max(yData)-min(yData))*0.1, paste("r = ", pearson));
#		text(max(xData)-(max(xData)-min(xData))*0.75, max(yData)-(max(yData)-min(yData))*0.1, paste("rho", " = ", spearman));
#text(max(xData)-(max(xData)-min(xData))*0.2, max(yData)-(max(yData)-min(yData))*0.2, paste("Pearson p = ", round(pearsonTest$p.value,digits=3)));
#text(max(xData)-(max(xData)-min(xData))*0.75, max(yData)-(max(yData)-min(yData))*0.2, paste("Spearman p", " = ", round(spearmanTest$p.value,digits=3)));

dev.off()
