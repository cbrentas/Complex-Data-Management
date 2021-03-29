# Christos Brentas, A.M: 4442
rTsv = open('R.tsv')
outputFile = open('Rgroupby.tsv', 'w+')


# Function used to divide array and call the SortMerge() function
def mergeArray(pinakas):

    if len(pinakas) <= 1:
        return pinakas

    # Splitting array in two
    mesh = len(pinakas) // 2

    # Using recursion to get the best out of the split array(until it has 1 element)
    first = mergeArray(pinakas[:mesh])
    second = mergeArray(pinakas[mesh:])

    # Return the split arrays sorted and merged
    return SortMerge(first, second)


def SortMerge(prwtos, deuteros):
    buffer = []
    tempPrwtos = 0
    tempDeuteros = 0
    sortedArray = []

    # Run until arrays are empty
    while tempPrwtos < len(prwtos) and tempDeuteros < len(deuteros):

        # Split file lines in order to process the data
        prwtosStr = prwtos[tempPrwtos].split('\t')
        deuterosStr = deuteros[tempDeuteros].split('\t')

        # Add to the returning array the smallest element of the two given arrays

        if prwtosStr[0] < deuterosStr[0]:
            sortedArray.append(prwtos[tempPrwtos])
            tempPrwtos += 1

        elif prwtosStr[0] > deuterosStr[0]:
            sortedArray.append(deuteros[tempDeuteros])
            tempDeuteros += 1

        # If the keys of the given arrays are equal
        elif prwtosStr[0] == deuterosStr[0]:
            # Append the values in the buffer after convert them integers
            buffer.append(int(prwtosStr[1]))
            buffer.append(int(deuterosStr[1]))
            # Convert to string and adding it to the returning array
            sortedArray.append(prwtosStr[0] + '\t' + str(sum(buffer))+'\n')
            tempPrwtos += 1
            tempDeuteros += 1
            # Empty buffer after I calculated and added the summary
            buffer = []

    # If one array is finished it just adds the remaining elements of
    # the other array to the returning array. Since they are already sorted
    # we don't need more calculations.
    sortedArray.extend(prwtos[tempPrwtos:])
    sortedArray.extend(deuteros[tempDeuteros:])
    return sortedArray


rArray = rTsv.readlines()
rSorted = mergeArray(rArray)


# Iterating the returned sorted array writing the elements on the output file
while len(rSorted) != 0:
    outputFile.write(rSorted.pop(0))

rTsv.close()
outputFile.close()