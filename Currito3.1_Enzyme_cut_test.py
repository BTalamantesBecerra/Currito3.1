
import sys,getopt

def main (argv):
    InputGenomeFile = ""
    OutputEnzymeCutTest = ""
    
    Output_PstI_HpaII_fragments = ""
    Output_PstI_MseI_fragments = ""
    Output_MseI_HpaII_fragments = ""

    try:
        opts, args = getopt.getopt(argv,"i:o:p:q:r:",["InputGenomeFile=","OutputEnzymeCutTest=","PstI_HpaII_fragments=","PstI_MseI_fragments=","MseI_HpaII_fragments="])
    except getopt.GetoptError:
      print ('Enzyme_cut_test.py -i <InputGenomeFile> -o <OutputEnzymeCutTest> -p <PstI_HpaII_fragments> -q <PstI_MseI_fragments> -r <MseI_HpaII_fragments>')
      sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
         print ('Enzyme_cut_test.py -i <InputGenomeFile> -o <OutputEnzymeCutTest> -p <PstI_HpaII_fragments> -q <PstI_MseI_fragments> -r <MseI_HpaII_fragments>')
         sys.exit()
        elif opt in ("-i", "--InputGenomeFile"):
            InputGenomeFile = arg
        elif opt in ("-o", "--OutputEnzymeCutTest"):
            OutputEnzymeCutTest = arg
        elif opt in ("-p", "--PstI_HpaII_fragments"):
            Output_PstI_HpaII_fragments = arg
        elif opt in ("-q", "--PstI_MseI_fragments"):
            Output_PstI_MseI_fragments = arg           
        elif opt in ("-r", "--MseI_HpaII_fragments"):
            Output_MseI_HpaII_fragments = arg

            
    print(InputGenomeFile)
    print(OutputEnzymeCutTest)


    inputFileGenome = open(InputGenomeFile)
    outputFile = open(OutputEnzymeCutTest, 'a')
    
    outputFile_PstI_HpaII_fragments = open(Output_PstI_HpaII_fragments, 'a')
 
    outputFile_PstI_MseI_fragments = open(Output_PstI_MseI_fragments, 'a')

    outputFile_MseI_HpaII_fragments = open(Output_MseI_HpaII_fragments, 'a')



    PstI_sequence = 'CTGCAG'
    HpaII_sequence = 'CCGG'
    MseI_sequence = 'TTAA'


    AllLines = inputFileGenome.readlines()

    NameOfGenome_Line0 = AllLines[0].splitlines()
    print(NameOfGenome_Line0)
    str0 = ''.join(NameOfGenome_Line0)
    outputFile.write(str0)
    outputFile.write('\n')



    genome_without_header = AllLines[1:]
    listLenght = len(genome_without_header)

 
    complete_genome_string = ""

    for x in range(0,listLenght):
        tempList = genome_without_header[x].splitlines()
        tempString = tempList[0]
        complete_genome_string += tempString
    outputFile.write(complete_genome_string)
    print("Genome size: " + str(len(complete_genome_string)) + " bp")


        
    search_fragments_PstI =  complete_genome_string.index(PstI_sequence)
    print(search_fragments_PstI)


    search_fragments_HpaII =  complete_genome_string.index(HpaII_sequence)
    print(search_fragments_HpaII)


    search_fragments_MseI =  complete_genome_string.index(MseI_sequence)
    print(search_fragments_MseI)


    list_for_PstI_start = []
    list_for_PstI_end = []


    Number_of_bases_to_add_to_get_final_position = len(PstI_sequence) - 1    
    starting_position_index = 0
    search_starting_position = 0
    lenght_of_genome_string = len(complete_genome_string)

    while True: 
        if search_starting_position > lenght_of_genome_string:
            break
        starting_position_index = complete_genome_string.find(PstI_sequence, search_starting_position)
        if starting_position_index == -1:
            break
        ending_position_index = starting_position_index + Number_of_bases_to_add_to_get_final_position
        search_starting_position = ending_position_index + 1
        print(starting_position_index)
        list_for_PstI_start.append(starting_position_index)
        print(ending_position_index)
        list_for_PstI_end.append(ending_position_index)

    print(list_for_PstI_start)
    print(list_for_PstI_end)


    list_for_HpaII_start = []
    list_for_HpaII_end = []


    Number_of_bases_to_add_to_get_final_position = len(HpaII_sequence) - 1 
    starting_position_index = 0
    search_starting_position = 0
    lenght_of_genome_string = len(complete_genome_string)

    while True: 
        if search_starting_position > lenght_of_genome_string:
            break
        starting_position_index = complete_genome_string.find(HpaII_sequence, search_starting_position)
        if starting_position_index == -1:
            break
        ending_position_index = starting_position_index + Number_of_bases_to_add_to_get_final_position
        search_starting_position = ending_position_index + 1
        print(starting_position_index)
        list_for_HpaII_start.append(starting_position_index)
        print(ending_position_index)
        list_for_HpaII_end.append(ending_position_index)


    print(list_for_HpaII_start)
    print(list_for_HpaII_end)


    list_for_MseI_start = []
    list_for_MseI_end = []

#Find fuction
    Number_of_bases_to_add_to_get_final_position = len(MseI_sequence) - 1    
    starting_position_index = 0
    search_starting_position = 0
    lenght_of_genome_string = len(complete_genome_string)

    while True: 
        if search_starting_position > lenght_of_genome_string:
            break
        starting_position_index = complete_genome_string.find(MseI_sequence, search_starting_position)
        if starting_position_index == -1:
            break
        ending_position_index = starting_position_index + Number_of_bases_to_add_to_get_final_position
        search_starting_position = ending_position_index + 1
        print(starting_position_index)
        list_for_MseI_start.append(starting_position_index)
        print(ending_position_index)
        list_for_MseI_end.append(ending_position_index)


    print(list_for_MseI_start)
    print(list_for_MseI_end)


    PstI_HpaII_sequence_list = []
    HpaII_PstI_sequence_list = []

    PstI_MseI_sequence_list = []
    MseI_Psti_sequence_list = []

    MseI_HpaII_sequence_list = []
    HpaII_MseI_sequence_list = []
    

    PstI_to_HpaII_start = []
    PstI_to_HpaII_end = []

    #lengh of list
    lenght_list_for_PstI_start = len(list_for_PstI_start)
    lenght_list_for_PstI_end = len(list_for_PstI_end)

    if lenght_list_for_PstI_start != lenght_list_for_PstI_end:
        print("the length of the list start and end for PstI is not the same. fix it!")
        exit()

    length_list_for_HpaII_start = len(list_for_HpaII_start)
    lenght_list_for_HpaII_end = len(list_for_HpaII_end)

    if length_list_for_HpaII_start != lenght_list_for_HpaII_end:
        print ("the length of the list start and end for HpaII is not the same")
        exit()
        
        
    for x in range (0, lenght_list_for_PstI_start):
        current_PstI_site_start = list_for_PstI_start[x]
        current_PstI_site_end = list_for_PstI_end[x]
        if x == (lenght_list_for_PstI_start -1):
            Next_PstI_site_start = len(complete_genome_string)
        else:
            Next_PstI_site_start = list_for_PstI_start[x+1]
            Next_PstI_site_end = list_for_PstI_end[x+1]

        for y in range (0, length_list_for_HpaII_start):
            start_position_of_HpaII = list_for_HpaII_start[y]
            if start_position_of_HpaII < current_PstI_site_end:
                continue
            if start_position_of_HpaII > Next_PstI_site_start:
                break
            end_position_of_HpaII = list_for_HpaII_end[y]

            PstI_to_HpaII_start.append(current_PstI_site_start)
            PstI_to_HpaII_end.append(end_position_of_HpaII)

            temp_string = complete_genome_string[current_PstI_site_start:end_position_of_HpaII + 1]
            PstI_HpaII_sequence_list.append(temp_string)
            break

    print('/n/')
    print("PstI to HpaII")
    print(PstI_to_HpaII_start)
    print(PstI_to_HpaII_end)
    print(PstI_HpaII_sequence_list)


      
    HpaII_to_PstI_start = []
    HpaII_to_PstI_end = []



    for x in range (0, length_list_for_HpaII_start):
        current_HpaII_site_start = list_for_HpaII_start[x]
        current_HpaII_site_end = list_for_HpaII_end[x]
        if x == (length_list_for_HpaII_start - 1):
            Next_HpaII_site_start = len(complete_genome_string)
        else:
            Next_HpaII_site_start = list_for_HpaII_start[x+1]

        for y in range(0, lenght_list_for_PstI_start):
            Start_position_of_PstI = list_for_PstI_start[y]
            if Start_position_of_PstI < current_HpaII_site_end:
                continue
            if Start_position_of_PstI > Next_HpaII_site_start:
                break
            end_position_of_PstI = list_for_PstI_end[y]

            HpaII_to_PstI_start.append(current_HpaII_site_start)
            HpaII_to_PstI_end.append(end_position_of_PstI)

            temp_string = complete_genome_string[current_HpaII_site_start:end_position_of_PstI + 1]
            HpaII_PstI_sequence_list.append(temp_string)
            break

    print('/n/')
    print("HpaII to PstI")
    print(HpaII_to_PstI_start)
    print(HpaII_to_PstI_end)
    print(HpaII_PstI_sequence_list)



    PstI_to_MseI_start = []
    PstI_to_MseI_end = []

    #lengh of list
    length_list_for_PstI_start = len(list_for_PstI_start)
    length_list_for_PstI_end = len(list_for_PstI_end)


    if lenght_list_for_PstI_start != lenght_list_for_PstI_end:
        print("the length of the list start and end for PstI is not the same. fix it!")
        exit()

    length_list_for_MseI_start = len(list_for_MseI_start)
    length_list_for_MseI_end = len(list_for_MseI_end)

    if length_list_for_MseI_start != length_list_for_MseI_end:
        print ("the length of the list start and end for MseI is not the same")
        exit()
        
        
    for x in range (0, length_list_for_PstI_start):
        current_PstI_site_start = list_for_PstI_start[x]
        current_PstI_site_end = list_for_PstI_end[x]
        if x == (length_list_for_PstI_start -1):
            Next_PstI_site_start = len(complete_genome_string)
        else:
            Next_PstI_site_start = list_for_PstI_start[x+1]
            Next_PstI_site_end = list_for_PstI_end[x+1]

        for y in range (0, length_list_for_MseI_start):
            start_position_of_MseI = list_for_MseI_start[y]
            
            if start_position_of_MseI < current_PstI_site_end:
                continue
            if start_position_of_MseI > Next_PstI_site_start:
                break
            end_position_of_MseI = list_for_MseI_end[y]

            PstI_to_MseI_start.append(current_PstI_site_start)
            PstI_to_MseI_end.append(end_position_of_MseI)

            temp_string = complete_genome_string[current_PstI_site_start:end_position_of_MseI + 1]
            PstI_MseI_sequence_list.append(temp_string)
            
            break

    print('/n/')
    print("PstI to MseI")
    print(PstI_to_MseI_start)
    print(PstI_to_MseI_end)
    print(PstI_MseI_sequence_list)


      
    MseI_to_PstI_start = []
    MseI_to_PstI_end = []

 

    for x in range (0, length_list_for_MseI_start):
        current_MseI_site_start = list_for_MseI_start[x]
        current_MseI_site_end = list_for_MseI_end[x]
        if x == (length_list_for_MseI_start - 1):
            Next_MseI_site_start = len(complete_genome_string)
        else:
            Next_MseI_site_start = list_for_MseI_start[x+1]

        for y in range(0, lenght_list_for_PstI_start):
            Start_position_of_PstI = list_for_PstI_start[y]
            if Start_position_of_PstI < current_MseI_site_end:
                continue
            if Start_position_of_PstI > Next_MseI_site_start:
                break
            end_position_of_PstI = list_for_PstI_end[y]

            MseI_to_PstI_start.append(current_MseI_site_start)
            MseI_to_PstI_end.append(end_position_of_PstI)

            temp_string = complete_genome_string[current_MseI_site_start:end_position_of_PstI + 1]
            MseI_Psti_sequence_list.append(temp_string)
            
            break

    print('/n/')
    print("MseI to PstI")
    print(MseI_to_PstI_start)
    print(MseI_to_PstI_end)
    print(MseI_Psti_sequence_list)



    MseI_to_HpaII_start = []
    MseI_to_HpaII_end = []



    length_list_for_MseI_start = len(list_for_MseI_start)
    length_list_for_MseI_end = len(list_for_MseI_end)

    if length_list_for_MseI_start != length_list_for_MseI_end:
        print("the length of the list start and end for MseI is not the same. fix it!")
        exit()

    length_list_for_HpaII_start = len(list_for_HpaII_start)
    length_list_for_HpaII_end = len(list_for_HpaII_end)

    if length_list_for_HpaII_start != length_list_for_HpaII_end:
        print ("the length of the list start and end for HpaII is not the same")
        exit()
        
        
    for x in range (0, length_list_for_MseI_start):
        current_MseI_site_start = list_for_MseI_start[x]
        current_MseI_site_end = list_for_MseI_end[x]

        
        if x == (length_list_for_MseI_start -1):
            Next_MseI_site_start = len(complete_genome_string)
        else:
            Next_MseI_site_start = list_for_MseI_start[x+1]
            Next_MseI_site_end = list_for_MseI_end[x+1]

        for y in range (0, length_list_for_HpaII_start):
            start_position_of_HpaII = list_for_HpaII_start[y]
            if start_position_of_HpaII < current_MseI_site_end:
                continue
            if start_position_of_HpaII > Next_MseI_site_start:
                break
            end_position_of_HpaII = list_for_HpaII_end[y]

            MseI_to_HpaII_start.append(current_MseI_site_start)
            MseI_to_HpaII_end.append(end_position_of_HpaII)

            temp_string = complete_genome_string[current_MseI_site_start:end_position_of_HpaII +1]
            MseI_HpaII_sequence_list.append(temp_string)
            
            break

    print('/n/')
    print("MseI to HpaII")
    print(MseI_to_HpaII_start)
    print(MseI_to_HpaII_end)
    print(MseI_HpaII_sequence_list)
    

      
    HpaII_to_MseI_start = []
    HpaII_to_MseI_end = []



    for x in range (0, length_list_for_HpaII_start):
        current_HpaII_site_start = list_for_HpaII_start[x]
        current_HpaII_site_end = list_for_HpaII_end[x]
        if x == (length_list_for_HpaII_start - 1):
            Next_HpaII_site_start = len(complete_genome_string)
        else:
            Next_HpaII_site_start = list_for_HpaII_start[x+1]

        for y in range(0, length_list_for_MseI_start):
            Start_position_of_MseI = list_for_MseI_start[y]
            if Start_position_of_MseI < current_HpaII_site_end:
                continue
        
            if Start_position_of_MseI > Next_HpaII_site_start:
                break
            end_position_of_MseI = list_for_MseI_end[y]

            HpaII_to_MseI_start.append(current_HpaII_site_start)
            HpaII_to_MseI_end.append(end_position_of_MseI)

            temp_string = complete_genome_string[current_HpaII_site_start:end_position_of_MseI + 1]
            HpaII_MseI_sequence_list.append(temp_string)
            
            
            break

    print('/n/')
    print("HpaII to MseI")
    print(HpaII_to_MseI_start)
    print(HpaII_to_MseI_end)
    print(HpaII_MseI_sequence_list)


    Complement_dict = { 'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N': 'N', 'a': 't', 'c': 'g', 'g': 'c', 't': 'a', 'n': 'n'}



    length_PstI_HpaII_sequence_list = len(PstI_HpaII_sequence_list)

    headers = ("SequenceStart\tSequenceEnd\tStrand\tSeqLength\tSeqForward\tSeqOrientedAlwaysForward\n")
    outputFile_PstI_HpaII_fragments.write(headers)
    
    for x in range(0,length_PstI_HpaII_sequence_list):
        RowString = ""
        SeqLength = (PstI_to_HpaII_end[x] - PstI_to_HpaII_start[x]) + 1
        temp_sequence = PstI_HpaII_sequence_list[x]
        RowString += str(PstI_to_HpaII_start[x]) + ('\t') + str(PstI_to_HpaII_end[x]) + ('\t') + ("+") + ('\t') + str(SeqLength) + ('\t') + temp_sequence + ('\t') + temp_sequence + ('\n')
        outputFile_PstI_HpaII_fragments.write(RowString)



        length_HpaII_PstI_sequence_list = len(HpaII_PstI_sequence_list)

    for x in range(0,length_HpaII_PstI_sequence_list):
        RowString = ""
        SeqLength = (HpaII_to_PstI_end[x] - HpaII_to_PstI_start[x]) + 1
        temp_sequence = HpaII_PstI_sequence_list[x]
        bases = list(temp_sequence)

        bases = reversed([Complement_dict.get(base,base) for base in bases])
        bases = ''.join(bases)
        print(bases)
    
        RowString +=str(HpaII_to_PstI_start[x]) + ('\t') + str(HpaII_to_PstI_end[x]) + ('\t') + ("-") + ('\t') + str(SeqLength) + ('\t') + temp_sequence + ('\t') + bases + ('\n')
        outputFile_PstI_HpaII_fragments.write(RowString)



        
    length_PstI_MseI_sequence_list = len(PstI_MseI_sequence_list)

    headers = ("SequenceStart\tSequenceEnd\tStrand\tSeqLength\tSeqForward\tSeqOrientedAlwaysForward\n")
    outputFile_PstI_MseI_fragments.write(headers)

    for x in range(0,length_PstI_MseI_sequence_list):
        RowString = ""
        SeqLength = (PstI_to_MseI_end[x] - PstI_to_MseI_start[x]) + 1
        temp_sequence = PstI_MseI_sequence_list[x]
        RowString += str(PstI_to_MseI_start[x]) + ('\t') + str(PstI_to_MseI_end[x]) + ('\t') + ("+") + ('\t') + str(SeqLength) + ('\t') + temp_sequence + ('\t') + temp_sequence + ('\n')
        outputFile_PstI_MseI_fragments.write(RowString)



        length_MseI_Psti_sequence_list = len(MseI_Psti_sequence_list)

    for x in range(0,length_MseI_Psti_sequence_list):
        RowString = ""
        SeqLength = (MseI_to_PstI_end[x] - MseI_to_PstI_start[x]) + 1
        temp_sequence = MseI_Psti_sequence_list[x]

        bases = list(temp_sequence)
        bases = reversed([Complement_dict.get(base,base) for base in bases])
        bases = ''.join(bases)
        print(bases)
        
        RowString +=str(MseI_to_PstI_start[x]) + ('\t') + str(MseI_to_PstI_end[x]) + ('\t') + ("-") + ('\t') + str(SeqLength) + ('\t') + temp_sequence + ('\t') +  bases  + ('\n')
        outputFile_PstI_MseI_fragments.write(RowString)



    length_MseI_HpaII_sequence_list = len(MseI_HpaII_sequence_list)

    headers = ("SequenceStart\tSequenceEnd\tStrand\tSeqLength\tSeqForward\tSeqOrientedAlwaysForward\n")
    outputFile_MseI_HpaII_fragments.write(headers)
    
    for x in range(0,length_MseI_HpaII_sequence_list):
        RowString = ""
        SeqLength = (MseI_to_HpaII_end[x] - MseI_to_HpaII_start[x]) + 1
        temp_sequence = MseI_HpaII_sequence_list[x]
        RowString += str(MseI_to_HpaII_start[x]) + ('\t') + str(MseI_to_HpaII_end[x]) + ('\t') + ("+") + ('\t') + str(SeqLength) + ('\t') + temp_sequence + ('\t') + temp_sequence + ('\n')
        outputFile_MseI_HpaII_fragments.write(RowString)



    length_HpaII_MseI_sequence_list = len(HpaII_MseI_sequence_list)


    for x in range(0,length_HpaII_MseI_sequence_list):
        RowString = ""
        SeqLength = (HpaII_to_MseI_end[x] - HpaII_to_MseI_start[x]) + 1
        temp_sequence = HpaII_MseI_sequence_list[x]

        bases = list(temp_sequence)
        bases = reversed([Complement_dict.get(base,base) for base in bases])
        bases = ''.join(bases)
        print(bases)
        
        RowString +=str(HpaII_to_MseI_start[x]) + ('\t') + str(HpaII_to_MseI_end[x]) + ('\t') + ("-") + ('\t') + str(SeqLength) + ('\t') + temp_sequence + ('\t') +  bases  + ('\n')
        outputFile_MseI_HpaII_fragments.write(RowString)



    inputFileGenome.close()
    outputFile.close()



if __name__ == "__main__":
    main(sys.argv[1:])

