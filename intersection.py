# Christos Brentas, A.M: 4442

rSorted = open('R_sorted.tsv')
sSorted = open('S_sorted.tsv')
outputFile = open('RintersectionS.tsv', 'w+')

rSortedLine = rSorted.readline()
sSortedLine = sSorted.readline()
# Variable to check for doubles
temp = ''


while rSortedLine != '' and sSortedLine != '':


    rSplit = rSortedLine.split('\t')
    sSplit = sSortedLine.split('\t')

    # Go next line on R and write if it does not equal @temp
    if rSplit[0] < sSplit[0]:
        rSortedLine = rSorted.readline()
        rSplit = rSortedLine.split('\t')

    # Go next line on S and write if it does not equal @temp
    elif rSplit[0] > sSplit[0]:
        sSortedLine = sSorted.readline()
        sSplit = sSortedLine.split('\t')


    elif rSplit[0] == sSplit[0]:

        # In case keys are the same, in order to avoid missing any doubles
        # we iterate lines depending on value and not key as done above

        if rSplit[1] < sSplit[1]:
            rSortedLine = rSorted.readline()
            rSplit = rSortedLine.split('\t')
        elif rSplit[1] > sSplit[1]:
            sSortedLine = sSorted.readline()
            sSplit = sSortedLine.split('\t')

        elif rSortedLine == sSortedLine and rSortedLine != temp:
            outputFile.write(rSortedLine)
            temp = rSortedLine
            sSortedLine = sSorted.readline()
            sSplit = sSortedLine.split('\t')



rSorted.close()
sSorted.close()
outputFile.close()