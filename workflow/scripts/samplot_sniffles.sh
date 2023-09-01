#!/usr/bin/bash

#we save all the violations in a file
awk -F ',' '$6 == "YES" { print }' samplot_sniffles_input_hg002_3_4_complete.csv > input.tsv
# change "," to tabs
sed -i 's/,/\t/g' input.tsv
# parsed archive with the needed information from the vcf merged
archive="input.tsv"
# obtain line by line of the archive
while IFS= read -r line
do

  #save ID in order to use it as png
  ID=$(awk '{print $1}' <<< "$line")
  # save chromosome in a variable
  chrom=$(awk '{print $2}' <<< "$line")
  # save start in a variable
  start=$(awk '{print $3}' <<< "$line")
  # save end in a variable
  end=$(awk '{print $4}' <<< "$line")
  # save the type of the variant of interest
  type=$(awk '{print $5}' <<< "$line")

  let "end=end+1"
  echo ${start}
  echo ${end}
  echo SUPPPdfdsfdsfds

  samplot plot \
      -n HG002_son HG003_father HG004_mother \
      -b HG002.SequelII.merged_15kb_20kb.pbmm2.GRCh38.haplotag.10x.bam \
        HG003.SequelII.merged_15kb_20kb.pbmm2.GRCh38.haplotag.10x.bam \
        HG004.SequelII.merged_15kb_20kb.pbmm2.GRCh38.haplotag.10x.bam \
      -o "sniffles/$ID"_sniffles.png \
      -c "$chrom" \
      -s "$start" \
      -e "$end" \
      -t "$type" \
      --ignore_hp
done < "$archive"

