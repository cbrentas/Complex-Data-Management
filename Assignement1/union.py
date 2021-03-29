# Christos Brentas, A.M: 4442

rSorted = open('R_sorted.tsv')
sSorted = open('S_sorted.tsv')
outputFile = open('RunionS.tsv', 'w+')
rSortedLine = rSorted.readline()
sSortedLine = sSorted.readline()
# Variable to check for doubles
temp = ''

while rSortedLine != '' or sSortedLine != '':

    rSplit = rSortedLine.split('\t')
    sSplit = sSortedLine.split('\t')

    # Go next line on R and write if it does not equal @temp
    if rSplit[0] < sSplit[0]:
        if rSortedLine == temp:
            rSortedLine = rSorted.readline()
            rSplit = rSortedLine.split('\t')
        else:
            outputFile.write(rSortedLine)
            temp = rSortedLine
            rSortedLine = rSorted.readline()
            rSplit = rSortedLine.split('\t')


    # Go next line on S and write if it does not equal @temp
    elif rSplit[0] > sSplit[0]:

        if sSortedLine == temp:
            sSortedLine = sSorted.readline()
            sSplit = sSortedLine.split('\t')
        else:
            outputFile.write(sSortedLine)
            temp = sSortedLine
            sSortedLine = sSorted.readline()
            sSplit = sSortedLine.split('\t')


    elif rSplit[0] == sSplit[0]:
        if sSortedLine == temp:
            sSortedLine = sSorted.readline()
            sSplit = sSortedLine.split('\t')
        elif rSortedLine == temp:
            rSortedLine = rSorted.readline()
            rSplit = rSortedLine.split('\t')

        # In case keys are the same, in order to avoid missing any doubles
        # we iterate lines depending on value and not key as done above
        else:
            if rSplit[1] < sSplit[1]:
                outputFile.write(rSortedLine)
                temp = rSortedLine
                rSortedLine = rSorted.readline()
                rSplit = rSortedLine.split('\t')
            elif rSplit[1] > sSplit[1]:
                outputFile.write(sSortedLine)
                temp = sSortedLine
                sSortedLine = sSorted.readline()
                sSplit = sSortedLine.split('\t')
            # If they have the same value it means the whole line is the same
            # so I just change line
            elif rSortedLine == sSortedLine:
                outputFile.write(sSortedLine)
                temp = sSortedLine
                sSortedLine = sSorted.readline()


    # If one file is finished, with this condition I continue the loop
    # until both files are over
    if rSortedLine == '' or sSortedLine =='':
        if rSortedLine == '':
            outputFile.write(sSortedLine)
            temp = sSortedLine
            sSortedLine = sSorted.readline()
            sSplit = sSortedLine.split()
        else:
            outputFile.write(rSortedLine)
            temp = rSortedLine
            rSortedLine = rSorted.readline()
            rSplit = rSortedLine.split()



rSorted.close()
sSorted.close()
outputFile.close()