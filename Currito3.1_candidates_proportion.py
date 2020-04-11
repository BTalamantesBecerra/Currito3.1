

import sys, getopt
def main(argv):


    Input_File_1 = ""
    Input_File_2 = ""
    Input_File_3 = ""
    Output_File = ""
    SeqID_index_1 = 0
    SeqID_index_2 = 0
    SeqID_index_3 = 0
    TargetID = ""



    try:
      opts, args = getopt.getopt(argv,"i:j:k:o:t:",["Input_File_1=","Input_File_2=","Input_File_3=", "Output_File=", "TargetID="])
    except getopt.GetoptError:
      print ('candidates_proportion.py -i <Input_File_1> -j <Input_File_2> -k <Input_File_3> -o <Output_File> -t <TargetID>')
      sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
         print ('candidates_proportion.py -i <Input_File_1> -j <Input_File_2> -k <Input_File_3> -o <Output_File> -t <TargetID>')
         sys.exit()
        elif opt in ("-i", "--Input_File_1"):
            Input_File_1 = arg
        elif opt in ("-j", "--Input_File_2"):
            Input_File_2 = arg
        elif opt in ("-k", "--Input_File_3"):
            Input_File_3 = arg
        elif opt in ("-o", "--Output_File"):
            Output_File = arg
        elif opt in ("-t", "--TargetID"):
            TargetID = arg



    print ('Input file is :"', Input_File_1)
    print ('Input file is : "', Input_File_2)
    print ('Input file is : "', Input_File_3)
    print ('Output file is :"', Output_File)



    PreStatistics_1 = open(Input_File_1)
    PreStatistics_2 = open(Input_File_2)
    PreStatistics_3 = open(Input_File_3)
    OutputFile = open(Output_File, 'w')


    BLAST_INDEXES_FROM_Genome_8_Pre_statistics_output_1 = set()
    BLAST_INDEXES_FROM_Genome_8_Pre_statistics_output_2 = set()
    BLAST_INDEXES_FROM_Genome_8_Pre_statistics_output_3 = set()


    tempstring = PreStatistics_1.readline()


    tempstring = "temp"
    while tempstring:
        tempstring = PreStatistics_1.readline()
        if tempstring == "":
            break
        templine = tempstring.splitlines()
        x = templine[0]
        rowlist = x.split("\t")
        SeqID = rowlist[SeqID_index_1]
        BLAST_INDEXES_FROM_Genome_8_Pre_statistics_output_1.add(SeqID)

    Number_of_sequences_hiting_candidate_1 = len(BLAST_INDEXES_FROM_Genome_8_Pre_statistics_output_1)





    tempstring = PreStatistics_2.readline()



    tempstring = "temp"
    while tempstring:
        tempstring = PreStatistics_2.readline()
        if tempstring == "":
            break
        templine = tempstring.splitlines()
        x = templine[0]
        rowlist = x.split("\t")
        SeqID = rowlist[SeqID_index_2]
        BLAST_INDEXES_FROM_Genome_8_Pre_statistics_output_2.add(SeqID)

    Number_of_sequences_hiting_candidate_2 = len(BLAST_INDEXES_FROM_Genome_8_Pre_statistics_output_2)




    tempstring = PreStatistics_3.readline()


    tempstring = "temp"
    while tempstring:
        tempstring = PreStatistics_3.readline()
        if tempstring == "":
            break
        templine = tempstring.splitlines()
        x = templine[0]
        rowlist = x.split("\t")
        SeqID = rowlist[SeqID_index_3]
        BLAST_INDEXES_FROM_Genome_8_Pre_statistics_output_3.add(SeqID)

    Number_of_sequences_hiting_candidate_3 = len(BLAST_INDEXES_FROM_Genome_8_Pre_statistics_output_3)



    INTERSECTION_BETWEEN_1_and_2 = BLAST_INDEXES_FROM_Genome_8_Pre_statistics_output_1.intersection(BLAST_INDEXES_FROM_Genome_8_Pre_statistics_output_2)
    Size_of_Intersection_1_and_2 = len(INTERSECTION_BETWEEN_1_and_2)

    INTERSECTION_BETWEEN_2_and_3 = BLAST_INDEXES_FROM_Genome_8_Pre_statistics_output_2.intersection(BLAST_INDEXES_FROM_Genome_8_Pre_statistics_output_3)
    Size_of_Intersection_2_and_3 = len(INTERSECTION_BETWEEN_2_and_3)  

    INTERSECTION_BETWEEN_1_and_3 = BLAST_INDEXES_FROM_Genome_8_Pre_statistics_output_1.intersection(BLAST_INDEXES_FROM_Genome_8_Pre_statistics_output_3)
    Size_of_Intersection_1_and_3 = len(INTERSECTION_BETWEEN_1_and_3)



    UNION_BETWEEN_1_and_2 = BLAST_INDEXES_FROM_Genome_8_Pre_statistics_output_1.union(BLAST_INDEXES_FROM_Genome_8_Pre_statistics_output_2)
    Size_of_union_1_and_2 = len(UNION_BETWEEN_1_and_2)

    UNION_BETWEEN_2_and_3 = BLAST_INDEXES_FROM_Genome_8_Pre_statistics_output_2.union(BLAST_INDEXES_FROM_Genome_8_Pre_statistics_output_3)
    Size_of_union_2_and_3 = len(UNION_BETWEEN_2_and_3)
                
    UNION_BETWEEN_1_and_3 = BLAST_INDEXES_FROM_Genome_8_Pre_statistics_output_1.union(BLAST_INDEXES_FROM_Genome_8_Pre_statistics_output_3)
    Size_of_union_1_and_3 = len(UNION_BETWEEN_1_and_3)




    Proportion_in_common_1_and_2 = (Size_of_Intersection_1_and_2/Size_of_union_1_and_2)

    Proportion_in_common_2_and_3 = (Size_of_Intersection_2_and_3/Size_of_union_2_and_3)

    Proportion_in_common_1_and_3 = (Size_of_Intersection_1_and_3/Size_of_union_1_and_3)

            


    AllHeaders = ("TargetID" + "\t" +
                "Size_of_Intersection_1_and_2"  + "\t" + "Size_of_Intersection_2_and_3"  + "\t" + "Size_of_Intersection_1_and_3"  + "\t" +
                "Size_of_union_1_and_2"  + "\t" + "Size_of_union_2_and_3"  + "\t" + "Size_of_union_1_and_3"  + "\t" +
                "Proportion_in_common_1_and_2"  + "\t" + "Proportion_in_common_2_and_3" + "\t" + "Proportion_in_common_1_and_3" + "\n")
                  
    OutputFile.write(AllHeaders)


    Data = (TargetID + "\t" +
        str(Size_of_Intersection_1_and_2) + "\t" + str(Size_of_Intersection_2_and_3) + "\t" + str(Size_of_Intersection_1_and_3) + "\t" +
        str(Size_of_union_1_and_2) + "\t" + str(Size_of_union_2_and_3) + "\t" + str(Size_of_union_1_and_3)+ "\t" +
        str(Proportion_in_common_1_and_2) + "\t" + str(Proportion_in_common_2_and_3) + "\t" + str(Proportion_in_common_1_and_3) + "\n")

    OutputFile.write(Data)



    
    PreStatistics_1.close()
    PreStatistics_2.close()
    PreStatistics_3.close()
    OutputFile.close()

        
    
if __name__ == "__main__":
    main(sys.argv[1:])
