
import sys, getopt

def main(argv):
    
    InputFile_TargetID_AccessionNumber = ""
    OutputFilePath = ""
    AccessionNumber = ""

    try:
        opts, args = getopt.getopt(argv,"i:o:",["InputFile_TargetID_AccessionNumber=", "OutputFilePath="])
    except getopt.GetoptError:
      print ('AccessionNumbers.py -i <InputFile_TargetID_AccessionNumber> -o <OutputFilePath>')
      sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
         print ('AccessionNumbers.py -i <InputFile_TargetID_AccessionNumber>  -o <OutputFilePath>')
         sys.exit()
        elif opt in ("-i", "--InputFile"):
            InputFile_TargetID_AccessionNumber = arg
        elif opt in ("-o", "--OutputFilePath"):
            OutputFilePath = arg


    inputFile = open(InputFile_TargetID_AccessionNumber)


    tempstring = "temp"
    while tempstring:
        tempstring = inputFile.readline()
        if tempstring == "":
            break
        templine = tempstring.splitlines()
        x = templine[0]
        rowlist = x.split('\n')
        AccessionNumber = rowlist[0]
        NameOfMyFile = OutputFilePath + AccessionNumber + ".txt"

    outputFile = open(NameOfMyFile, 'w')
    outputFile.write(AccessionNumber)
  
    
    
    outputFile.close()
    inputFile.close()
    

if __name__ == "__main__":
    main(sys.argv[1:])


   
