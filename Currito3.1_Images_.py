
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import sys, getopt
def main(argv):

    InputImage1 = ""
    InputImage2 = ""
    InputImage3 = ""
    PreStatisticsFile_1 = ""
    PreStatisticsFile_2 = ""
    PreStatisticsFile_3 = ""
    OutputPathName = ""
    TargetID = ""
    SampleName = ""

    

    try:
      opts, args = getopt.getopt(argv,"i:j:k:a:b:c:o:s:w:",["InputImage1=","InputImage2=","InputImage3=","PreStatisticsFile_1=","PreStatisticsFile_2=","PreStatisticsFile_3=","OutputPathName=","TargetID=", "SampleName="])
    except getopt.GetoptError:
      print ('Images_.py -i <InputImage1> -j <nputImage2> -k <InputImage3> -a <PreStatisticsFile_1> -b <PreStatisticsFile_2> -c <PreStatisticsFile_3> -o <OutputPathName> -s <TargetID> -w <SampleName>')
      sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
         print ('Images_.py -i <InputImage1> -j <InputImage2> -k <InputImage3> -a <PreStatisticsFile_1> -b <PreStatisticsFile_2> -c <PreStatisticsFile_3> -o <OutputPathName> -s <TargetID> -w <SampleName>' )
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
        elif opt in ("-s", "-TargetID"):
            TargetID = arg
        elif opt in ("-w", "-SampleName"):
            SampleName = arg

            
    """   
        elif opt in ("-p", "-FirstSubjectTitle"):
            FirstSubjectTitle = arg
        elif opt in ("-q", "-SecondSubjectTitle"):
            SecondSubjectTitle = arg
        elif opt in ("-r", "-ThirdSubjectTitle"):
            ThirdSubjectTitle = arg
    """


            
    print ('Input image 1 is : ', InputImage1)
    print ('Input image 2 is : ', InputImage2)
    print ('Input image 3 is : ', InputImage3)
    print ('Input PreStatisticsFile_1 is : ',PreStatisticsFile_1)
    print ('Input PreStatisticsFile_2 is : ',PreStatisticsFile_2)
    print ('Input PreStatisticsFile_3 is : ',PreStatisticsFile_3)
    print ('Output path is : ', OutputPathName)
    print ('TargetID is : ', TargetID)


    InputPrestatistics_1 = open(PreStatisticsFile_1)
    InputPrestatistics_2 = open(PreStatisticsFile_2)
    InputPrestatistics_3 = open(PreStatisticsFile_3)
    subjectTitle_1 = ""
    subjectTitle_2 = ""
    subjectTitle_3 = ""



    tempstring = "temp"
    tempstring = InputPrestatistics_1.readline()
    tempstring = InputPrestatistics_1.readline()
    templine = tempstring.splitlines()
    x = templine[0]
    rowlist = x.split('\t')
    subjectTitle_1 = rowlist[2]


    tempstring = "temp"
    tempstring = InputPrestatistics_2.readline()
    tempstring = InputPrestatistics_2.readline()
    templine = tempstring.splitlines()
    x = templine[0]
    rowlist = x.split('\t')
    subjectTitle_2 = rowlist[2]
   

    tempstring = "temp"
    tempstring = InputPrestatistics_3.readline()
    tempstring = InputPrestatistics_3.readline()
    templine = tempstring.splitlines()
    x = templine[0]
    rowlist = x.split('\t')
    subjectTitle_3 = rowlist[2]

    try:
        Image1 = Image.open(InputImage1)
        Image2 = Image.open(InputImage2)
        Image3 = Image.open(InputImage3)


    except:
        print("Unable to load image")

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
    font = ImageFont.truetype("arial.ttf", 40)

    draw.text((1450, 1500),"SAMPLE ID: " + TargetID + " \n" + "SAMPLE NAME: " + SampleName,(0, 0, 0),font=font)
    
    draw.text((1500, 1650),"a) Circular plot showing BLAST alignments of sample sequenced fragments ",(0, 0, 0),font=font)
    draw.text((1500, 1700),"     against the first candidate reference genome.",(0, 0, 0),font=font)
    draw.text((1500, 1750),"     First candidate title:",(0, 0, 0),font=font)
    draw.text((1500, 1800),"    " + subjectTitle_1 + ".",(0, 0, 0),font=font)
    
    draw.text((1500, 1900),"b) Circular plot showing BLAST alignments of sample sequenced fragments ",(0, 0, 0),font=font)
    draw.text((1500, 1950),"     against the second candidate reference genome.",(0, 0, 0),font=font)
    draw.text((1500, 2000),"     Second candidate title:",(0, 0, 0),font=font)
    draw.text((1500, 2050),"    " + subjectTitle_2 + ".",(0, 0, 0),font=font)
    
    draw.text((1500, 2150),"c) Circular plot showing BLAST alignments of sample sequenced fragments ",(0, 0, 0),font=font)
    draw.text((1500, 2200),"     against the third candidate reference genome.",(0, 0, 0),font=font)
    draw.text((1500, 2250),"     Third candidate title:",(0, 0, 0),font=font)
    draw.text((1500, 2300),"    " + subjectTitle_3 + ".",(0, 0, 0),font=font)
    
    draw.text((1500, 2400),"Explanation of circular plots:",(0, 0, 0),font=font)
    draw.text((1500, 2450),"-Outer black circle represents the candidate reference genome with size",(0, 0, 0),font=font)
    draw.text((1500, 2500),"    indicated in megabases (Mb).",(0, 0, 0),font=font)
    draw.text((1500, 2550),"-Middle blue circle shows aligned sequenced fragments obtained by complexity",(0, 0, 0),font=font)
    draw.text((1500, 2600),"    reduced genotyping.",(0, 0, 0),font=font)
    draw.text((1500, 2650),"-Inner green / red circle shows the percentage identity of the alignments. ",(0, 0, 0),font=font)
    draw.text((1500, 2700),"    Values below 95% are red, values equal to or above 95% are green.",(0, 0, 0),font=font)
    result2.save(OutputPathName)
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
