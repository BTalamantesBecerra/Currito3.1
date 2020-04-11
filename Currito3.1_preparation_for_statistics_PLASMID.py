
import sys, getopt
import math

def main(argv):


    InputBLASTfiltered = ""
    Output_preparingBLAST_data_path = ""
    Candidate = ""
    TargetID = ""
    output_preCIRCOS_path = ""
    circos_program_path  = ""


    try:
      opts, args = getopt.getopt(argv,"i:o:c:t:w:y:",["InputBLASTfiltered=","Output_preparingBLAST_data_path=", "Candidate=", "TargetID=", "output_preCIRCOS_path=", "circos_program_path="])
    except getopt.GetoptError:
      print ('statistics.py -i <InputBLASTfiltered> -o <Output_preparingBLAST_data_path> -c <Candidate> -t <TargetID> -w <output_preCIRCOS_path> -y <circos_program_path>')
      sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
         print ('statistics.py -i <InputBLASTfiltered> -o <Output_preparingBLAST_data_path> -c <Candidate> -t <TargetID> -w <output_preCIRCOS_path>')
         sys.exit()
        elif opt in ("-i", "--InputBLASTfiltered"):
            InputBLASTfiltered = arg
        elif opt in ("-o", "--Output_preparingBLAST_data_path"):
            Output_preparingBLAST_data_path = arg
        elif opt in ("-c", "--Candidate"):
            Candidate = arg
        elif opt in ("-t", "--TargetID"):
            TargetID = arg
        elif opt in ("-w", "--output_preCIRCOS_path"):
            output_preCIRCOS_path = arg
        elif opt in ("-y", "--circos_program_path"):
            circos_program_path = arg
            
            
    print ('Input file is the InputBLASTfiltered : ', InputBLASTfiltered)
    print ('Output_preparingBLAST_data_path : ', Output_preparingBLAST_data_path)
    print ('Input for candidate : ', Candidate)
    print ('TargetID : ', TargetID)
    print ('output_preCIRCOS_path : ', output_preCIRCOS_path)



    inputFileToArrange = open(InputBLASTfiltered)
    OutputFile = open(Output_preparingBLAST_data_path, 'w')


    highlights_sequences = output_preCIRCOS_path + "highlights_sequences.txt"
    pident = output_preCIRCOS_path + "pident.txt"
    subjectAcc = ""

    outputHighLights = open(highlights_sequences, 'w')
    outputPident = open(pident, 'w')

    karyotype = output_preCIRCOS_path + "karyotype.txt"
    outputkaryotype = open(karyotype, 'w')
    sLength = ""
    ImageLabelNumber = ""
    if Candidate == "first_candidate":
        ImageLabelNumber = "a)"
    elif Candidate == "second_candidate":
        ImageLabelNumber = "b)"
    elif Candidate == "third_candidate":
        ImageLabelNumber = "c)"


    highlights = output_preCIRCOS_path + "highlights.txt"
    outputHighL = open(highlights,'w')


    ticks = output_preCIRCOS_path + "ticks.txt"
    outputTicks = open(ticks, 'w')



    conf = output_preCIRCOS_path + "conf.txt"
    outputConf = open(conf,'w')

    

    VariableForTargetID = ""
                
    NumberOfHeaders = 18
                
    blastIndexColumn = 0
    subjectAccColumn = 1
    subjectTitleColumn = 2
    QseqColumn = 3
    SseqColumn = 4
    nIdentColumn = 5
    nMismatchColumn = 6
    PidentColumn = 7
    lengthColumn = 8
    evalueColumn = 9
    bitscoreColumn = 10
    qStartColumn = 11
    qEndColumn = 12
    sStartColumn = 13
    sEndColumn = 14
    gapOpenColumn = 15
    gapsColumn = 16
    qLengthColumn = 17
    numHitsWithinRefColumn = 18
    sStartConverted = 19
    sEndConverted = 20
    

    headerTemp = inputFileToArrange.readline()
    headerLine = headerTemp.splitlines()
    y = headerLine[0]
    OutputFile.write(y + '\t' + "sStartConverted" + '\t' + "sEndConverted" + '\t' + "NucleotideSubstitution" + '\t' + "GlobalNucleotideSubstitution" +'\n') #HERE)
    
    OutputRowsList = list() #HERE
    SumOf_nIdent_I = 0.0 #HERE
    SumOf_nMismatch_fv = 0.0 #HERE
    SumOf_gapOpen_G = 0.0 #HERE
    


    tempstring = "temp"
    while tempstring:
        tempstring = inputFileToArrange.readline()
        if tempstring == "":
            break
        templine = tempstring.splitlines()
        x = templine[0]
        rowlist = x.split('\t')
        blastIndex = rowlist[0]
        subjectAcc = rowlist[1]
        subjectTitle = rowlist[2]
        Qseq = rowlist[3]
        Sseq = rowlist[4]
        nIdent = rowlist[5] #I HERE
        nMismatch = rowlist[6]  #fv HERE
        Pident = rowlist[7]
        length = rowlist[8]
        evalue = rowlist[9]
        bitscore = rowlist[10]
        qStart = rowlist[11]
        qEnd = rowlist[12]
        sStart = rowlist[13]
        sEnd = rowlist[14]
        gapOpen = rowlist[15]  #G HERE
        gaps = rowlist[16]
        qLength = rowlist[17]
        sLength = rowlist[18]
        numHitsWithinRef = rowlist[19]

        sStartConverted = ""
        sEndConverted = ""
        
        SstartNumber = int(sStart)
        SendNumber = int(sEnd)

        if SstartNumber > SendNumber:
            sStartConverted = sEnd
            sEndConverted = sStart
        else:
            sStartConverted = sStart
            sEndConverted = sEnd


        nIdentFLOAT = float(nIdent)
        nMismatchFLOAT = float(nMismatch)
        gapOpenFLOAT = float(gapOpen)

        SumOf_nIdent_I += nIdentFLOAT
        SumOf_nMismatch_fv += nMismatchFLOAT
        SumOf_gapOpen_G += gapOpenFLOAT
    

        NucleotideSubstitution = ""
        T = (nIdentFLOAT + nMismatchFLOAT + gapOpenFLOAT)

        dAB = (-0.75 * math.log(1-0.75 * (nMismatchFLOAT / (nIdentFLOAT+nMismatchFLOAT))) * (1 - (gapOpenFLOAT / T)) + (gapOpenFLOAT / T))
        NucleotideSubstitution = str(dAB)

        OutputRows = (blastIndex + '\t' + subjectAcc  + '\t' + subjectTitle + '\t' + Qseq + '\t' + Sseq + '\t' +
                      nIdent + '\t' + nMismatch + '\t' + Pident + '\t' + length + '\t' + evalue + '\t' + bitscore + '\t' +
                      qStart + '\t' + qEnd + '\t' + sStart + '\t' + sEnd + '\t' + gapOpen + '\t' + gaps + '\t' + qLength + '\t' +
                      sLength + '\t' + numHitsWithinRef + '\t' + sStartConverted  + '\t' +  sEndConverted  + '\t' + NucleotideSubstitution + '\t') #HERE

        OutputRowsList.append(OutputRows) #HERE


        OutputRowsHighlights = (TargetID + "_vs_" + Candidate + " " + sStartConverted + " " + sEndConverted  + '\n')
        outputHighLights.write(OutputRowsHighlights)

        IntPident = float(Pident)
        NewPident = (IntPident / 100 ) - 0.5
        NewPident = round(NewPident, 4)
        string = str(NewPident)

        OutputRowsPident = (TargetID + "_vs_" + Candidate + " " + sStartConverted + " " + sEndConverted  + " " + string + '\n')
        outputPident.write(OutputRowsPident)



    Global_T = (SumOf_nIdent_I + SumOf_nMismatch_fv + SumOf_gapOpen_G)
    Global_dAB = (-0.75 * math.log(1-0.75 * (SumOf_nMismatch_fv / (SumOf_nIdent_I+SumOf_nMismatch_fv))) * (1 - (SumOf_gapOpen_G / Global_T)) + (SumOf_gapOpen_G / Global_T))
    print("Global_dAB")
    print(Global_dAB)
        

    for OutputRow in OutputRowsList:
        OutputRow += (str(Global_dAB) + '\n')
        OutputFile.write(OutputRow)


    OutputRowsKaryotype = ("chr - " + TargetID + "_vs_" + Candidate + " " + ImageLabelNumber + "_" + TargetID + "_vs_" + Candidate + " 0 " + sLength + " " +
                           "black" + '\n' + "band " + TargetID + "_vs_" + Candidate + " band1 band1 0 " + sLength + " " + "black" + '\n')
    outputkaryotype.write(OutputRowsKaryotype)



    OutputRowsHighlightsNonSequences = ("<highlights>" + '\n' + "<highlight>" + '\n' + "init_counter = highlight:1" + '\n' +
                                        "file = " + highlights_sequences + '\n' + "fill_color = blue" + '\n' + "r1 = 0.97r" + '\n' +
                                        "r0 = 0.67r" + '\n' + "</highlight>" + '\n' + "</highlights>" + '\n')
    outputHighL.write(OutputRowsHighlightsNonSequences)


    OutputRowsTicks = ("show_ticks = yes" + '\n' +
                       "show_tick_labels = yes" + '\n' +
                       "<ticks>" + '\n' +
                       "radius = dims(ideogram,radius_outer)" + '\n' +
                       "label_offset = 5p" + '\n' +
                       "thickness = 3p" + '\n' +
                       "size = 20p" + '\n' +
                       "label_separation = 5p" + '\n' +
                       "<tick>" + '\n' +
                       "spacing = 0.05u" + '\n' +
                       "color = black" + '\n' +
                       "thickness = 2p" + '\n' +
                       "show_label = yes" + '\n' +
                       "label_size = 30p" + '\n' +
                       "label_font = bold" + '\n' +
                       "label_offset = 0p" + '\n' +
                       "format = %d" + '\n' +
                       "</tick>" + '\n' +
                       "<tick>" + '\n' +
                       "spacing = 0.01u" + '\n' +
                       "color = black" + '\n' +
                       "thickness = 2p" + '\n' +
                       "show_label = yes" + '\n' +
                       "label_size = 30p" + '\n' +
                       "label_font = bold" + '\n' +
                       "label_offset = 0p" + '\n' +
                       "format = %d" + '\n' +
                       "</tick>" + '\n' +
                       "<tick>" + '\n' +
                       "spacing = 0.001u" + '\n' +
                       "color = dgrey" + '\n' +
                       "thickness = 2p" + '\n' +
                       "show_label = yes" + '\n' +
                       "label_size = 20p" + '\n' +
                       "label_font = bold" + '\n' +
                       "label_offset = 0p" + '\n' +
                       "format = %.1f" + '\n' +
                       "</tick>" + '\n' +
                       "</ticks>" + '\n')
    outputTicks.write(OutputRowsTicks)
    


    OutputRowsConf = ("karyotype = " + karyotype + '\n' + "chromosomes_units = 1000000" + '\n' + "chromosomes_display_defaults = yes" + '\n' +
    "<<include " + highlights + ">>" + '\n' +
    "<ideogram>" + '\n' +
    "<spacing>" + '\n' + "default = 0u" + '\n' + "break = 0u" + '\n' +
    "</spacing>" + '\n' + "thickness = 20p" + '\n' +
    "radius = 0.65r" + '\n' + "show_label = yes" + '\n' + "label_font = bold" + '\n' + "label_with_tag = yes" + '\n' + "label_radius = dims(ideogram,radius) + 0.45r" + '\n' +
    "label_size = 30" + '\n' + "label_parallel   = yes" + '\n' + "stroke_thickness = 3" + '\n' + "stroke_color = gray" + '\n' + "fill = yes" + '\n' + "show_bands = yes" + '\n' +
    "fill_bands = yes" + '\n' +
    "</ideogram>" + '\n' +
    "<<include " + ticks + ">>" + '\n' +
    "<plots>" + '\n' +
    "<plot>" + '\n' + "type = histogram" + '\n' +
    "file = " + pident + '\n' +
    "r1 = 0.62r" + '\n' + "r0 = 0.27r" + '\n' + "thickness = 3" + '\n' + "max = 1.0" + '\n' + "min = 0" + '\n' + "extend_bin = no" + '\n' + "color = green" + '\n' + "orientation = in" + '\n' + 
    "<rules>" + '\n' + "<rule>" + '\n' + "condition = var(value) < 0.45" + '\n' + "color = red" + '\n' + "</rule>" + '\n' + "</rules>" + '\n' +
    "</plot>" + '\n' + "</plots>" + '\n' + 
    "<image>" + '\n' + "#TO DO - CHANGE THESE PATHS BECAUSE THEY ARE HARCODED" + '\n' +
    "<<include etc/image.conf>>"  + '\n' + "radius* = 750p" + '\n' + "</image>" + '\n' +
    "<<include etc/colors_fonts_patterns.conf>>" + '\n' +
    "<<include etc/housekeeping.conf>>" + '\n')
    outputConf.write(OutputRowsConf)


    
    inputFileToArrange.close()
    OutputFile.close()
    outputHighLights.close()
    outputPident.close()
    outputkaryotype.close()
    outputHighL.close()
    outputConf.close()
    outputTicks.close()
                



if __name__ == "__main__":
    main(sys.argv[1:])












        

