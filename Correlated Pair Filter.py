ensemblFile= "mart_export.txt"
DifferentChromosomesOutput= 'DifferentChromosomes.txt'	#File containing genes in a pair on different chromosomes
SameChromosomesOutput='SameChromosomes.txt'				#File containing genes in a pair on the same chromosome
correlatedPairs="most_correlated_full.txt"
outputSameChromosome= open(SameChromosomesOutput, 'w')	
outputDifferentChromosmes= open(DifferentChromosomesOutput, 'w')

GeneNameChr={} #'key'= gene name, 'vale'= chromosome
GeneNameDis={}	#'key'=gene name, 'value'=gene start site (bp)

#Create a dictionary of gene name and its chromosome
for line in open(ensemblFile):
	row= line.strip().split("\t")
	if len(row) <8:
		continue
	GeneNameChr[row[7]]=row[4]
input("Check")
for line in open(correlatedPairs):
	row= line.strip().split("\t")
	if len(row)<4:
		continue
	geneA= row[0]
	geneAStart= int(GeneNameDis[geneA])
	geneB= row[1]
	geneBStart= int(GeneNameDis[geneB])
	geneCorrelation= row[3]
	genePValue= row[4]
	if geneA in GeneNameChr.keys():
		if geneB in GeneNameChr.keys():
			if GeneNameChr[geneA] == GeneNameChr[geneB]:	#Check if the genes are on the same chromosome
				outputSameChromosome.write("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\n".format(geneA,geneAStart,geneB,geneBStart,GeneNameChr[geneA],geneCorrelation,genePValue))
			else:
				outputDifferentChromosomes.write("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\n".format(geneA,geneAStart,GeneNameChr[geneA],geneB,geneBStart,GeneNameChr[geneB],geneCorrelation,genePValue))
	else:
		continue