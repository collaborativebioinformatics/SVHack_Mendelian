#!/bin/bash
# parsed archive with the needed information from the vcf merged
archive=samples_merged_survivor_sorted_mendelannotate.vcf
# obtain line by line of the archive, ommiting the first row (columns names)
tail -n +2 "$archive" | while IFS= read -r line
  do
  # save chromosome in a variable
  chrom=$(awk '{print $2}' <<< "$line")
  # save start in a variable
  start=$(awk '{print $3}' <<< "$line")
  # save end in a variable
  end=$(awk '{print $4}' <<< "$line")
  # save the type of the variant of interest
  type=$(awk '{print $5}' <<< "$line")

  
  time samplot plot \
      -n <name bam file> <name bam file> <name bam file> \
      -b <path of bam file>/.bam \
        <path of bam file>/.bam \
        <path of bam file>/.bam \
      -o 4_115928726_115931880.png \
      -c "$chrom" \
      -s "$start" \
      -e "$end" \
      -t "$type"
  done < <(tail -n +2 "$archive")