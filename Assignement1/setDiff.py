# Christos Brentas, A.M: 4442

rSorted = open('R_sorted.tsv')
sSorted = open('S_sorted.tsv')
outputFile = open('RdifferenceS.tsv', 'w+')

rSortedLine = rSorted.readline()
sSortedLine = sSorted.readline()
temp = ''


while rSortedLine != '' and sSortedLine != '':


    rSplit = rSortedLine.split('\t')
    sSplit = sSortedLine.split('\t')

    if rSplit[0] < sSplit[0]:
        if rSortedLine == temp:
            rSortedLine = rSorted.readline()
            rSplit = rSortedLine.split('\t')
        else:
            outputFile.write(rSortedLine)
            temp = rSortedLine
            rSortedLine = rSorted.readline()
            rSplit = rSortedLine.split('\t')

    elif rSplit[0] > sSplit[0]:
            sSortedLine = sSorted.readline()
            sSplit = sSortedLine.split('\t')

    elif rSplit[0] == sSplit[0]:
        if rSplit[1] < sSplit[1]:
            if rSortedLine == temp:
                sSortedLine = sSorted.readline()
                sSplit = sSortedLine.split('\t')
            else:
                outputFile.write(rSortedLine)
                temp = rSortedLine
                rSortedLine = rSorted.readline()
                rSplit = rSortedLine.split('\t')
        elif rSplit[1] > sSplit[1]:
            sSortedLine = sSorted.readline()
            sSplit = sSortedLine.split('\t')
        elif rSortedLine == sSortedLine:
            rSortedLine = rSorted.readline()
            rSplit = rSortedLine.split('\t')


rSorted.close()
sSorted.close()
outputFile.close()