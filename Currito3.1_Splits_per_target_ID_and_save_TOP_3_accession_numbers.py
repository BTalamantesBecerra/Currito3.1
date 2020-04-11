

import sys, getopt

def main(argv):



    InputCondensedTOP3Candidates = ""
    OutputSplitAccessionNumbersFilePath = ""


    try:
      opts, args = getopt.getopt(argv,"i:o:",["InputCondensedTOP3Candidates=","OutputSplitAccessionNumbersFilePath="])
    except getopt.GetoptError:
      print ('Splits_per_target_ID_and_save_TOP_3_accession_numbers.py -i <InputCondensedTOP3Candidates> -o <OutputSplitAccessionNumbersFilePath>')
      sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
         print ('Splits_per_target_ID_and_save_TOP_3_accession_numbers.py -i <InputCondensedTOP3Candidates> -o <OutputSplitAccessionNumbersFilePath>')
         sys.exit()
        elif opt in ("-i", "--InputCondensedTOP3Candidates"):
            InputCondensedTOP3Candidates = arg
        elif opt in ("-o", "--OutputSplitAccessionNumbersFilePath"):
            OutputSplitAccessionNumbersFilePath = arg
    print ('Input file is the InputCondensedTOP3Candidates "', InputCondensedTOP3Candidates)
    print ('Output file is the OutputSplitAccessionNumbersFilePath"', OutputSplitAccessionNumbersFilePath)

    inputFileToSplit = open(InputCondensedTOP3Candidates)

    tempstring = "temp"
    while tempstring:
        tempstring = inputFileToSplit.readline()
        if tempstring == "":
            break
        templine = tempstring.splitlines()
        x = templine[0]
        rowlist = x.split('\t')
        targetID = rowlist[0]
        
        FirstAccessionNumber = rowlist[1]
        SecondAccessionNumber = rowlist[5]
        ThirdAccessionNumber = rowlist[9]
        
        OutputRows1 = FirstAccessionNumber + '\n'
        outputFileNameANDPath1 = OutputSplitAccessionNumbersFilePath + targetID + "_1.txt"
        outputFile1 = open(outputFileNameANDPath1, 'w')
        outputFile1.write(OutputRows1)
        outputFile1.close()

        OutputRows2 = SecondAccessionNumber + '\n'
        outputFileNameANDPath2 = OutputSplitAccessionNumbersFilePath + targetID + "_2.txt"
        outputFile2 = open(outputFileNameANDPath2, 'w')
        outputFile2.write(OutputRows2)
        outputFile2.close()

        OutputRows3 = ThirdAccessionNumber + '\n'
        outputFileNameANDPath3 = OutputSplitAccessionNumbersFilePath + targetID + "_3.txt"
        outputFile3 = open(outputFileNameANDPath3, 'w')
        outputFile3.write(OutputRows3)
        outputFile3.close()
 

    inputFileToSplit.close()


if __name__ == "__main__":
    main(sys.argv[1:])
            
