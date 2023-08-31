# Usage:
# Input: (1) a multi-sample vcf file to be tested for mendelian consistency
#        (2) trio.ped, specifying the trio
# Output:
#	 (1) output.vcf, the same as (1) but with 'VIOLATION' tag. 


#check if the correct number of arguments is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 input.vcf"
    exit 1
fi

# Input VCF file
input_vcf=$1

# Compressed and Indexed VCF file
compressed_vcf="${input_vcf}.gz"

# PED file
ped_file="trio.ped"

# Violations VCF file
violations_vcf="violations.vcf"
violations_compressed="violations.vcf.gz"
# Output VCF file
output_vcf="output.vcf"

# Compress and index the VCF file
bgzip -c $input_vcf > $compressed_vcf
tabix -p vcf $compressed_vcf

# Run bcftools +mendelian --list
bcftools +mendelian $compressed_vcf -p $ped_file --list x -o $violations_vcf

# compress violoations also
# ...
bgzip -c $violations_vcf > $violations_compressed
tabix -p vcf $violations_compressed


# Annotate the original VCF file
bcftools annotate -a $violations_compressed -c CHROM,POS,ID,REF,ALT -h <\(echo '##INFO=<ID=VIOLATION,Number=0,Type=Flag,Description="Mendelian violation">'\) -m VIOLATION $compressed_vcf > $output_vcf

# Remove temporary files
rm $compressed_vcf $compressed_vcf.tbi $violations_vcf $violations_compressed

echo "Annotated VCF file written to $output_vcf"
