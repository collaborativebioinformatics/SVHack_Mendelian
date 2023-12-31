#!/bin/bash

#we save all the violations in a file
awk -F ',' '$6 == "YES" { print }' samplot_survivor_input_hg002_3_4.csv> input.tsv
# change "," to tabs
sed -i 's/,/\t/g' input.tsv
# parsed archive with the needed information from the vcf merged
archive=input.tsv
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

  
  samplot plot \
      -n HG002 HG002 HG002 \
      -b HG002.SequelII.merged_15kb_20kb.pbmm2.GRCh38.haplotag.10x.bam \
        HG003.SequelII.merged_15kb_20kb.pbmm2.GRCh38.haplotag.10x.bam \
        HG004.SequelII.merged_15kb_20kb.pbmm2.GRCh38.haplotag.10x.bam \
      -o "$ID"_survivor.png \
      -c "$chrom" \
      -s "$start" \
      -e "$end" \
      -t "$type"
done < <("$archive")
