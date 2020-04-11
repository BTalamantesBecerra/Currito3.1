import sys,getopt

def main (argv):
    InputCondensedFileName = ""
    OutputCondensedMergedResults = ""
    print("It works")

    try:
        opts, args = getopt.getopt(argv,"i:o:",["inCondensedfile=","outMergedresults="])
    except getopt.GetoptError:
      print ('cucu.py -i <CondensedFile> -o <OutputCondensedMergedResults>')
      sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
         print ('cucu.py -i <CondensedFile> -o <OutputCondensedMergedResults>')
         sys.exit()
        elif opt in ("-i", "--inCondensedfile"):
            InputCondensedFileName = arg
        elif opt in ("-o", "--outMergedresults"):
            OutputCondensedMergedResults = arg

    print(InputCondensedFileName)
    print(OutputCondensedMergedResults)

    inputFileSplit = open(InputCondensedFileName)
    outputFile = open(OutputCondensedMergedResults, 'a')

    FirstRow = ""
    SecondRow = ""
    ThirdRow = ""


    inputFileSplit.readline()

    FirstRow = inputFileSplit.readline()
    SecondRow = inputFileSplit.readline()
    ThirdRow = inputFileSplit.readline()

    FirstRowSubAcc = ""
    FirstRowSubTitle = ""
    FirstRowCountOfBestHits = ""
    FirstRowMeanBitScore = ""
    temporaryList = FirstRow.splitlines()
    singleString = temporaryList [0]
    splitingList = singleString.split('\t')

    FirstRowSubAcc = splitingList[0]
    FirstRowSubTitle = splitingList[1]
    FirstRowCountOfBestHits = splitingList[2]
    FirstRowMeanBitScore = splitingList[3]
    
    temporaryList = SecondRow.splitlines()
    singleString = temporaryList [0]
    splitingList = singleString.split("\t")

    SecondRowSubAcc = splitingList[0]
    SecondRowSubTitle = splitingList[1]
    SecondRowCountOfBestHits = splitingList[2]
    SecondRowMeanBitScore = splitingList[3]
    
    temporaryList = ThirdRow.splitlines()
    singleString = temporaryList [0]
    splitingList = singleString.split("\t")

    ThirdRowSubAcc = splitingList[0]
    ThirdRowSubTitle = splitingList[1]
    ThirdRowCountOfBestHits = splitingList[2]
    ThirdRowMeanBitScore = splitingList[3]
    
    variable_to_hold_spliting_by_backslash = InputCondensedFileName.split("\\")
    variable_to_hold_size_of_list = len(variable_to_hold_spliting_by_backslash)
    pulling_the_last_element = variable_to_hold_spliting_by_backslash [variable_to_hold_size_of_list - 1]
    variable_to_hold_Spliting_name_by_underscore = pulling_the_last_element.split("_")
    
    TargetID = variable_to_hold_Spliting_name_by_underscore[0]
    
    OutputLineFirstRow = FirstRowSubAcc + "\t" + FirstRowSubTitle + "\t" + FirstRowCountOfBestHits + "\t" + FirstRowMeanBitScore
    OutputLineSecondRow = SecondRowSubAcc + "\t" +   SecondRowSubTitle  + "\t" +  SecondRowCountOfBestHits  + "\t" + SecondRowMeanBitScore
    OutputLineThirdRow = ThirdRowSubAcc  + "\t" + ThirdRowSubTitle  + "\t" + ThirdRowCountOfBestHits  + "\t" + ThirdRowMeanBitScore

    OutputLineAll = TargetID + "\t" + OutputLineFirstRow + "\t" + OutputLineSecondRow + "\t" + OutputLineThirdRow + "\n"

    outputFile.write(OutputLineAll)
    
if __name__ == "__main__":
    main(sys.argv[1:])


