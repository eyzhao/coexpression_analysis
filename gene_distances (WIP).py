ensemblFile= "mart_export.txt"
outputFile= 'output1.txt'
correlatedPairs="most_correlated_full.txt"

geneName=[]
i=-1

#Create a dictionary of: gene name and its respective chromosome, gene name and its respective start site

GeneNameChr={}	#'key'=gene name, 'value'=chromosome
GeneNameDis={}	#'key'=gene name, 'value'=gene start site (bp)
GeneCorrelatedPairs=[]	#Ordered list of each correlated pair
GenePairDistance=[]
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
#input("Check1")

for line in open(correlatedPairs):
	row=line.strip().split("\t")
	if len(row) <4:
		continue
	geneA= row[0]
	geneB= row[1]
	if geneA in GeneNameChr.keys():
		if geneB in GeneNameChr.keys():
			if GeneNameChr[geneA]==GeneNameChr[geneB]:	#check if the genes are on the same chromosome
				X= int(GeneNameDis[geneA])				
				Y= int(GeneNameDis[geneB])
				Dis= abs(X-Y)
				genepair=(geneA,geneB,Dis)
				#print(genepair)
				if Dis <= 10000:
					#input("Check")
					GenePairDistance.append(genepair)		#Create a nested tuple inside a larger list
				else:
					continue
			else:
				continue
		else:
			continue
	else:
		continue



input("Check")

#write the correlated gene pairs to an output file as a check

for item in GenePairDistance:
		output.write("{0}\t{1}\t{2}\n".format(item[0],item[1],item[2]))
input("Done")
