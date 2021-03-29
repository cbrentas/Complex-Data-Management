# Christos Brentas, A.M: 4442

rSorted = open("R_sorted.tsv")
sSorted = open("S_sorted.tsv")
outputfile = open("RjoinS.tsv", 'w+')


buffer = []
# buffer itterator
bufferindicator = 0
bufferMaxSize = 0
# read next lines
rTemp = rSorted.readline()
sTemp = sSorted.readline()
# While until files are over
while rTemp != '' and sTemp != '':

    # buffer max size calculation
    bufferindicator = len(buffer)
    if bufferindicator > bufferMaxSize:
        bufferMaxSize = bufferindicator

    #S plit lines as key-value so I can use them
    rSplit = rTemp.split('\t')
    sSplit = sTemp.split('\t')


    # Read next S line
    if sSplit[0] < rSplit[0]:
        sTemp = sSorted.readline()
        sSplit = sTemp.split('\t')
    else:
        if rSplit[0] != sSplit[0]:
            # Iterate buffer to in case R has repeatable line keys
            if len(buffer) != 0:
                for i in range (len(buffer)):
                    if len(buffer) !=0:
                        # Popping element from buffer in order to process it
                        bString = buffer.pop(0)
                        bTemp = bString.split('\t')
                        if rSplit[0] == bTemp[0]:
                            outputfile.write(rSplit[0] + '\t' + rSplit[1].strip('\n') + '\t' + bTemp[1].strip('\n') + '\n')
                        # Adding the element back in, in case I need to use the buffer again
                        buffer.append(bString)
                        # Condition to empty buffer while it's no longer needed
                        if rSplit[0] != bTemp[0]:
                            buffer = []
                    else:
                        break
                if rSplit[0] < sSplit[0]:
                    rTemp = rSorted.readline()
                    rSplit = rTemp.split('\t')

            elif rSplit[0] != sSplit[0]:
                rTemp = rSorted.readline()
                rSplit = rTemp.split('\t')


        elif rSplit[0] == sSplit[0]:
            # Compare R key with buffer key so that I know if I have to empty the buffer
            if len(buffer) !=0:
                bString = buffer.pop(0)
                bTemp = bString.split('\t')
                if rSplit[0] != bTemp[0]:
                    buffer = []
                else:
                    buffer.insert(0, bString)

            if rSplit[0] == sSplit[0]:
                outputfile.write(rSplit[0]+ '\t' + rSplit[1].strip('\n') + '\t' + sSplit[1].strip('\n') + '\n')
                buffer.append(sTemp)
                sTemp = sSorted.readline()
                sSplit = sTemp.split('\t')

            if rSplit[0] != sSplit[0] and rSplit[0] != buffer[0].split('\t')[0]:
                buffer = []

            elif rSplit[0] != sSplit[0] and len(buffer) !=0:
                rTemp = rSorted.readline()
                rSplit = rTemp.split('\t')


print('Max buffer size: ' + str(bufferMaxSize))
rSorted.close()
sSorted.close()
outputfile.close()