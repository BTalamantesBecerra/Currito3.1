

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import matplotlib.pyplot as plt
import sys, getopt
def main(argv):


    InputImage1 = ""
    InputImage2 = ""
    InputImage3 = ""
    OutputPathName = ""

    PreStatisticsFile_1 = ""
    PreStatisticsFile_2 = ""
    PreStatisticsFile_3 = ""
    OutputPathName = ""
    OutputPathNameMergedPlots = ""
    TargetID = ""
    SampleName = ""

    try:
      opts, args = getopt.getopt(argv,"i:j:k:a:b:c:o:p:s:w:",["InputImage1=","InputImage2=","InputImage3=","PreStatisticsFile_1=","PreStatisticsFile_2=","PreStatisticsFile_3=","OutputPathName=", "OutputPathNameMergedPlots=", "TargetID=", "SampleName="])
    except getopt.GetoptError:
      print ('graphs.py -i <InputImage1> -j <nputImage2> -k <InputImage3> -a <PreStatisticsFile_1> -b <PreStatisticsFile_2> -c <PreStatisticsFile_3> -o <OutputPathName> -p <OutputPathNameMergedPlots> -s <TargetID> -w <SampleName>')
      sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
         print ('graphs.py -i <InputImage1> -j <InputImage2> -k <InputImage3> -a <PreStatisticsFile_1> -b <PreStatisticsFile_2> -c <PreStatisticsFile_3> -o <OutputPathName> -p<OutputPathNameMergedPlots> -s <TargetID> -w <SampleName>' )
         sys.exit()
        elif opt in ("-i", "-InputImage1"):
            InputImage1 = arg
        elif opt in ("-j", "-InputImage2"):
            InputImage2 = arg
        elif opt in ("-k", "-InputImage3"):
            InputImage3 = arg
        elif opt in ("-a", "-PreStatisticsFile_1"):
            PreStatisticsFile_1 = arg
        elif opt in ("-b", "-PreStatisticsFile_2"):
            PreStatisticsFile_2 = arg
        elif opt in ("-c", "-PreStatisticsFile_3"):
            PreStatisticsFile_3 = arg
            
        elif opt in ("-o", "-OutputPathName"):
            OutputPathName = arg
        elif opt in ("-p", "-OutputPathNameMergedPlots"):
            OutputPathNameMergedPlots = arg
        elif opt in ("-s", "-TargetID"):
            TargetID = arg
        elif opt in ("-w", "-SampleName"):
            SampleName = arg


    InputPrestatistics_1 = open(PreStatisticsFile_1)
    InputPrestatistics_2 = open(PreStatisticsFile_2)
    InputPrestatistics_3 = open(PreStatisticsFile_3)
    Pident_1 = []
    Pident_2 = []
    Pident_3 = []
    subjectAcc_1 = ""
    subjectAcc_2 = ""
    subjectAcc_3 = ""
    subjectTitle_1 = ""
    subjectTitle_2 = ""
    subjectTitle_3 = ""
    
    InputPrestatistics_1.readline()



    tempstring = "temp"
    while tempstring:
        tempstring = InputPrestatistics_1.readline()
        if tempstring == "":
            break
        templine = tempstring.splitlines()
        x = templine[0]
        rowlist = x.split('\t')
        subjectAcc_1 = rowlist[1]
        subjectTitle_1 = rowlist[2]
        Pident_1.append(float(rowlist[7]))
    Pident_1 = sorted(Pident_1, reverse=True)
    fig1 = plt.plot(Pident_1)
    average_1 = sum(Pident_1)/float(len(Pident_1))
    textPositionX = round((len(Pident_1)/4),0)
    TwoDecimals_1 = round(average_1, 2)
    plt.ylim(60,105)
    plt.text(textPositionX, 75, 'Mean of % ID:' )
    plt.text(textPositionX, 73, TwoDecimals_1)
    plt.xlabel('Aligned sequences ordered by percentage identity (%ID)')
    plt.ylabel('BLAST alignment percentage identity (%ID)')
    plt.title("a) " + TargetID + " vs first candidate")
    plt.savefig(InputImage1)
    plt.ioff()

    plt.close()
        

    InputPrestatistics_2.readline()




    tempstring = "temp"
    while tempstring:
        tempstring = InputPrestatistics_2.readline()
        if tempstring == "":
            break
        templine = tempstring.splitlines()
        x = templine[0]
        rowlist = x.split('\t')
        subjectAcc_2 = rowlist[1]
        subjectTitle_2 = rowlist[2]
        Pident_2.append(float(rowlist[7]))
    Pident_2 = sorted(Pident_2, reverse=True)
    fig2 = plt.plot(Pident_2)
    average_2 = sum(Pident_2)/float(len(Pident_2))
    textPositionX_2 = round((len(Pident_2)/4),0)
    TwoDecimals_2 = round(average_2, 2)
    plt.ylim(60,105)
    plt.text(textPositionX_2, 75, 'Mean of % ID:' )
    plt.text(textPositionX_2, 73, TwoDecimals_2)
    plt.xlabel('Aligned sequences ordered by percentage identity (%ID)')
    plt.ylabel('BLAST alignment percentage identity (%ID)')
    plt.title("b) " +TargetID + " vs second candidate")
    plt.savefig(InputImage2)
    plt.ioff()

    plt.close()

    InputPrestatistics_3.readline()



    tempstring = "temp"
    while tempstring:
        tempstring = InputPrestatistics_3.readline()
        if tempstring == "":
            break
        templine = tempstring.splitlines()
        x = templine[0]
        rowlist = x.split('\t')
        subjectAcc_3 = rowlist[1]
        subjectTitle_3 = rowlist[2]
        Pident_3.append(float(rowlist[7]))
    Pident_3 = sorted(Pident_3, reverse=True)
    fig3 = plt.plot(Pident_3)
    average_3 = sum(Pident_3)/float(len(Pident_3))

    textPositionX_3 = round((len(Pident_3)/4),0)
    TwoDecimals_3 = round(average_3, 2)
    plt.ylim(60,105)
    plt.text(textPositionX_3, 75, 'Mean of % ID:' )
    plt.text(textPositionX_3, 73, TwoDecimals_3)
    plt.xlabel('Aligned sequences ordered by percentage identity (%ID)')
    plt.ylabel('BLAST alignment percentage identity (%ID)')
    plt.title("c) " +TargetID + " vs third candidate")
    plt.savefig(InputImage3)
    plt.ioff()

    plt.close()



    try:
        Image1 = Image.open(InputImage1)
        Image2 = Image.open(InputImage2)
        Image3 = Image.open(InputImage3)


    except:
        print("Unable to load plots")

    print ("The original format, the size  and the original mode of Image 1 are: ")
    print(Image1.format, Image1.size, Image1.mode)
    print ("The original format, the size  and the original mode of Image 2 are: ")
    print(Image2.format, Image2.size, Image2.mode)
    print ("The original format, the size  and the original mode of Image 3 are: ")
    print(Image3.format, Image3.size, Image3.mode)


    (width1, height1) = Image1.size
    (width2, height2) = Image2.size
    (width3, height3) = Image3.size

    result_width = width1 + width2
    result_height = max(height1, height2)
    print(result_width)
    print(result_height)

    result = Image.new('RGB', (result_width, result_height))
    result.paste(im=Image1, box=(0, 0))
    result.paste(im=Image2, box=(width1, 0))

    

    result2_height = result_height + height3
    result2 = Image.new('RGB', (result_width, result2_height), color=(255,255,255,0))
    result2.paste(im=result, box=(0,0))
    result2.paste(im=Image3, box=(0, result_height))

    draw =  ImageDraw.Draw(result2)
    font = ImageFont.truetype("arial.ttf", 13)

    draw.text((640, 490),"SAMPLE ID: " + TargetID + " \n" + "SAMPLE NAME: " + SampleName,(0, 0, 0),font=font)
    
    draw.text((640, 540),"a) Plot showing percentage identity of all BLAST alignments against the first  ",(0, 0, 0),font=font)
    draw.text((640, 560),"    candidate reference, sorted from highest to lowest:",(0, 0, 0),font=font)
    draw.text((640, 580),"    " + subjectAcc_1 + "-" + subjectTitle_1 + ".",(0, 0, 0),font=font)
    
    draw.text((640, 610),"b) Plot showing percentage identity of all BLAST alignments, against the second  ",(0, 0, 0),font=font)
    draw.text((640, 630),"    candidate reference, sorted from highest to lowest:",(0, 0, 0),font=font)
    draw.text((640, 650),"    " + subjectAcc_2 + "-" + subjectTitle_2 + ".",(0, 0, 0),font=font)
    
    draw.text((640, 680),"c) Plot showing percentage identity of all BLAST alignments, against the third  ",(0, 0, 0),font=font)
    draw.text((640, 700),"    candidate reference, sorted from highest to lowest:",(0, 0, 0),font=font)
    draw.text((640, 720),"    " + subjectAcc_3 + "-" + subjectTitle_3 + ".",(0, 0, 0),font=font)
    
    draw.text((640, 750),"Explanation of plots :",(0, 0, 0),font=font)
    draw.text((640, 770),"- The X axis shows the total number of sequences with BLAST hits ordered from ",(0, 0, 0),font=font)
    draw.text((640, 790),"    highest to lowest.",(0, 0, 0),font=font)
    draw.text((640, 810),"- The Y axis shows the BLAST alignment percentage identity. ",(0, 0, 0),font=font)
    draw.text((640, 830),"- The mean of percentage identity of all alignments is shown in the graph area.",(0, 0, 0),font=font)
    result2.save(OutputPathNameMergedPlots)
    result2.close()
    result.close()
    

    Image1.close()
    Image2.close()
    Image3.close()
              

    InputPrestatistics_1.close()
    InputPrestatistics_2.close()
    InputPrestatistics_3.close()

    
if __name__ == "__main__":
    main(sys.argv[1:])


