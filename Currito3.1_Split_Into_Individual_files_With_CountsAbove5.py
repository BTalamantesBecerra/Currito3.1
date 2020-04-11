
import sys, getopt

def main(argv):
    
    InputFileToSplitWithCountsAbove5 = ""
    NumberOfTargetColumns = ""
    OutputFilePath = ""

    try:
        opts, args = getopt.getopt(argv,"i:n:o:",["InputFileToSplitWithCountsAbove5=", "NumberOfTargetColumns=", "OutputFilePath="])
    except getopt.GetoptError:
      print ('Split_Into_Individual_files_With_CountsAbove5.py -i <InputFileToSplitWithCountsAbove5> -n <NumberOfTargetColumns> -o <OutputFilePath>')
      sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
         print ('Split_Into_Individual_files_With_CountsAbove5.py -i <InputFileToSplitWithCountsAbove5> -n <NumberOfTargetColumns> -o <OutputFilePath>')
         sys.exit()
        elif opt in ("-i", "--InputFileToSplitWithCountsAbove5"):
            InputFileToSplitWithCountsAbove5 = arg
        elif opt in ("-n", "--NumberOfTargetColumns"):
            NumberOfTargetColumns = int(arg)
        elif opt in ("-o", "--OutputFilePath"):
            OutputFilePath = arg


    inputFile = open(InputFileToSplitWithCountsAbove5)

    
    NumMetadataCol = 13
    VariableForTargetID = ""
    NumberOfHeaders = 6
    IndexBLAST = 0
    IndexTag = 3
    IndextTrimSeq = 4


    while NumberOfTargetColumns > 0:
        absoluteNumberOfTargetColumn = NumberOfTargetColumns + NumMetadataCol
        NumberOfTargetColumns = NumberOfTargetColumns -1
        indexNumberOfTargetCol = absoluteNumberOfTargetColumn - 1
        AllHeadersJoined = ""
        inputFile.seek(0)
        

        for c in range(0,NumberOfHeaders):
            headerTemp = inputFile.readline()
            headerLine = headerTemp.splitlines()
            y = headerLine[0]
            headerList=y.split(",")
  
            AllHeadersJoined += headerList[IndexBLAST] + ',' + headerList[IndexTag] + ',' +  headerList[IndextTrimSeq] + ',' + headerList[indexNumberOfTargetCol] + '\n'
            if c == NumberOfHeaders -1:
                VariableForTargetID = headerList[indexNumberOfTargetCol]
                
        NameOfMyFile = OutputFilePath + VariableForTargetID + ".csv"
        outputFile = open(NameOfMyFile, 'w')
        outputFile.write(AllHeadersJoined)

        tempstring = "temp"
        while tempstring:
            tempstring = inputFile.readline()
            if tempstring == "":
                break
            templine = tempstring.splitlines()

            x = templine[0]
            rowlist= x.split(",")
            b = len(rowlist)
            targetcount = rowlist[indexNumberOfTargetCol]
            if int(rowlist[indexNumberOfTargetCol],10) >= 5:
                outputFile.write(rowlist[IndexBLAST] + ',' + rowlist[IndexTag] + ',' + rowlist[IndextTrimSeq] + ',' + rowlist[indexNumberOfTargetCol] + '\n')
        outputFile.close()

    inputFile.close()
    

if __name__ == "__main__":
    main(sys.argv[1:])
