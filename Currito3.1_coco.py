


import sys, getopt

def main(argv):


    InputSplitFileName = ""
    InputFileFilteredName = ""
    OutputFilteredBlastResults = ""

    try:
      opts, args = getopt.getopt(argv,"i:j:o:",["insplitfile=","infilfile=","outfilresults="])
    except getopt.GetoptError:
      print ('coco.py -i <SplitFile> -j <FilteredFile> -o <OutputFilteredBLASTResults>')
      sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
         print ('test.py -i <SplitFile> -j <FilteredFile> -o <OutputFilteredBLASTResults>')
         sys.exit()
        elif opt in ("-i", "--insplitfile"):
            InputSplitFileName = arg
        elif opt in ("-j", "--infilfile"):
            InputFileFilteredName = arg
        elif opt in ("-o", "--outfilresults"):
            OutputFilteredBlastResults = arg
    print ('Input file is "', InputSplitFileName)
    print ('Input file is "', InputFileFilteredName)
    print ('Output file is "', OutputFilteredBlastResults)



    inputFileSplit = open(InputSplitFileName)
    inputFileFiltered = open(InputFileFilteredName)
    outputFile = open(OutputFilteredBlastResults, 'w')


    BlastIndexInSplitFile = 0
    BlastIndexInFilteredFile =  0
    NumberOfHeaderRowsInSplitFile = 1
    StringToHoldHeaderOfFilteredFile = ""
    NumberOfHeadersInFilteredFile = 1
    AllHeadersFromFilteredFile = ""

    BlastIndexSet = set()

    ReadingHeadersTemporarily = inputFileSplit.readline()

    temporaryString = "temp"
    while temporaryString:
        temporaryString = inputFileSplit.readline()
        if temporaryString == "":
            break
        templineList = temporaryString.splitlines()

        singleString = templineList[0]
        splitingList = singleString.split(",")
        
        BlastIndexSet.add(splitingList[BlastIndexInSplitFile])


    for HeaderCounter in range(0, NumberOfHeadersInFilteredFile):
        HeaderTemp = inputFileFiltered.readline()
        AllHeadersFromFilteredFile += HeaderTemp

    outputFile.write(AllHeadersFromFilteredFile)



    temporaryStringFilteredDoc = "temp"
    while temporaryStringFilteredDoc:
        temporaryStringFilteredDoc = inputFileFiltered.readline()
        if temporaryStringFilteredDoc =="":
            break
        templineList_filtered = temporaryStringFilteredDoc.splitlines()
        singleString_filtered = templineList_filtered[0]
        splitingList_filtered = singleString_filtered.split('\t')
        
        if splitingList_filtered[BlastIndexInFilteredFile] in BlastIndexSet:
            outputFile.write(temporaryStringFilteredDoc)


    inputFileSplit.close()
    inputFileFiltered.close()
    outputFile.close()

if __name__ == "__main__":
    main(sys.argv[1:])
