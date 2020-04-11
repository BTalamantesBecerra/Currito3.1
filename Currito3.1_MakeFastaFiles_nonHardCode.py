

import sys, getopt

def main(argv):
    
    InputCSVFileName = ""
    OutputFASTAFile = ""
    SeqID_index = 0
    TrimmedSequence_index = 0
    rowWhereDataStarts = ""
    OutputRows = ""
    

    try:
        opts, args = getopt.getopt(argv,"i:o:u:s:t:",["inCSVfile=","outFASTAFile=","rowWhereDataStarts=","SeqID_index=","TrimmedSequence_index="])
    except getopt.GetoptError:
      print ('MakeFastaFiles.py -i <CSVFile> -o <OutputFastaFile> -u <rowWhereDataStarts> -s <SeqID_index> -t <TrimmedSequence_index>')
      sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
         print ('MakeFastaFiles.py -i <CSVFile> -o <OutputFastaFile> -u <rowWhereDataStarts> -s <SeqID_index> -t <TrimmedSequence_index>')
         sys.exit()
        elif opt in ("-i", "--inCSVfile"):
            InputCSVFileName = arg
        elif opt in ("-o", "--outFASTAFile"):
            OutputFASTAFile = arg
        elif opt in ("-u", "--rowWhereDataStarts"):
            rowWhereDataStarts = arg
            
        elif opt in ("-s", "--SeqID_index"):
            SeqID_index = int(arg)
        elif opt in ("-t", "--TrimmedSequence_index"):
            TrimmedSequence_index = int(arg)


    inputFile = open(InputCSVFileName)
    OutputFile = open(OutputFASTAFile,'a')
        
    for c in range(0, int(rowWhereDataStarts)):
        HeaderTemp = inputFile.readline()


    tempstring = "temp"
    while tempstring:
        tempstring = inputFile.readline()
        if tempstring == "":
            break
        templine = tempstring.splitlines()
        x = templine[0]
        rowlist = x.split(",")
        SeqID = rowlist[SeqID_index]
        TrimmedSequence = rowlist[TrimmedSequence_index]
        OutputRows = ">" + SeqID + '\n' + TrimmedSequence + '\n'
        OutputFile.write(OutputRows)

    inputFile.close()
    OutputFile.close()


 
if __name__ == "__main__":
    main(sys.argv[1:])
