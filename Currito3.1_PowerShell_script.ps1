
$EOL = "`r`n"


$ScriptsDirectory = ""
cd $ScriptsDirectory



$BaseDirectory = ""
$BLASTnt_output = ""
$Cluster_Unclustered_file = ""


$NumberOfColumns_Samples_OFClusteredUnclusteredFile = "20"


$BLASTntPATH = ""
$CircosETC_PATH = ""
$Circos_bin_PATH = ""

$BLASTbinPATH = ""



$FirstSplitPerTargetDirectory = $BaseDirectory + "First_split_per_targetID"
$RowWhereDataStarts = "6"
$SeqIndex = "0"
$TrimmedSequence = "2"

$fso = new-object -ComObject scripting.filesystemobject

$RownWhereDataStartsForClusterUnclusteredFiles = "7"


$Plasmid_directory = $BLASTnt_output + "Plasmid\"
$fso.CreateFolder($Plasmid_directory)


$Genome_directory = $BLASTnt_output + "Genome\"
$fso.CreateFolder($Genome_directory)

$Genome_Plasmid_directory = $BLASTnt_output + "Genome_Plasmid\"
$fso.CreateFolder($Genome_Plasmid_directory)


$BLAST_3_split = $BLASTnt_output + "BLAST_unfiltered\"
$inputFilesBLASTfor3Split = Get-ChildItem $BLAST_3_split

$batchJason0 = $ScriptsDirectory + "split_BLASTnt_into_3.bat"
Add-Content $batchJason0 "echo on`r`n"
for ($i = 0; $i -lt $inputFilesBLASTfor3Split.Count; $i++) {
$commandLine = ("Blast_result_analysis)software.exe  --input_file  " + $inputFilesBLASTfor3Split[$i].FullName +
"  --split_genome_plasmid" +
"  --output_folder  " + $BLASTnt_output) 
Add-Content $batchJason0 $commandLine
}
Start-Process ~PATH\split_BLASTnt_into_3.bat -wait
Write-Output "Spliting BLAST by Plasmids and Chromosomes finished"



$Filtered_Plasmids = $Plasmid_directory + "1_Filtered_Plasmids\"
$FilesBlast1 = Get-ChildItem $Plasmid_directory
$fso.CreateFolder($Filtered_Plasmids)


$BatchJason1 = $ScriptsDirectory + "Blast_result_analysis_software1_PLASMID.bat"

Add-Content $BatchJason1 "echo on`r`n"
for ($i = 0; $i -lt $FilesBlast1.Count; $i++) {
$commandLine = ("Blast_result_analysis)software.exe --input_file  " + $FilesBlast1[$i].FullName +
" --parse_small_blast" +
"  --output_folder  " + $Filtered_Plasmids)
Add-Content $BatchJason1 $commandLine
}
Start-Process ~PATH\Blast_result_analysis_software1_PLASMID.bat -wait
Write-Output "Filtering of BLAST PLASMIDS output finished"


$Filtered_Genomes = $Genome_directory + "1_Filtered_Genomes\"
$FilesBlastGenome = Get-ChildItem $Genome_directory
$fso.CreateFolder($Filtered_Genomes)

$BatchJason1Genome = $ScriptsDirectory + "Blast_result_analysis_software1_GENOME.bat"

Add-Content $BatchJason1Genome "echo on`r`n"
for ($i = 0; $i -lt $FilesBlastGenome.Count; $i++) {
$commandLine = ("Blast_result_analysis)software.exe --input_file  " + $FilesBlastGenome[$i].FullName +
" --parse_small_blast" +
"  --output_folder  " + $Filtered_Genomes)
Add-Content $BatchJason1Genome $commandLine
}
Start-Process ~PATH\Blast_result_analysis_software1_GENOME.bat -wait
Write-Output "Filtering of BLAST GENOMES output finished"



$Filtered_Genomes_Plasmids = $Genome_Plasmid_directory + "1_Filtered_Genomes_Plasmids\"
$FilesBlastGenomePlasmids = Get-ChildItem $Genome_Plasmid_directory
$fso.CreateFolder($Filtered_Genomes_Plasmids)

$BatchJason1GenomePlasmids = $ScriptsDirectory + "Blast_result_analysis_software1_GENOME_PLASMIDS.bat"

Add-Content $BatchJason1GenomePlasmids "echo on`r`n"
for ($i = 0; $i -lt $FilesBlastGenomePlasmids.Count; $i++) {
$commandLine = ("Blast_result_analysis)software.exe --input_file  " + $FilesBlastGenomePlasmids[$i].FullName +
" --parse_small_blast" +
"  --output_folder  " + $Filtered_Genomes_Plasmids)
Add-Content $BatchJason1GenomePlasmids $commandLine
}
Start-Process ~PATH\Blast_result_analysis_software1_GENOME_PLASMIDS.bat -wait
Write-Output "Filtering of BLAST GENOMES AND PLASMIDS output finished"



$Split_cluster_unclustered = $BaseDirectory + "A_Split_cluster_unclustered\"

$fso.CreateFolder($Split_cluster_unclustered)
$filesClusterUnclustered = Get-ChildItem $Cluster_Unclustered_file
$batchFileSplits = $ScriptsDirectory + "Split_Into_Individual_files_With_CountsAbove5.bat"

Add-Content $batchFileSplits "echo on`r`n"
for ($i = 0; $i -lt $filesClusterUnclustered.Count; $i++) {
$commandLine = ("Split_Into_Individual_files_With_CountsAbove5.py -i " + $filesClusterUnclustered[$i].FullName +
" -n " + $NumberOfColumns_Samples_OFClusteredUnclusteredFile +
" -o " + $Split_cluster_unclustered)
Add-Content $batchFileSplits $commandLine

}

Start-Process ~PATH\Split_Into_Individual_files_With_CountsAbove5.bat -wait
Write-Output "Split_Into_Individual_files_With_CountsAbove5 finished"


$FastaFiles_Split_cluster_unclustered = $BaseDirectory + "B_FastaFiles_Split_cluster_unclustered\"

$fso.CreateFolder($FastaFiles_Split_cluster_unclustered)
$fastafilesClusterUnclustered = Get-ChildItem $Split_cluster_unclustered
$batchFastaFileSplits = $ScriptsDirectory + "MakeFastaFiles_individualTargetID.bat"

Add-Content $batchFastaFileSplits "echo on`r`n"
for ($i = 0; $i -lt $fastafilesClusterUnclustered.Count; $i++) {
$commandLine = ("MakeFastaFiles_nonHardCode.py -i " + $fastafilesClusterUnclustered[$i].FullName +
" -o " + $FastaFiles_Split_cluster_unclustered + $fastafilesClusterUnclustered[$i].BaseName + "_fasta.fasta" +
" -u " + $RowWhereDataStarts +
" -s " + $SeqIndex +
" -t " + $TrimmedSequence)
Add-Content $batchFastaFileSplits $commandLine

}
Start-Process ~PATH\MakeFastaFiles_individualTargetID.bat -wait
Write-Output "MakeFastaFiles_individualTargetID finished"




$filesPLASMID = Get-ChildItem $Split_cluster_unclustered 
$batchFilePLASMID = $ScriptsDirectory + "coco_batch_PLASMID.bat"
$First_filt_directoryPLASMID = $Plasmid_directory + "2_First_filt_per_target\" 
$fso.CreateFolder($First_filt_directoryPLASMID)

Add-Content $batchFilePLASMID (Get-Content $Parallel_Batch_Template_Portion1_File)
for ($i = 0; $i -lt $filesPLASMID.Count; $i++) {
$commandLine = ("::: coco.py -i " +  $filesPLASMID[$i].FullName + 
" -j " + $Filtered_Plasmids + "filtered_blast_output.txt" + 
" -o " +  $First_filt_directoryPLASMID + $filesPLASMID[$i].BaseName + "_filtered_blast_results.txt")
Add-Content $batchFilePLASMID $commandLine 
}
Add-Content $batchFilePLASMID (Get-Content $Parallel_Batch_Template_Portion2_File)
Start-Process ~PATH\coco_batch_PLASMID.bat -Wait
Write-Output "coco for PLASMID finished"


$filesGENOME = Get-ChildItem $Split_cluster_unclustered 
$batchFileGENOME = $ScriptsDirectory + "coco_batch_GENOME.bat"
$First_filt_directoryGENOME = $Genome_directory + "2_First_filt_per_target\" 
$fso.CreateFolder($First_filt_directoryGENOME)

Add-Content $batchFileGENOME (Get-Content $Parallel_Batch_Template_Portion1_File)
for ($i = 0; $i -lt $filesGENOME.Count; $i++) {
$commandLine = ("::: coco.py -i " +  $filesGENOME[$i].FullName + 
" -j " + $Filtered_Genomes + "filtered_blast_output.txt" + 
" -o " +  $First_filt_directoryGENOME + $filesGENOME[$i].BaseName + "_filtered_blast_results.txt")
Add-Content $batchFileGENOME $commandLine 
}
Add-Content $batchFileGENOME (Get-Content $Parallel_Batch_Template_Portion2_File)
Start-Process ~PATH\coco_batch_GENOME.bat -Wait
Write-Output "coco for GENOME finished"




$files = Get-ChildItem $Split_cluster_unclustered 
$batchFile = $ScriptsDirectory + "coco_batch.bat"
$First_filt_directory = $Genome_Plasmid_directory + "2_First_filt_per_target\" 
$fso.CreateFolder($First_filt_directory)

Add-Content $batchFile (Get-Content $Parallel_Batch_Template_Portion1_File)
for ($i = 0; $i -lt $files.Count; $i++) {
$commandLine = ("::: coco.py -i " +  $files[$i].FullName + 
" -j " + $Filtered_Genomes_Plasmids + "filtered_blast_output.txt" + 
" -o " +  $First_filt_directory + $files[$i].BaseName + "_filtered_blast_results.txt")
Add-Content $batchFile $commandLine 
}
Add-Content $batchFile (Get-Content $Parallel_Batch_Template_Portion2_File)
Start-Process ~PATH\coco_batch.bat -Wait
Write-Output "coco for GENOME AND PLASMID finished"



$Blast_result_analysis_software2_PLASMID = $Plasmid_directory + "3_Individual_Blast_Filter_analysis\"
$fso.CreateFolder($Blast_result_analysis_software2_PLASMID)
$files11_PLASMID = Get-ChildItem $First_filt_directoryPLASMID
$batchJason2PLASMID = $ScriptsDirectory + "Blast_result_analysis_software2_PLASMID.bat"


Add-Content $batchJason2PLASMID (Get-Content $Parallel_Batch_Template_Portion1_File)
for ($i = 0; $i -lt $files11_PLASMID.Count; $i++) {
$commandLine = ("::: Blast_result_analysis)software.exe  --input_file  " + $files11_PLASMID[$i].FullName +
"  --parse_splitFilt  " +
"  --output_folder  " + $Blast_result_analysis_software2_PLASMID)
Add-Content $batchJason2PLASMID $commandLine
}
Add-Content $batchJason2PLASMID (Get-Content $Parallel_Batch_Template_Portion2_File)
Start-Process ~PATH\Blast_result_analysis_software2_PLASMID.bat -Wait
Write-Output "Blast filtering per individual target ID analysis PLASMID finished"



$Blast_result_analysis_software2_GENOME = $Genome_directory + "3_Individual_Blast_Filter_analysis\"
$fso.CreateFolder($Blast_result_analysis_software2_GENOME)
$files11_GENOME = Get-ChildItem $First_filt_directoryGENOME
$batchJason2GENOME = $ScriptsDirectory + "Blast_result_analysis_software2_GENOME.bat"


Add-Content $batchJason2GENOME (Get-Content $Parallel_Batch_Template_Portion1_File)
for ($i = 0; $i -lt $files11_GENOME.Count; $i++) {
$commandLine = ("::: Blast_result_analysis)software.exe  --input_file  " + $files11_GENOME[$i].FullName +
"  --parse_splitFilt  " +
"  --output_folder  " + $Blast_result_analysis_software2_GENOME)
Add-Content $batchJason2GENOME $commandLine
}
Add-Content $batchJason2GENOME (Get-Content $Parallel_Batch_Template_Portion2_File)
Start-Process ~PATH\Blast_result_analysis_software2_GENOME.bat -Wait
Write-Output "Blast filtering per individual target ID analysis GENOME finished"




$Blast_result_analysis_software2 = $Genome_Plasmid_directory + "3_Individual_Blast_Filter_analysis\"
$fso.CreateFolder($Blast_result_analysis_software2)
$files11 = Get-ChildItem $First_filt_directory
$batchJason2 = $ScriptsDirectory + "Blast_result_analysis_software2.bat"


Add-Content $batchJason2 (Get-Content $Parallel_Batch_Template_Portion1_File)
for ($i = 0; $i -lt $files11.Count; $i++) {
$commandLine = ("::: Blast_result_analysis)software.exe  --input_file  " + $files11[$i].FullName +
"  --parse_splitFilt  " +
"  --output_folder  " + $Blast_result_analysis_software2)
Add-Content $batchJason2 $commandLine
}
Add-Content $batchJason2 (Get-Content $Parallel_Batch_Template_Portion2_File)
Start-Process ~PATH\Blast_result_analysis_software2.bat -Wait
Write-Output "Blast filtering per individual target ID analysis GENOME AND PLASMID finished"



$Filt_condensed_directory_PLASMID = $Plasmid_directory + "4_Filt_condensed_output\"
$fso.CreateFolder($Filt_condensed_directory_PLASMID)
$files2_PLASMID = Get-ChildItem $Blast_result_analysis_software2_PLASMID
$batchFile2_PLASMID = $ScriptsDirectory + "cocu_batch_PLASMID.bat"
Add-Content $batchFile2_PLASMID "echo on`r`n"
for ($i = 0; $i -lt $files2_PLASMID.Count; $i++) {
$commandLine = ("cocu.py -i" + $files2_PLASMID[$i].FullName +
" -o " + $Filt_condensed_directory_PLASMID +  "OutputCondensedMergedResults.txt")
Add-Content $batchFile2_PLASMID $commandLine} 
Start-Process ~PATH\cocu_batch_PLASMID.bat -Wait
Write-Output "cocu PLASMID finished"


$Filt_condensed_directory_GENOME = $Genome_directory + "4_Filt_condensed_output\"
$fso.CreateFolder($Filt_condensed_directory_GENOME)
$files2_GENOME = Get-ChildItem $Blast_result_analysis_software2_GENOME
$batchFile2_GENOME = $ScriptsDirectory + "cocu_batch_GENOME.bat"
Add-Content $batchFile2_GENOME "echo on`r`n"
for ($i = 0; $i -lt $files2_GENOME.Count; $i++) {
$commandLine = ("cocu.py -i" + $files2_GENOME[$i].FullName +
" -o " + $Filt_condensed_directory_GENOME +  "OutputCondensedMergedResults.txt")
Add-Content $batchFile2_GENOME $commandLine} 
Start-Process ~PATH\cocu_batch_GENOME.bat -Wait
Write-Output "cocu GENOME finished"



$Filt_condensed_directory = $Genome_Plasmid_directory + "4_Filt_condensed_output\"
$fso.CreateFolder($Filt_condensed_directory)
$files2 = Get-ChildItem $Blast_result_analysis_software2
$batchFile2 = $ScriptsDirectory + "cocu_batch.bat"
Add-Content $batchFile2 "echo on`r`n"
for ($i = 0; $i -lt $files2.Count; $i++) {
$commandLine = ("cocu.py -i" + $files2[$i].FullName +
" -o " + $Filt_condensed_directory +  "OutputCondensedMergedResults.txt")
Add-Content $batchFile2 $commandLine} 
Start-Process ~PATH\cocu_batch.bat -Wait
Write-Output "cocu GENOME AND PLASMID finished"


$Split_Condensed_results_PLASMID = $Plasmid_directory + "5_Split_Condensed_output\"
$fso.CreateFolder($Split_Condensed_results_PLASMID)
$files3_PLASMID = Get-ChildItem $Filt_condensed_directory_PLASMID
$NonBatchFile3_PLASMID = $ScriptsDirectory + "Splits_per_target_ID_and_save_TOP_3_accession_numbers_PLASMID.bat"
Add-Content $NonBatchFile3_PLASMID "echo on`r`n"
for ($i = 0; $i -lt $files3_PLASMID.Count; $i++) {
$commandLine = ("Splits_per_target_ID_and_save_TOP_3_accession_numbers.py -i" + $files3_PLASMID[$i].FullName +
" -o " + $Split_Condensed_results_PLASMID)
Add-Content $NonBatchFile3_PLASMID $commandLine}
Start-Process ~PATH\Splits_per_target_ID_and_save_TOP_3_accession_numbers_PLASMID.bat -wait
Write-Output "Split of merged results by target ID and top 3 candidate accesion numbers finished _PLASMID"


$Split_Condensed_results_GENOME = $Genome_directory + "5_Split_Condensed_output\"
$fso.CreateFolder($Split_Condensed_results_GENOME)
$files3_GENOME = Get-ChildItem $Filt_condensed_directory_GENOME
$NonBatchFile3_GENOME = $ScriptsDirectory + "Splits_per_target_ID_and_save_TOP_3_accession_numbers_GENOME.bat"
Add-Content $NonBatchFile3_GENOME "echo on`r`n"
for ($i = 0; $i -lt $files3_GENOME.Count; $i++) {
$commandLine = ("Splits_per_target_ID_and_save_TOP_3_accession_numbers.py -i" + $files3_GENOME[$i].FullName +
" -o " + $Split_Condensed_results_GENOME)
Add-Content $NonBatchFile3_GENOME $commandLine}
Start-Process ~PATH\Splits_per_target_ID_and_save_TOP_3_accession_numbers_GENOME.bat -wait
Write-Output "Split of merged results by target ID and top 3 candidate accesion numbers finished _GENOME"



$Split_Condensed_results = $Genome_Plasmid_directory + "5_Split_Condensed_output\"
$fso.CreateFolder($Split_Condensed_results)
$files3 = Get-ChildItem $Filt_condensed_directory
$NonBatchFile3 = $ScriptsDirectory + "Splits_per_target_ID_and_save_TOP_3_accession_numbers.bat"
Add-Content $NonBatchFile3 "echo on`r`n"
for ($i = 0; $i -lt $files3.Count; $i++) {
$commandLine = ("Splits_per_target_ID_and_save_TOP_3_accession_numbers.py -i" + $files3[$i].FullName +
" -o " + $Split_Condensed_results)
Add-Content $NonBatchFile3 $commandLine}
Start-Process ~PATH\Splits_per_target_ID_and_save_TOP_3_accession_numbers.bat -wait
Write-Output "Split of merged results by target ID and top 3 candidate accesion numbers finished"



$IndividualBLASTV2_8_PLASMID = $Plasmid_directory + "6_Individual_BLASTv2_8\"
$fso.CreateFolder($IndividualBLASTV2_8_PLASMID)
$filesBatchX_PLASMID = Get-ChildItem $Split_Condensed_results_PLASMID
$batchForIndividualBLAST_PLASMID = $ScriptsDirectory +"Individual_BLAST_PLASMID.bat"

$changeToBLASTdir = "cd " + $BLASTbinPATH

Add-Content $batchForIndividualBLAST_PLASMID "echo on`r`n"
Add-Content $batchForIndividualBLAST_PLASMID $changeToBLASTdir
for ($i = 0; $i -lt $filesBatchX_PLASMID.Count; $i++){
$SingleName = $filesBatchX_PLASMID[$i].basename 
$temp_array = $SingleName.split("{_}")
Write-Host $temp_array[0]

$commandLine = ("blastn -db " + $BLASTntPATH + "nt" +
" -query " + $FastaFiles_Split_cluster_unclustered + $temp_array[0] + "_fasta.fasta" + 
" -word_size 10 -evalue 1 -outfmt `"6 qseqid sacc stitle qseq sseq nident mismatch pident length evalue bitscore qstart qend sstart send gapopen gaps qlen slen`"" +
" -seqidlist " + $filesBatchX_PLASMID[$i].FullName + " -out " + $IndividualBLASTV2_8_PLASMID +
$SingleName + "_BLAST.txt")
Add-Content $batchForIndividualBLAST_PLASMID $commandLine}
Start-Process ~PATH\Individual_BLAST_PLASMID.bat -wait
Write-Output "Individual BLAST PLASMID finished"



$IndividualBLASTV2_8_GENOME = $Genome_directory + "6_Individual_BLASTv2_8\"
$fso.CreateFolder($IndividualBLASTV2_8_GENOME)
$filesBatchX_GENOME = Get-ChildItem $Split_Condensed_results_GENOME
$batchForIndividualBLAST_GENOME = $ScriptsDirectory +"Individual_BLAST_GENOME.bat"

Add-Content $batchForIndividualBLAST_GENOME "echo on`r`n"
Add-Content $batchForIndividualBLAST_GENOME $changeToBLASTdir
for ($i = 0; $i -lt $filesBatchX_GENOME.Count; $i++){
$SingleName = $filesBatchX_GENOME[$i].basename 
$temp_array = $SingleName.split("{_}")
Write-Host $temp_array[0]

$commandLine = ("blastn -db " + $BLASTntPATH + "nt" +
" -query " + $FastaFiles_Split_cluster_unclustered + $temp_array[0] + "_fasta.fasta" + 
" -word_size 10 -evalue 1 -outfmt `"6 qseqid sacc stitle qseq sseq nident mismatch pident length evalue bitscore qstart qend sstart send gapopen gaps qlen slen`"" +
" -seqidlist " + $filesBatchX_GENOME[$i].FullName + " -out " + $IndividualBLASTV2_8_GENOME +
$SingleName + "_BLAST.txt")
Add-Content $batchForIndividualBLAST_GENOME $commandLine}
Start-Process ~PATH\Individual_BLAST_GENOME.bat -wait
Write-Output "Individual BLAST GENOME finished"




$IndividualBLASTV2_8 = $Genome_Plasmid_directory + "6_Individual_BLASTv2_8\"
$fso.CreateFolder($IndividualBLASTV2_8)
$filesBatchX = Get-ChildItem $Split_Condensed_results
$batchForIndividualBLAST = $ScriptsDirectory +"Individual_BLAST.bat"

Add-Content $batchForIndividualBLAST "echo on`r`n"
Add-Content $batchForIndividualBLAST $changeToBLASTdir
for ($i = 0; $i -lt $filesBatchX.Count; $i++){
$SingleName = $filesBatchX[$i].basename 
$temp_array = $SingleName.split("{_}")
Write-Host $temp_array[0]

$commandLine = ("blastn -db " + $BLASTntPATH + "nt" +
" -query " + $FastaFiles_Split_cluster_unclustered + $temp_array[0] + "_fasta.fasta" + 
" -word_size 10 -evalue 1 -outfmt `"6 qseqid sacc stitle qseq sseq nident mismatch pident length evalue bitscore qstart qend sstart send gapopen gaps qlen slen`"" +
" -seqidlist " + $filesBatchX[$i].FullName + " -out " + $IndividualBLASTV2_8 +
$SingleName + "_BLAST.txt")
Add-Content $batchForIndividualBLAST $commandLine}
Start-Process ~PATH\Individual_BLAST.bat -wait
Write-Output "Individual BLAST GENOME AND PLASMID finished"



$Blast_result_analysis_software3_PLASMID = $Plasmid_directory + "7_Filtering_Split_condensed_output\"
$fso.CreateFolder($Blast_result_analysis_software3_PLASMID)
$filesIndividualBLAST_PLASMID = Get-ChildItem $IndividualBLASTV2_8_PLASMID
$batchJason3_PLASMID = $ScriptsDirectory + "Blast_result_analysis_software3_PLASMID.bat"


Add-Content $batchJason3_PLASMID (Get-Content $Parallel_Batch_Template_Portion1_File)
for ($i = 0; $i -lt $filesIndividualBLAST_PLASMID.Count; $i++) {
$commandLine = ("::: Blast_result_analysis)software.exe  --input_file  " + $filesIndividualBLAST_PLASMID[$i].FullName +
"  --parse_small_blast  " + 
"  --output_folder  " + $Blast_result_analysis_software3_PLASMID +
"  --output_file_name  " + $filesIndividualBLAST_PLASMID[$i].BaseName + "_filtered_blast.txt" )
Add-Content $batchJason3_PLASMID $commandLine}
Add-Content $batchJason3_PLASMID (Get-Content $Parallel_Batch_Template_Portion2_File)
Start-Process ~PATH\Blast_result_analysis_software3_PLASMID.bat -Wait
Write-Output "Blast filtering per individual target ID analysis software3 PLASMID finished"




$Blast_result_analysis_software3_GENOME = $Genome_directory + "7_Filtering_Split_condensed_output\"
$fso.CreateFolder($Blast_result_analysis_software3_GENOME)
$filesIndividualBLAST_GENOME = Get-ChildItem $IndividualBLASTV2_8_GENOME
$batchJason3_GENOME = $ScriptsDirectory + "Blast_result_analysis_software3_GENOME.bat"


Add-Content $batchJason3_GENOME (Get-Content $Parallel_Batch_Template_Portion1_File)
for ($i = 0; $i -lt $filesIndividualBLAST_GENOME.Count; $i++) {
$commandLine = ("::: Blast_result_analysis)software.exe  --input_file  " + $filesIndividualBLAST_GENOME[$i].FullName +
"  --parse_small_blast  " + 
"  --output_folder  " + $Blast_result_analysis_software3_GENOME +
"  --output_file_name  " + $filesIndividualBLAST_GENOME[$i].BaseName + "_filtered_blast.txt" )
Add-Content $batchJason3_GENOME $commandLine}
Add-Content $batchJason3_GENOME (Get-Content $Parallel_Batch_Template_Portion2_File)
Start-Process ~PATH\Blast_result_analysis_software3_GENOME.bat -Wait
Write-Output "Blast filtering per individual target ID analysis software3 GENOME finished"



$Blast_result_analysis_software3 = $Genome_Plasmid_directory + "7_Filtering_Split_condensed_output\"
$fso.CreateFolder($Blast_result_analysis_software3)
$filesIndividualBLAST = Get-ChildItem $IndividualBLASTV2_8
$batchJason3 = $ScriptsDirectory + "Blast_result_analysis_software3.bat"


Add-Content $batchJason3 (Get-Content $Parallel_Batch_Template_Portion1_File)
for ($i = 0; $i -lt $filesIndividualBLAST.Count; $i++) {
$commandLine = ("::: Blast_result_analysis)software.exe  --input_file  " + $filesIndividualBLAST[$i].FullName +
"  --parse_small_blast  " + 
"  --output_folder  " + $Blast_result_analysis_software3 +
"  --output_file_name  " + $filesIndividualBLAST[$i].BaseName + "_filtered_blast.txt" )
Add-Content $batchJason3 $commandLine}
Add-Content $batchJason3 (Get-Content $Parallel_Batch_Template_Portion2_File)
Start-Process ~PATH\Blast_result_analysis_software3.bat -Wait
Write-Output "Blast filtering per individual target ID analysis software3 GENOME AND PLASMID finished"




$PreCircos_PLASMID = $Plasmid_directory + "13_Pre_Circos\"
$fso.CreateFolder($PreCircos_PLASMID)

$IndividualDirectoriesNamesPreCircos_PLASMID = Get-ChildItem $Split_Condensed_results_PLASMID
for ($i = 0; $i -lt $IndividualDirectoriesNamesPreCircos_PLASMID.Count; $i++) {
$currentDirectoryPathAndName_PLASMID = $PreCircos_PLASMID + $IndividualDirectoriesNamesPreCircos_PLASMID[$i].BaseName + "\" 
$fso.CreateFolder($currentDirectoryPathAndName_PLASMID)
}




$PreCircos_GENOME =  $Genome_directory + "13_Pre_Circos\"
$fso.CreateFolder($PreCircos_GENOME)

$IndividualDirectoriesNamesPreCircos_GENOME = Get-ChildItem $Split_Condensed_results_GENOME
for ($i = 0; $i -lt $IndividualDirectoriesNamesPreCircos_GENOME.Count; $i++) {
$currentDirectoryPathAndName_GENOME = $PreCircos_GENOME + $IndividualDirectoriesNamesPreCircos_GENOME[$i].BaseName + "\" 
$fso.CreateFolder($currentDirectoryPathAndName_GENOME)
}





$PreCircos = $Genome_Plasmid_directory + "13_PreCircos\"
$fso.CreateFolder($PreCircos)

$IndividualDirectoriesNamesPreCircos = Get-ChildItem $Split_Condensed_results
for ($i = 0; $i -lt $IndividualDirectoriesNamesPreCircos.Count; $i++) {
$currentDirectoryPathAndName = $PreCircos + $IndividualDirectoriesNamesPreCircos[$i].BaseName + "\" 
$fso.CreateFolder($currentDirectoryPathAndName)
}





$Pre_statistics_arrangement_PLASMID = $Plasmid_directory + "8_Pre_statistics_output\"
$fso.CreateFolder($Pre_statistics_arrangement_PLASMID)
$filesPreStatistics_PLASMID = Get-ChildItem $Blast_result_analysis_software3_PLASMID
$batchPreStatistics_PLASMID = $ScriptsDirectory + "Pre_stat_PLASMID.bat"

Add-Content $batchPreStatistics_PLASMID (Get-Content $Parallel_Batch_Template_Portion1_File)
for ($i = 0; $i -lt $filesPreStatistics_PLASMID.Count; $i++) {
$SingleName = $filesPreStatistics_PLASMID[$i].basename
$temp_array = $SingleName.split("{_}")
$TargetID = $temp_array[0] 
$CandidateNumber = $temp_array[1]
$CandidateString = ""
switch ($CandidateNumber)
{
    1 {$CandidateString = 'first_candidate'}
    2 {$CandidateString = 'second_candidate'}
    3 {$CandidateString = 'third_candidate'}

    }
$PathForW = $PreCircos_PLASMID + $TargetID + "_" + $CandidateNumber + "\"
$commandLine = ("::: preparation_for_statistics_PLASMID.py  -i " + $filesPreStatistics_PLASMID[$i].FullName +
" -o " + $Pre_statistics_arrangement_PLASMID + $filesPreStatistics_PLASMID[$i].BaseName + "Pre_Stat.txt" +
" -c " + $CandidateString +
" -t " + $TargetID +
" -w " + $PathForW +
" -y " + $CircosETC_PATH
)
Add-Content $batchPreStatistics_PLASMID $commandLine}
Add-Content $batchPreStatistics_PLASMID (Get-Content $Parallel_Batch_Template_Portion2_File)
Start-Process ~PATH\Pre_stat_PLASMID.bat -Wait
Write-Output "Pre statistics and CIRCOS input files for PLASMID script finished"




$Pre_statistics_arrangement_GENOME = $Genome_directory + "8_Pre_statistics_output\"
$fso.CreateFolder($Pre_statistics_arrangement_GENOME)
$filesPreStatistics_GENOME = Get-ChildItem $Blast_result_analysis_software3_GENOME
$batchPreStatistics_GENOME = $ScriptsDirectory + "Pre_stat_GENOME.bat"

Add-Content $batchPreStatistics_GENOME (Get-Content $Parallel_Batch_Template_Portion1_File)
for ($i = 0; $i -lt $filesPreStatistics_GENOME.Count; $i++) {
$SingleName = $filesPreStatistics_GENOME[$i].basename
$temp_array = $SingleName.split("{_}")
$TargetID = $temp_array[0] 
$CandidateNumber = $temp_array[1]
$CandidateString = ""
switch ($CandidateNumber)
{
    1 {$CandidateString = 'first_candidate'}
    2 {$CandidateString = 'second_candidate'}
    3 {$CandidateString = 'third_candidate'}

    }
$PathForW = $PreCircos_GENOME + $TargetID + "_" + $CandidateNumber + "\"
$commandLine = ("::: preparation_for_statistics.py  -i " + $filesPreStatistics_GENOME[$i].FullName +
" -o " + $Pre_statistics_arrangement_GENOME + $filesPreStatistics_GENOME[$i].BaseName + "Pre_Stat.txt" +
" -c " + $CandidateString +
" -t " + $TargetID +
" -w " + $PathForW +
" -y " + $CircosETC_PATH
)
Add-Content $batchPreStatistics_GENOME $commandLine}
Add-Content $batchPreStatistics_GENOME (Get-Content $Parallel_Batch_Template_Portion2_File)
Start-Process ~PATH\Pre_stat_GENOME.bat -Wait
Write-Output "Pre statistics and CIRCOS input files for GENOME script finished"




$Pre_statistics_arrangement = $Genome_Plasmid_directory + "8_Pre_statistics_output\"
$fso.CreateFolder($Pre_statistics_arrangement)
$filesPreStatistics = Get-ChildItem $Blast_result_analysis_software3
$batchPreStatistics = $ScriptsDirectory + "Pre_stat.bat"


Add-Content $batchPreStatistics (Get-Content $Parallel_Batch_Template_Portion1_File)
for ($i = 0; $i -lt $filesPreStatistics.Count; $i++) {
$SingleName = $filesPreStatistics[$i].basename
$temp_array = $SingleName.split("{_}")
$TargetID = $temp_array[0] 
$CandidateNumber = $temp_array[1]
$CandidateString = ""
switch ($CandidateNumber)
{
    1 {$CandidateString = 'first_candidate'}
    2 {$CandidateString = 'second_candidate'}
    3 {$CandidateString = 'third_candidate'}

    }
$PathForW = $PreCircos + $TargetID + "_" + $CandidateNumber + "\"
$commandLine = ("::: preparation_for_statistics.py  -i " + $filesPreStatistics[$i].FullName +
" -o " + $Pre_statistics_arrangement + $filesPreStatistics[$i].BaseName + "Pre_Stat.txt" +
" -c " + $CandidateString +
" -t " + $TargetID +
" -w " + $PathForW +
" -y " + $CircosETC_PATH
)

Add-Content $batchPreStatistics $commandLine}
Add-Content $batchPreStatistics (Get-Content $Parallel_Batch_Template_Portion2_File)
Start-Process ~PATH\Pre_stat.bat -Wait
Write-Output "Pre statistics and CIRCOS input files for GENOME AND PLASMID script finished"




$ProportionsInCommon = $Genome_directory + "8c_Proportions_in_common\"
$fso.CreateFolder($ProportionsInCommon)
$InputFilesProportionsInCommon = Get-ChildItem $Pre_statistics_arrangement_GENOME
$BatchProportionInCommon = $ScriptsDirectory + "Proportions.bat"
Add-Content $BatchProportionInCommon "echo on`r`n"




for ($i = 0; $i -lt $InputFilesProportionsInCommon.Count; $i++) {

$SingleName = $filesPreStatistics_GENOME[$i].basename
$temp_array = $SingleName.split("{_}")
$TargetID = $temp_array[0] 
$CandidateNumber = $temp_array[1]


$PathForCircosInput_GENOME = $PreCircos_GENOME + $TargetID + "_" + $CandidateNumber + "\"

$commandLine = ("candidates_proportion.py -i " + $Pre_statistics_arrangement_GENOME + $TargetID + "_1"  + "_BLAST_filtered_blastPre_Stat.txt" +
" -j " + $Pre_statistics_arrangement_GENOME + $TargetID + "_2"  + "_BLAST_filtered_blastPre_Stat.txt" +
" -k " + $Pre_statistics_arrangement_GENOME + $TargetID + "_3"  + "_BLAST_filtered_blastPre_Stat.txt" +
" -o " + $ProportionsInCommon + $TargetID +"_intersections_and_unions.txt" +
" -t " + $TargetID

)
Add-content $BatchProportionInCommon $commandLine}
Start-Process ~PATH\Proportions.bat -wait
Write-Output "Intersections and unions between sets is completed"



 
$Statistics_PLASMID = $Plasmid_directory + "9_statistics\"
$fso.CreateFolder($Statistics_PLASMID)
$filesStatistics_PLASMID = Get-ChildItem $Pre_statistics_arrangement_PLASMID
$batchStatistics_PLASMID = $ScriptsDirectory + "statistics_PLASMID.bat"
Add-content $batchStatistics_PLASMID "echo on `r`n"

$header_only_commandLine_PLASMID = ("Blast_result_analysis)software.exe --write_stats_header --output_folder " + $Statistics_PLASMID)
Add-Content $batchStatistics_PLASMID $header_only_commandLine_PLASMID

for ($i = 0; $i -lt $filesStatistics_PLASMID.Count; $i++) {
$SingleName = $filesStatistics_PLASMID[$i].basename 
$temp_array = $SingleName.split("{_}")
$sampleID = $temp_array[0] + "_"+ $temp_array[1]
$commandLine = ("Blast_result_analysis)software.exe  --input_file  " + $filesStatistics_PLASMID[$i].FullName +
"  --generate_stats  " +
"  --sampleID  " + $sampleID +
"  --output_folder  " + $Statistics_PLASMID)
Add-Content $batchStatistics_PLASMID $commandLine }
Start-Process ~PATH\statistics_PLASMID.bat -Wait
Write-Output "Statistics PLASMID script finished"



$Statistics_GENOME = $Genome_directory + "9_statistics\"
$fso.CreateFolder($Statistics_GENOME)
$filesStatistics_GENOME = Get-ChildItem $Pre_statistics_arrangement_GENOME
$batchStatistics_GENOME = $ScriptsDirectory + "statistics_GENOME.bat"
Add-content $batchStatistics_GENOME "echo on `r`n"

$header_only_commandLine_GENOME = ("Blast_result_analysis)software.exe --write_stats_header --output_folder " + $Statistics_GENOME)
Add-Content $batchStatistics_GENOME $header_only_commandLine_GENOME

for ($i = 0; $i -lt $filesStatistics_GENOME.Count; $i++) {
$SingleName = $filesStatistics_GENOME[$i].basename 
$temp_array = $SingleName.split("{_}")
$sampleID = $temp_array[0] + "_"+ $temp_array[1]
$commandLine = ("Blast_result_analysis)software.exe  --input_file  " + $filesStatistics_GENOME[$i].FullName +
"  --generate_stats  " +
"  --sampleID  " + $sampleID +
"  --output_folder  " + $Statistics_GENOME)
Add-Content $batchStatistics_GENOME $commandLine }
Start-Process ~PATH\statistics_GENOME.bat -Wait
Write-Output "Statistics GENOME script finished"



$Statistics = $Genome_Plasmid_directory + "9_statistics\"
$fso.CreateFolder($Statistics)
$filesStatistics = Get-ChildItem $Pre_statistics_arrangement
$batchStatistics = $ScriptsDirectory + "statistics.bat"
Add-content $batchStatistics "echo on `r`n"

$header_only_commandLine = ("Blast_result_analysis)software.exe --write_stats_header --output_folder " + $Statistics)
Add-Content $batchStatistics $header_only_commandLine

for ($i = 0; $i -lt $filesStatistics.Count; $i++) {
$SingleName = $filesStatistics[$i].basename 
$temp_array = $SingleName.split("{_}")
$sampleID = $temp_array[0] + "_"+ $temp_array[1]
$commandLine = ("Blast_result_analysis)software.exe  --input_file  " + $filesStatistics[$i].FullName +
"  --generate_stats  " +
"  --sampleID  " + $sampleID +
"  --output_folder  " + $Statistics)
Add-Content $batchStatistics $commandLine }
Start-Process ~PATH\statistics.bat -Wait
Write-Output "Statistics GENOME AND PLASMID script finished"



$NameAccessions_PLASMID = $Plasmid_directory + "10_accession_numbers\"
$fso.CreateFolder($NameAccessions_PLASMID)
$filesNameAccessions_PLASMID = Get-ChildItem $Split_Condensed_results_PLASMID
$batchNameAccessionNumbers_PLASMID = $ScriptsDirectory + "Name_accessions_PLASMID.bat"
Add-content $batchNameAccessionNumbers_PLASMID "echo on `r`n"
for ($i = 0; $i -lt $filesNameAccessions_PLASMID.Count; $i++) {
$commandLine = ("AccessionNumbers.py  -i " + $filesNameAccessions_PLASMID[$i].FullName +
" -o " + $NameAccessions_PLASMID)
Add-Content $batchNameAccessionNumbers_PLASMID $commandLine}
Start-Process ~PATH\Name_accessions_PLASMID.bat -Wait
Write-Output "Getting accession numbers FOR PLASMIDS in the title of the document finished"



$NameAccessions_GENOME = $Genome_directory + "10_accession_numbers\"
$fso.CreateFolder($NameAccessions_GENOME)
$filesNameAccessions_GENOME = Get-ChildItem $Split_Condensed_results_GENOME
$batchNameAccessionNumbers_GENOME = $ScriptsDirectory + "Name_accessions_GENOME.bat"
Add-content $batchNameAccessionNumbers_GENOME "echo on `r`n"
for ($i = 0; $i -lt $filesNameAccessions_GENOME.Count; $i++) {
$commandLine = ("AccessionNumbers.py  -i " + $filesNameAccessions_GENOME[$i].FullName +
" -o " + $NameAccessions_GENOME)
Add-Content $batchNameAccessionNumbers_GENOME $commandLine}
Start-Process ~PATH\Name_accessions_GENOME.bat -Wait
Write-Output "Getting accession numbers FOR GENOMES in the title of the document finished"



$NameAccessions = $Genome_Plasmid_directory + "10_accession_numbers\"
$fso.CreateFolder($NameAccessions)
$filesNameAccessions = Get-ChildItem $Split_Condensed_results
$batchNameAccessionNumbers = $ScriptsDirectory + "Name_accessions.bat"
Add-content $batchNameAccessionNumbers "echo on `r`n"
for ($i = 0; $i -lt $filesNameAccessions.Count; $i++) {
$commandLine = ("AccessionNumbers.py  -i " + $filesNameAccessions[$i].FullName +
" -o " + $NameAccessions )
Add-Content $batchNameAccessionNumbers $commandLine}
Start-Process ~PATH\Name_accessions.bat -Wait
Write-Output "Getting accession numbers FOR GENOMES AND PLASMIDS in the title of the document finished"





$changeToBLASTdir = "cd " + $BLASTbinPATH 


$PullIndividualGenomes_PLASMID = $Plasmid_directory + "11_individual_genomes\"
$fso.CreateFolder($PullIndividualGenomes_PLASMID)
$filesIndividualGenomes_PLASMID = Get-ChildItem $NameAccessions_PLASMID
$batchIndividualGenomes_PLASMID = $ScriptsDirectory + "IndividualGenomes_PLASMID.bat"
Add-Content $batchIndividualGenomes_PLASMID "echo on `r`n"
Add-Content $batchIndividualGenomes_PLASMID $changeToBLASTdir

for ($i = 0; $i -lt $filesIndividualGenomes_PLASMID.count; $i++) {
$commandLine = ("blastdbcmd -db " + $BLASTntPATH  + "nt" +
" -entry_batch " + $filesIndividualGenomes_PLASMID[$i].FullName +
" -out " + $PullIndividualGenomes_PLASMID + $filesIndividualGenomes_PLASMID[$i].BaseName + "_.txt")
Add-Content $batchIndividualGenomes_PLASMID $commandLine}
Start-Process ~PATH\IndividualGenomes_PLASMID.bat -wait
Write-Output "Pulling individual genomes from nt database (PLASMID ONLY), finished"




$PullIndividualGenomes_GENOME = $Genome_directory + "11_individual_genomes\"
$fso.CreateFolder($PullIndividualGenomes_GENOME)
$filesIndividualGenomes_GENOME = Get-ChildItem $NameAccessions_GENOME
$batchIndividualGenomes_GENOME = $ScriptsDirectory + "IndividualGenomes_GENOME.bat"
Add-Content $batchIndividualGenomes_GENOME "echo on `r`n"
Add-Content $batchIndividualGenomes_GENOME $changeToBLASTdir

for ($i = 0; $i -lt $filesIndividualGenomes_GENOME.count; $i++) {
$commandLine = ("blastdbcmd -db " + $BLASTntPATH  + "nt" +
" -entry_batch " + $filesIndividualGenomes_GENOME[$i].FullName +
" -out " + $PullIndividualGenomes_GENOME + $filesIndividualGenomes_GENOME[$i].BaseName + "_.txt")
Add-Content $batchIndividualGenomes_GENOME $commandLine}
Start-Process ~PATH\IndividualGenomes_GENOME.bat -wait
Write-Output "Pulling individual genomes from nt database (GENOME ONLY), finished"




$PullIndividualGenomes = $Genome_Plasmid_directory + "11_individual_genomes\"
$fso.CreateFolder($PullIndividualGenomes)
$filesIndividualGenomes = Get-ChildItem $NameAccessions
$batchIndividualGenomes = $ScriptsDirectory + "IndividualGenomes.bat"
Add-Content $batchIndividualGenomes "echo on `r`n"
Add-Content $batchIndividualGenomes $changeToBLASTdir

for ($i = 0; $i -lt $filesIndividualGenomes.count; $i++) {
$commandLine = ("blastdbcmd -db " + $BLASTntPATH  + "nt" +
" -entry_batch " + $filesIndividualGenomes[$i].FullName +
" -out " + $PullIndividualGenomes + $filesIndividualGenomes[$i].BaseName + "_.txt")
Add-Content $batchIndividualGenomes $commandLine}
Start-Process ~PATH\IndividualGenomes.bat -wait
Write-Output "Pulling individual genomes from nt database (GENOME AND PLASMID), finished"




$InSilicos_PLASMID = $Plasmid_directory + "12_InsilicoAnalysis\"
$fso.CreateFolder($InSilicos_PLASMID)
$filesInputInsilicos_PLASMID = Get-ChildItem $PullIndividualGenomes_PLASMID
$batchInSilicos_PLASMID = $ScriptsDirectory + "InSilico_PLASMID.bat"


Add-Content $batchInSilicos_PLASMID (Get-Content $Parallel_Batch_Template_Portion1_File)
for ($i = 0; $i -lt  $filesInputInsilicos_PLASMID.count; $i++) {
$commandLine = ("::: Enzyme_cut_test.py -i " + $filesInputInsilicos_PLASMID[$i].FullName +
" -o " + $InSilicos_PLASMID + $filesInputInsilicos_PLASMID[$i].BaseName + "_output_data.txt" +
" -p " + $InSilicos_PLASMID + $filesInputInsilicos_PLASMID[$i].BaseName + "_PstI_HpaII_fragments.txt" +
" -q " + $InSilicos_PLASMID + $filesInputInsilicos_PLASMID[$i].BaseName + "_PstI_MseI_fragments.txt" +
" -r " + $InSilicos_PLASMID + $filesInputInsilicos_PLASMID[$i].BaseName + "_MseI_HpaII_fragments.txt")
Add-Content $batchInSilicos_PLASMID $commandLine}
Add-Content $batchInSilicos_PLASMID (Get-Content $Parallel_Batch_Template_Portion2_File)
Start-Process ~PATH\InSilico_PLASMID.bat -wait
Write-Output "InSilico analysis PLASMIDS finished"



$InSilicos_GENOME = $Genome_directory + "12_InsilicoAnalysis\"
$fso.CreateFolder($InSilicos_GENOME)
$filesInputInsilicos_GENOME = Get-ChildItem $PullIndividualGenomes_GENOME
$batchInSilicos_GENOME = $ScriptsDirectory + "InSilico_GENOME.bat"


Add-Content $batchInSilicos_GENOME (Get-Content $Parallel_Batch_Template_Portion1_File)
for ($i = 0; $i -lt  $filesInputInsilicos_GENOME.count; $i++) {
$commandLine = ("::: Enzyme_cut_test.py -i " + $filesInputInsilicos_GENOME[$i].FullName +
" -o " + $InSilicos_GENOME + $filesInputInsilicos_GENOME[$i].BaseName + "_output_data.txt" +
" -p " + $InSilicos_GENOME + $filesInputInsilicos_GENOME[$i].BaseName + "_PstI_HpaII_fragments.txt" +
" -q " + $InSilicos_GENOME + $filesInputInsilicos_GENOME[$i].BaseName + "_PstI_MseI_fragments.txt" +
" -r " + $InSilicos_GENOME + $filesInputInsilicos_GENOME[$i].BaseName + "_MseI_HpaII_fragments.txt")
Add-Content $batchInSilicos_GENOME $commandLine}
Add-Content $batchInSilicos_GENOME (Get-Content $Parallel_Batch_Template_Portion2_File)
Start-Process ~PATH\InSilico_GENOME.bat -wait
Write-Output "InSilico analysis GENOME finished"



$InSilicos = $Genome_Plasmid_directory + "12_InsilicoAnalysis\"
$fso.CreateFolder($InSilicos)
$filesInputInsilicos = Get-ChildItem $PullIndividualGenomes
$batchInSilicos = $ScriptsDirectory + "InSilico.bat"


Add-Content $batchInSilicos (Get-Content $Parallel_Batch_Template_Portion1_File)
for ($i = 0; $i -lt  $filesInputInsilicos.count; $i++) {
$commandLine = ("::: Enzyme_cut_test.py -i " + $filesInputInsilicos[$i].FullName +
" -o " + $InSilicos + $filesInputInsilicos[$i].BaseName + "_output_data.txt" +
" -p " + $InSilicos + $filesInputInsilicos[$i].BaseName + "_PstI_HpaII_fragments.txt" +
" -q " + $InSilicos + $filesInputInsilicos[$i].BaseName + "_PstI_MseI_fragments.txt" +
" -r " + $InSilicos + $filesInputInsilicos[$i].BaseName + "_MseI_HpaII_fragments.txt")
Add-Content $batchInSilicos $commandLine}
Add-Content $batchInSilicos (Get-Content $Parallel_Batch_Template_Portion2_File)
Start-Process ~PATH\InSilico.bat -wait
Write-Output "InSilico analysis GENOME AND PLASMID finished"



$circos_PLASMID = $Plasmid_directory + "14_circos\"
$fso.CreateFolder($circos_PLASMID)

$IndividualDirectoriesNamesCIRCOS_PLASMID = Get-ChildItem  $PreCircos_PLASMID
$batchCIRCOS_PLASMID = $ScriptsDirectory + "circos_PLASMID.bat"

Add-Content $batchCIRCOS_PLASMID (Get-Content $Parallel_Batch_Template_Portion1_File)

for ($i = 0; $i -lt $IndividualDirectoriesNamesCIRCOS_PLASMID.Count; $i++) {

$SingleName = $filesPreStatistics_PLASMID[$i].basename
$temp_array = $SingleName.split("{_}")
$TargetID = $temp_array[0] 
$CandidateNumber = $temp_array[1]

$PathForCircosInput_PLASMID = $PreCircos_PLASMID + $TargetID + "_" + $CandidateNumber + "\"

$commandLine = ("::: " + $Circos_bin_PATH + "circos -outputfile " + $TargetID + "_" + $CandidateNumber +
" -outputdir " + $circos_PLASMID + " -conf " + $PathForCircosInput_PLASMID + "Conf.txt"
)

Add-content $batchCIRCOS_PLASMID $commandLine}

Add-Content $batchCIRCOS_PLASMID (Get-Content $Parallel_Batch_Template_Portion2_File)
Start-Process ~PATH\circos_PLASMID.bat -Wait
Write-Output "Circus plot for PLASMID finished"




$circos_GENOME = $Genome_directory + "14_circos\"
$fso.CreateFolder($circos_GENOME)

$IndividualDirectoriesNamesCIRCOS_GENOME = Get-ChildItem  $PreCircos_GENOME
$batchCIRCOS_GENOME = $ScriptsDirectory + "circos_GENOME.bat"


Add-Content $batchCIRCOS_GENOME (Get-Content $Parallel_Batch_Template_Portion1_File)

for ($i = 0; $i -lt $IndividualDirectoriesNamesCIRCOS_GENOME.Count; $i++) {

$SingleName = $filesPreStatistics_GENOME[$i].basename
$temp_array = $SingleName.split("{_}")
$TargetID = $temp_array[0] 
$CandidateNumber = $temp_array[1]

$PathForCircosInput_GENOME = $PreCircos_GENOME + $TargetID + "_" + $CandidateNumber + "\"

$commandLine = ("::: " + $Circos_bin_PATH + "circos -outputfile " + $TargetID + "_" + $CandidateNumber +
" -outputdir " + $circos_GENOME + " -conf " + $PathForCircosInput_GENOME + "Conf.txt"
)
Add-content $batchCIRCOS_GENOME $commandLine}

Add-Content $batchCIRCOS_GENOME (Get-Content $Parallel_Batch_Template_Portion2_File)
Start-Process ~PATH\circos_GENOME.bat -Wait
Write-Output "Circus plot for GENOME finished"





$circos = $Genome_Plasmid_directory + "14_circos\"
$fso.CreateFolder($circos)

$IndividualDirectoriesNamesCIRCOS = Get-ChildItem  $PreCircos
$batchCIRCOS = $ScriptsDirectory + "circos.bat"


Add-Content $batchCIRCOS (Get-Content $Parallel_Batch_Template_Portion1_File)

for ($i = 0; $i -lt $IndividualDirectoriesNamesCIRCOS.Count; $i++) {

$SingleName = $filesPreStatistics[$i].basename
$temp_array = $SingleName.split("{_}")
$TargetID = $temp_array[0] 
$CandidateNumber = $temp_array[1]

$PathForCircosInput = $PreCircos + $TargetID + "_" + $CandidateNumber + "\"

$commandLine = ("::: " + $Circos_bin_PATH + "circos -outputfile " + $TargetID + "_" + $CandidateNumber +
" -outputdir " + $circos + " -conf " + $PathForCircosInput + "Conf.txt"
)
Add-content $batchCIRCOS $commandLine}

Add-Content $batchCIRCOS (Get-Content $Parallel_Batch_Template_Portion2_File)
Start-Process ~PATH\circos.bat -Wait
Write-Output "Circus plot for GENOME AND PLASMID finished"






$StichingCIRCOS_PLASMID = $Plasmid_directory + "15_Circos_merged_plots\"
$fso.CreateFolder($StichingCIRCOS_PLASMID)
$InputFilesCircosStitching_PLASMID = Get-ChildItem $PreCircos_PLASMID
$batchStitchingCIRCOS_PLASMID = $ScriptsDirectory + "Stitching_circos_PLASMID.bat"
$subDirectoryNameHashSet_PLASMID = @{}



$PlotsAndStitching_PLASMID = $Plasmid_directory + "16_Graphs\"
$fso.CreateFolder($PlotsAndStitching_PLASMID)
$BatchPlots_PLASMID = $ScriptsDirectory + "Ploting_and_Stitching_graps_PLASMID.bat"

$PlotsMerged_PLASMID = $Plasmid_directory + "17_GraphsPerTargetID\"
$fso.CreateFolder($PlotsMerged_PLASMID)


$Histograms_PLASMID = $Plasmid_directory + "18_histograms\"
$fso.CreateFolder($Histograms_PLASMID)
$BatchHistograms_PLASMID = $ScriptsDirectory + "histograms_PLASMID.bat"


$HistogramsMerged_PLASMID = $Plasmid_directory + "18b_histograms_merged\"
$fso.CreateFolder($HistogramsMerged_PLASMID)


$HistogramsTopThree_PLASMID = $Plasmid_directory + "18c_histograms_top_three\"
$fso.CreateFolder($HistogramsTopThree_PLASMID)


for ($i = 0; $i -lt $InputFilesCircosStitching_PLASMID.Count; $i++) {

$SingleName = $InputFilesCircosStitching_PLASMID[$i].basename
$temp_array = $SingleName.split("{_}")
$TargetID = $temp_array[0] 

if(!$subDirectoryNameHashSet_PLASMID.ContainsKey($TargetID)){ $subDirectoryNameHashSet_PLASMID.Add($TargetID, '0') }

}

Add-Content $batchStitchingCIRCOS_PLASMID (Get-Content $Parallel_Batch_Template_Portion1_File)

Add-Content $BatchPlots_PLASMID (Get-Content $Parallel_Batch_Template_Portion1_File)
Add-Content $BatchHistograms_PLASMID (Get-Content $Parallel_Batch_Template_Portion1_File)

foreach ($TargetIDkey in $subDirectoryNameHashSet_PLASMID.Keys) {

$TargetID = $TargetIDkey

$commandLine = ("::: python.exe Images_PLASMID.py -i " + $circos_PLASMID + $TargetID + "_1.png" +
" -j " + $circos_PLASMID + $TargetID + "_2.png" +
" -k " + $circos_PLASMID + $TargetID + "_3.png" +
" -a " + $Pre_statistics_arrangement_PLASMID + $TargetID + "_1"  + "_BLAST_filtered_blastPre_Stat.txt" +
" -b " + $Pre_statistics_arrangement_PLASMID + $TargetID + "_2"  + "_BLAST_filtered_blastPre_Stat.txt" +
" -c " + $Pre_statistics_arrangement_PLASMID + $TargetID + "_3"  + "_BLAST_filtered_blastPre_Stat.txt" +
" -o " + $StichingCIRCOS_PLASMID + $TargetID + ".png" +
" -s " + $TargetID)
Add-Content $batchStitchingCIRCOS_PLASMID $commandLine


$commandLinePlots = ("::: python.exe graphs.py -i " + $PlotsAndStitching_PLASMID + $TargetID + "_1.png" +
" -j " + $PlotsAndStitching_PLASMID + $TargetID + "_2.png" +
" -k " + $PlotsAndStitching_PLASMID + $TargetID + "_3.png" +
" -a " + $Pre_statistics_arrangement_PLASMID + $TargetID + "_1"  + "_BLAST_filtered_blastPre_Stat.txt" +
" -b " + $Pre_statistics_arrangement_PLASMID + $TargetID + "_2"  + "_BLAST_filtered_blastPre_Stat.txt" +
" -c " + $Pre_statistics_arrangement_PLASMID + $TargetID + "_3"  + "_BLAST_filtered_blastPre_Stat.txt" +
" -o " + $PlotsAndStitching_PLASMID + $TargetID + ".png" +
" -p " + $PlotsMerged_PLASMID + $TargetID + ".png" +
" -s " + $TargetID)
Add-Content $BatchPlots_PLASMID $commandLinePlots


$commandLineHistograms = ("::: python.exe histograms.py -i " + $Histograms_PLASMID + $TargetID + "_1.png" +
" -j " + $Histograms_PLASMID + $TargetID + "_2.png" +
" -k " + $Histograms_PLASMID + $TargetID + "_3.png" +
" -a " + $Pre_statistics_arrangement_PLASMID + $TargetID + "_1"  + "_BLAST_filtered_blastPre_Stat.txt" +
" -b " + $Pre_statistics_arrangement_PLASMID + $TargetID + "_2"  + "_BLAST_filtered_blastPre_Stat.txt" +
" -c " + $Pre_statistics_arrangement_PLASMID + $TargetID + "_3"  + "_BLAST_filtered_blastPre_Stat.txt" +
" -o " + $HistogramsTopThree_PLASMID + $TargetID + "_.png" +
" -p " + $HistogramsMerged_PLASMID + $TargetID + ".png" +
" -s " + $TargetID)
Add-content $BatchHistograms_PLASMID $commandLineHistograms


}

Add-Content $batchStitchingCIRCOS_PLASMID (Get-Content $Parallel_Batch_Template_Portion2_File)
Start-Process ~PATH\Stitching_circos_PLASMID.bat -Wait
Write-Output "Circus plot for PLASMID finished"


Add-Content $BatchPlots_PLASMID (Get-Content $Parallel_Batch_Template_Portion2_File)
Start-Process ~PATH\Ploting_and_Stitching_graps_PLASMID.bat -Wait
Write-Output "Plots created and stitched for PLASMID finished"

Add-Content $BatchHistograms_PLASMID (Get-Content $Parallel_Batch_Template_Portion2_File)
Start-Process ~PATH\histograms_PLASMID.bat -Wait
Write-Output "Histograms created and stitched for PLASMID finished"


$StichingCIRCOS_GENOME = $Genome_directory + "15_Circos_merged_plots\"
$fso.CreateFolder($StichingCIRCOS_GENOME)
$InputFilesCircosStitching_GENOME = Get-ChildItem $PreCircos_GENOME
$batchStitchingCIRCOS_GENOME = $ScriptsDirectory + "Stitching_circos_GENOME.bat"
$subDirectoryNameHashSet_Genome = @{}

Add-Content $batchStitchingCIRCOS_GENOME (Get-Content $Parallel_Batch_Template_Portion1_File)


 
$PlotsAndStitching_GENOME = $Genome_directory + "16_Graphs\"
$fso.CreateFolder($PlotsAndStitching_GENOME)
$BatchPlots_GENOME = $ScriptsDirectory + "Ploting_and_Stitching_graps_GENOME.bat"

Add-Content $BatchPlots_GENOME (Get-Content $Parallel_Batch_Template_Portion1_File)


$PlotsMerged_GENOME = $Genome_directory + "17_GraphsPerTargetID\"
$fso.CreateFolder($PlotsMerged_GENOME)

$Histograms_GENOME = $Genome_directory  + "18_histograms\"
$fso.CreateFolder($Histograms_GENOME)
$BatchHistograms_GENOME = $ScriptsDirectory + "histograms_GENOME.bat"

$HistogramsMerged_GENOME = $Genome_directory + "18b_histograms_merged\"
$fso.CreateFolder($HistogramsMerged_GENOME)

$HistogramsTopThree_GENOME = $Genome_directory + "18c_histograms_top_three\"
$fso.CreateFolder($HistogramsTopThree_GENOME)

Add-Content $BatchHistograms_GENOME (Get-Content $Parallel_Batch_Template_Portion1_File)

$BarStatistics = $Genome_directory + "8b_Alignment_counts\"
$fso.CreateFolder($BarStatistics)
$BatchBarStatistics = $ScriptsDirectory + "Statistics_bars.bat"
Add-Content $BatchBarStatistics "echo on`r`n"


$BarPlots = $Genome_directory + "17b_Individual_barplots\"
$fso.CreateFolder($BarPlots)

$BatchBarPlots = $ScriptsDirectory + "bars.bat"

Add-Content $BatchBarPlots (Get-Content $Parallel_Batch_Template_Portion1_File)


$BarPlotsMerged = $Genome_directory + "17c_merged_barplots\"
$fso.CreateFolder($BarPlotsMerged)


for($i = 0; $i -lt $InputFilesCircosStitching_GENOME.Count; $i++) {

$SingleName = $InputFilesCircosStitching_GENOME[$i].basename
$temp_array = $SingleName.split("{_}")
$TargetID = $temp_array[0] 

if(!$subDirectoryNameHashSet_Genome.ContainsKey($TargetID)){ $subDirectoryNameHashSet_Genome.Add($TargetID, '0')}

$CommandLineBarPlotsStatistics = ("bars_statistics.py -i " + $Split_cluster_unclustered + $TargetID + ".csv" +
" -j " + $Pre_statistics_arrangement_GENOME + $SingleName + "_BLAST_filtered_blastPre_Stat.txt" + 
" -k " + $First_filt_directoryPLASMID + $TargetID + "_filtered_blast_results.txt" +
" -l " + $RownWhereDataStartsForClusterUnclusteredFiles + 
" -m " + $SingleName + 
" -o " + $BarStatistics + $SingleName + "_alignment_counts.txt")
Add-Content $BatchBarStatistics $CommandLineBarPlotsStatistics
}


foreach ($TargetIDkey in $subDirectoryNameHashSet_Genome.Keys) {

$TargetID = $TargetIDkey

$commandLine = ("::: python.exe Images_.py -i " + $circos_GENOME + $TargetID + "_1.png" +
" -j " + $circos_GENOME + $TargetID + "_2.png" +
" -k " + $circos_GENOME + $TargetID + "_3.png" +
" -a " + $Pre_statistics_arrangement_GENOME + $TargetID + "_1"  + "_BLAST_filtered_blastPre_Stat.txt" +
" -b " + $Pre_statistics_arrangement_GENOME + $TargetID + "_2"  + "_BLAST_filtered_blastPre_Stat.txt" +
" -c " + $Pre_statistics_arrangement_GENOME + $TargetID + "_3"  + "_BLAST_filtered_blastPre_Stat.txt" +
" -o " + $StichingCIRCOS_GENOME + $TargetID + ".png" +
" -s " + $TargetID)
Add-Content $batchStitchingCIRCOS_GENOME $commandLine


$commandLinePlots = ("::: python.exe graphs.py -i " + $PlotsAndStitching_GENOME + $TargetID + "_1.png" +
" -j " + $PlotsAndStitching_GENOME + $TargetID + "_2.png" +
" -k " + $PlotsAndStitching_GENOME + $TargetID + "_3.png" +
" -a " + $Pre_statistics_arrangement_GENOME + $TargetID + "_1"  + "_BLAST_filtered_blastPre_Stat.txt" +
" -b " + $Pre_statistics_arrangement_GENOME + $TargetID + "_2"  + "_BLAST_filtered_blastPre_Stat.txt" +
" -c " + $Pre_statistics_arrangement_GENOME + $TargetID + "_3"  + "_BLAST_filtered_blastPre_Stat.txt" +
" -o " + $PlotsAndStitching_GENOME + $TargetID + ".png" +
" -p " + $PlotsMerged_GENOME + $TargetID + ".png" +
" -s " + $TargetID)
Add-Content $BatchPlots_GENOME $commandLinePlots


$commandLineHistograms = ("::: python.exe histograms.py -i " + $Histograms_GENOME + $TargetID + "_1.png" +
" -j " + $Histograms_GENOME + $TargetID + "_2.png" +
" -k " + $Histograms_GENOME + $TargetID + "_3.png" +
" -a " + $Pre_statistics_arrangement_GENOME + $TargetID + "_1"  + "_BLAST_filtered_blastPre_Stat.txt" +
" -b " + $Pre_statistics_arrangement_GENOME + $TargetID + "_2"  + "_BLAST_filtered_blastPre_Stat.txt" +
" -c " + $Pre_statistics_arrangement_GENOME + $TargetID + "_3"  + "_BLAST_filtered_blastPre_Stat.txt" +
" -o " + $HistogramsTopThree_GENOME + $TargetID + "_.png" +
" -p " + $HistogramsMerged_GENOME + $TargetID + ".png" +
" -s " + $TargetID)
Add-content $BatchHistograms_GENOME $commandLineHistograms



$CommandLineBarPlots  = ("::: python.exe bars.py -i " + $BarPlots + $TargetID + "_1.png" +
" -j " + $BarPlots + $TargetID + "_2.png" +
" -k " + $BarPlots + $TargetID + "_3.png" +

" -a " + $BarStatistics + $TargetID  + "_1_alignment_counts.txt" + 
" -b " + $BarStatistics + $TargetID  + "_2_alignment_counts.txt" +
" -c " + $BarStatistics + $TargetID  + "_3_alignment_counts.txt" +

" -p " + $BarPlotsMerged + $TargetID + ".png" +
" -s " + $TargetID +

" -d " + $Pre_statistics_arrangement_GENOME + $TargetID + "_1"  + "_BLAST_filtered_blastPre_Stat.txt" +
" -e " + $Pre_statistics_arrangement_GENOME + $TargetID + "_2"  + "_BLAST_filtered_blastPre_Stat.txt" +
" -f " + $Pre_statistics_arrangement_GENOME + $TargetID + "_3"  + "_BLAST_filtered_blastPre_Stat.txt" 

)
Add-Content $BatchBarPlots $CommandLineBarPlots
}

Add-Content $batchStitchingCIRCOS_GENOME (Get-Content $Parallel_Batch_Template_Portion2_File)
Start-Process ~PATH\Stitching_circos_GENOME.bat -Wait
Write-Output "Circus plot for GENOME finished"


Add-Content $BatchPlots_GENOME (Get-Content $Parallel_Batch_Template_Portion2_File)
Start-Process ~PATH\Ploting_and_Stitching_graps_GENOME.bat -Wait
Write-Output "Plots created and stitched for GENOME finished"


Start-Process ~PATH\Statistics_bars.bat -Wait
Write-Output "Statistics for bar Plots for GENOME finished"

Add-Content $BatchBarPlots (Get-Content $Parallel_Batch_Template_Portion2_File)
Start-Process ~PATH\bars.bat -Wait
Write-Output "Individual Bar plots for GENOME finished"


Add-Content $BatchHistograms_GENOME (Get-Content $Parallel_Batch_Template_Portion2_File)
Start-Process ~PATH\histograms_GENOME.bat -Wait
Write-Output "Histograms created and stitched for GENOME finished"





$StichingCIRCOS = $Genome_Plasmid_directory + "15_Circos_merged_plots\"
$fso.CreateFolder($StichingCIRCOS)
$InputFilesCircosStitching = Get-ChildItem $PreCircos
$batchStitchingCIRCOS = $ScriptsDirectory + "Stitching_circos.bat"
$subDirectoryNameHashSet = @{}


 
$PlotsAndStitching = $Genome_Plasmid_directory + "16_Graphs\"
$fso.CreateFolder($PlotsAndStitching)
$BatchPlots = $ScriptsDirectory + "Ploting_and_Stitching_graps.bat"

$PlotsMerged = $Genome_Plasmid_directory + "17_GraphsPerTargetID\"
$fso.CreateFolder($PlotsMerged)



$Histograms = $Genome_Plasmid_directory  + "18_histograms\"
$fso.CreateFolder($Histograms)
$BatchHistograms = $ScriptsDirectory + "histograms.bat"

$HistogramsMerged = $Genome_Plasmid_directory + "18b_histograms_merged\"
$fso.CreateFolder($HistogramsMerged)


$HistogramsTopThree = $Genome_Plasmid_directory + "18c_histograms_top_three\"
$fso.CreateFolder($HistogramsTopThree)

Add-Content $BatchHistograms (Get-Content $Parallel_Batch_Template_Portion1_File)




for ($i = 0; $i -lt $InputFilesCircosStitching.Count; $i++){

$SingleName = $InputFilesCircosStitching[$i].basename
$temp_array = $SingleName.split("{_}")
$TargetID = $temp_array[0]

if(!$subDirectoryNameHashSet.ContainsKey($TargetID)){ $subDirectoryNameHashSet.Add($TargetID, '0') }
 
}

Add-Content $batchStitchingCIRCOS (Get-Content $Parallel_Batch_Template_Portion1_File)

Add-Content $BatchPlots (Get-Content $Parallel_Batch_Template_Portion1_File)

foreach($TargetIDkey in $subDirectoryNameHashSet.Keys){

$TargetID = $TargetIDkey

$commandLine = ("::: python.exe Images_.py -i " + $circos + $TargetID + "_1.png" +
" -j " + $circos + $TargetID + "_2.png" +
" -k " + $circos + $TargetID + "_3.png" +
" -a " + $Pre_statistics_arrangement + $TargetID + "_1"  + "_BLAST_filtered_blastPre_Stat.txt" +
" -b " + $Pre_statistics_arrangement + $TargetID + "_2"  + "_BLAST_filtered_blastPre_Stat.txt" +
" -c " + $Pre_statistics_arrangement + $TargetID + "_3"  + "_BLAST_filtered_blastPre_Stat.txt" +
" -o " + $StichingCIRCOS + $TargetID + ".png" +
" -s " + $TargetID)
Add-Content $batchStitchingCIRCOS $commandLine

$commandLinePlots = ("::: python.exe graphs.py -i " + $PlotsAndStitching + $TargetID + "_1.png" +
" -j " + $PlotsAndStitching + $TargetID + "_2.png" +
" -k " + $PlotsAndStitching + $TargetID + "_3.png" +
" -a " + $Pre_statistics_arrangement + $TargetID + "_1"  + "_BLAST_filtered_blastPre_Stat.txt" +
" -b " + $Pre_statistics_arrangement + $TargetID + "_2"  + "_BLAST_filtered_blastPre_Stat.txt" +
" -c " + $Pre_statistics_arrangement + $TargetID + "_3"  + "_BLAST_filtered_blastPre_Stat.txt" +
" -o " + $PlotsAndStitching + $TargetID + ".png" +
" -p " + $PlotsMerged + $TargetID + ".png" +
" -s " + $TargetID)
Add-Content $BatchPlots $commandLinePlots


$commandLineHistograms = ("::: python.exe histograms.py -i " + $Histograms + $TargetID + "_1.png" +
" -j " + $Histograms + $TargetID + "_2.png" +
" -k " + $Histograms + $TargetID + "_3.png" +
" -a " + $Pre_statistics_arrangement + $TargetID + "_1"  + "_BLAST_filtered_blastPre_Stat.txt" +
" -b " + $Pre_statistics_arrangement + $TargetID + "_2"  + "_BLAST_filtered_blastPre_Stat.txt" +
" -c " + $Pre_statistics_arrangement + $TargetID + "_3"  + "_BLAST_filtered_blastPre_Stat.txt" +
" -o " + $HistogramsTopThree + $TargetID + "_.png" +
" -p " + $HistogramsMerged + $TargetID + ".png" +
" -s " + $TargetID)
Add-content $BatchHistograms $commandLineHistograms

}

Add-Content $batchStitchingCIRCOS (Get-Content $Parallel_Batch_Template_Portion2_File)
Start-Process ~PATH\Stitching_circos.bat -Wait
Write-Output "Circus plot for GENOME AND PLASMID finished"


Add-Content $BatchPlots (Get-Content $Parallel_Batch_Template_Portion2_File)
Start-Process ~PATH\Ploting_and_Stitching_graps.bat -Wait
Write-Output "Plots created and stitched for GENOME AND PLASMID finished"

Add-Content $BatchHistograms (Get-Content $Parallel_Batch_Template_Portion2_File)
Start-Process ~PATH\histograms.bat -Wait
Write-Output "Histograms created and stitched for GENOME and PLASMID finished"




