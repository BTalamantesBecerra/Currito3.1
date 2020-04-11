

import sys, getopt
def main(argv):



    Input_Split_cluster_unclustered = ""
    Input_Genome_8_Pre_statistics_output = ""
    Input_Plasmid_2_First_filt_per_target = ""
    Output_statistics_for_bars = ""
    SeqID_index = 0

    RowNumberWhereDataStarts = ""
    TargetID_candidate = ""



    try:
      opts, args = getopt.getopt(argv,"i:j:k:l:m:o:",["Input_Split_cluster_unclustered=","Input_Genome_8_Pre_statistics_output=","Input_Plasmid_2_First_filt_per_target=", "RowNumberWhereDataStarts=", "TargetID_candidate=","Output_statistics_for_bars="])
    except getopt.GetoptError:
      print ('bars_statistics.py -i <Input_Split_cluster_unclustered> -j <Input_Genome_8_Pre_statistics_output> -k <Input_Plasmid_2_First_filt_per_target> -l <RowNumberWhereDataStarts> -m <TargetID_candidate> -o <Output_statistics_for_bars>')
      sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
         print ('bars_statistics.py -i <Input_Split_cluster_unclustered> -j <Input_Genome_8_Pre_statistics_output> -k <Input_Plasmid_2_First_filt_per_target> -l<RowNumberWhereDataStarts> -m <TargetID_candidate> -o <Output_statistics_for_bars>')
         sys.exit()
        elif opt in ("-i", "--Input_Split_cluster_unclustered"):
            Input_Split_cluster_unclustered = arg
        elif opt in ("-j", "--Input_Genome_8_Pre_statistics_output"):
            Input_Genome_8_Pre_statistics_output = arg
        elif opt in ("-k", "--Input_Plasmid_2_First_filt_per_target"):
            Input_Plasmid_2_First_filt_per_target = arg
        elif opt in ("-l", "--RowNumberWhereDataStarts"):
            RowNumberWhereDataStarts = arg
        elif opt in ("-m", "--TargetID_candidate"):
            TargetID_candidate = arg
        elif opt in ("-o", "--Output_statistics_for_bars"):
            Output_statistics_for_bars = arg

  
    print ('Input file is :"', Input_Split_cluster_unclustered)
    print ('Input file is : "', Input_Genome_8_Pre_statistics_output)
    print ('Input file is : "', Input_Plasmid_2_First_filt_per_target)
    print ('Output file is :"', Output_statistics_for_bars)
    


    InputTotalSequences = open(Input_Split_cluster_unclustered)
    InputSeqsWITH_hits = open(Input_Genome_8_Pre_statistics_output)
    InputPLASMID_hits = open(Input_Plasmid_2_First_filt_per_target)
    OutputFile = open(Output_statistics_for_bars, 'w')


    BLAST_INDEXES_FROM_Split_cluster_unclustered = set()
    BLAST_INDEXES_FROM_Genome_8_Pre_statistics_output = set()
    BLAST_INDEXES_FROM_Plasmid_2_First_filt_per_target = set()

    Total_number_of_sequences = 0
    Number_of_sequences_hiting_Genome = 0
    Number_of_sequences_hiting_PLASMID_not_GENOME = 0
    Number_of_sequencesWithoutHits = 0



    for i in range(0, int(RowNumberWhereDataStarts)):
        HeaderTemp = InputTotalSequences.readline()


    tempstring = "temp"
    while tempstring:
        tempstring = InputTotalSequences.readline()
        if tempstring == "":
            break
        templine = tempstring.splitlines()
        x = templine[0]
        rowlist = x.split(",")
        SeqID = rowlist[SeqID_index]
        BLAST_INDEXES_FROM_Split_cluster_unclustered.add(SeqID)

    Total_number_of_sequences = len(BLAST_INDEXES_FROM_Split_cluster_unclustered)
        


    tempstring = InputSeqsWITH_hits.readline()



    tempstring = "temp"
    while tempstring:
        tempstring = InputSeqsWITH_hits.readline()
        if tempstring == "":
            break
        templine = tempstring.splitlines()
        x = templine[0]
        rowlist = x.split("\t")
        SeqID = rowlist[SeqID_index]
        BLAST_INDEXES_FROM_Genome_8_Pre_statistics_output.add(SeqID)

    Number_of_sequences_hiting_Genome = len(BLAST_INDEXES_FROM_Genome_8_Pre_statistics_output)


    tempstring = InputPLASMID_hits.readline()
    
    tempstring = "temp"
    while tempstring:
        tempstring = InputPLASMID_hits.readline()
        if tempstring == "":
            break
        templine = tempstring.splitlines()
        x = templine[0]
        rowlist = x.split("\t")
        SeqID = rowlist[SeqID_index]
        BLAST_INDEXES_FROM_Plasmid_2_First_filt_per_target.add(SeqID)


    BLAST_INDEXES_Plasmid_WITHOUT_BLAST_INDEXES_Genome = BLAST_INDEXES_FROM_Plasmid_2_First_filt_per_target.difference(BLAST_INDEXES_FROM_Genome_8_Pre_statistics_output)

    Number_of_sequences_hiting_PLASMID_not_GENOME = len(BLAST_INDEXES_Plasmid_WITHOUT_BLAST_INDEXES_Genome)
    
    Number_of_sequencesWithoutHits = Total_number_of_sequences - (Number_of_sequences_hiting_Genome + Number_of_sequences_hiting_PLASMID_not_GENOME)

    AllHeaders = "TargetID" + "\t" + "TotalSequences" + "\t" + "SequencesWithHitsToAReference" + "\t" + "SequencesWithHitsToAPlasmid" + "\t" + "SequencesWithoutHitsToAReference" + "\n"
    OutputFile.write(AllHeaders)
    
    Data = (TargetID_candidate + "\t" + str(Total_number_of_sequences) + "\t" + str(Number_of_sequences_hiting_Genome)  + "\t" +
            str(Number_of_sequences_hiting_PLASMID_not_GENOME) + "\t" + str(Number_of_sequencesWithoutHits) + "\n")
    OutputFile.write(Data)
    
    InputTotalSequences.close()
    InputSeqsWITH_hits.close()
    InputPLASMID_hits.close()
    OutputFile.close()
    
    
    
if __name__ == "__main__":
    main(sys.argv[1:])
