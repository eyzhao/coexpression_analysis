import linecache
from scipy import stats

ccleFilename = "CCLE_Expression_Entrez_2012-09-29.gct"
interactionsFilename = "interacts-with.txt"
outputFilename = "output.txt"

fileLineDict = {}

i=-1
for line in open(ccleFilename):
    i += 1
    row = line.strip().split("\t")
    if len(row) < 10:
        continue

    geneName = row[1]
    fileLineDict[geneName] = i

# use the linecache to be able to search on the data effectively

interactionsFile = open(interactionsFilename)

output = open(outputFilename, 'w')

i = 0
for line in interactionsFile:
    if i % 1000 == 0:
        print i

    if not line.strip():
        continue

    row = line.strip().split("\t")

    geneA = row[0]
    geneB = row[2]

    if geneA in fileLineDict and geneB in fileLineDict:
        lineA = linecache.getline(ccleFilename, fileLineDict[geneA] + 1).split("\t")
        lineB = linecache.getline(ccleFilename, fileLineDict[geneB] + 1).split("\t")

        if not geneA == lineA[1] or not geneB == lineB[1]:
            print geneA
            print lineA[1]
            print "ERROR"
            continue

        x = [float(a) for a in lineA[2:len(lineA)]]
        y = [float(a) for a in lineB[2:len(lineB)]]
        
        spearmanCoefficient = stats.spearmanr(x, y)
        output.write("{0}\t{1}\t{2}\t{3}\n".format(geneA, geneB, spearmanCoefficient[0], spearmanCoefficient[1]))

    i += 1

output.close()
