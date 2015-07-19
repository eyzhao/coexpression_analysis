geneFile = open('mart_export.txt')
numLines = sum(1 for line in open('mart_export.txt'))

header = geneFile.next().strip().split('\t')

chromosomeIndex = header.index('Chromosome Name')
geneNameIndex = header.index('Associated Gene Name')
startPosIndex = header.index('Gene Start (bp)')
endPosIndex = header.index('Gene End (bp)')

chrHash = {}
outputHash = {}

outputFile = open('gene_distances.txt', 'w')

counter = 1
for line in geneFile:
    if counter % 1000 == 0:
        print '{0} / {1}'.format(counter, numLines)
    counter += 1

    split = line.strip().rstrip('\n').split('\t')

    chr = split[chromosomeIndex]
    if not chr == '1':
        continue

    geneName = split[geneNameIndex]
    if not geneName.strip():
        continue

    if not chr in chrHash:
        chrHash[chr] = {}
        outputHash[chr] = []

    startPos = int(split[startPosIndex])
        
    for otherGene in chrHash[chr]:
        distance = abs(chrHash[chr][otherGene] - startPos)
        outputRow = [chr, geneName, otherGene, str(distance)]
        outputFile.write('\t'.join(outputRow) + '\n')

    chrHash[chr][geneName] = int(split[startPosIndex])

outputFile.close()
