ensemblFile= "mart_export.txt"
outputFile= 'output.txt'
correlatedPairs="most_correlated_full.txt"

geneName=[]
i=-1

#Create a dictionary of: gene name and its respective chromosome, gene name and its respective start site

GeneNameChr={}	#'key'=gene name, 'value'=chromosome
GeneNameDis={}	#'key'=gene name, 'value'=gene start site (bp)
GeneCorrelatedPairs=[]	#Ordered list of each correlated pair
GeneCorrelatedDistance=[]	#Ordered list of each pairs absolute distance
output = open(outputFile, 'w')

for line in open(ensemblFile):
	i+=1
	row=line.strip().split("\t")
	if len(row) < 8:
		continue
	geneName= row[7]
	GeneNameChr[geneName]=row[4]
	GeneNameDis[geneName]=row[2]

#Check if two genes are on the same chromosome

for line in open(correlatedPairs):
	row=line.strip().split("\t")
	if len(row) <4:
		continue
	geneA= row[0]
	geneB= row[1]
	if geneA in GeneNameChr.keys():
		if geneB in GeneNameChr.keys():
			if GeneNameChr[geneA]==GeneNameChr[geneB]:	#check if the genes are on the same chromosome
				genepair=(geneA,geneB)
				GeneCorrelatedPairs.append(genepair)		#store genes on the same chromosome in a list
	else:
		continue

print(GeneCorrelatedPairs[0])



#find the distance between each correlated gene pair

for item in GeneCorrelatedPairs:
	geneA = item[0]
	geneB = item[1]
	X= int(GeneNameDis[geneA])
	Y= int(GeneNameDis[geneB])
	Dis= abs(X-Y)
	GeneCorrelatedDistance.append(Dis)
	
#write the correlated gene pairs to an output file as a check
i=-1
for item in GeneCorrelatedPairs:
	i+=1
	output.write("{0}\t{1}\t{2}\n".format(item[0],item[1],GeneCorrelatedDistance[i]))
input("Done")
