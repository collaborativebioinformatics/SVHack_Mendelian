# Snakefile

# Define parameters
SAMPLES = ["HG002", "HG003", "HG004"]
REF_GENOME = "reference/genome.fa"

# Rule for Sniffles variant calling
rule sniffles_call:
    input:
        bam="aligned/{sample}.bam"
    output:
        vcf="variants/{sample}.vcf",
        snf="snfs/{sample}.snf"
    conda:
        "environment.yml"
    shell:
        """
        sniffles --input {input.bam} --vcf {output.vcf}
        sniffles --input {input.bam} --snf {output.snf}
        """
        
# Rule for merging variants using Survivor
rule survivor_merge:
    input:
        vcf1="variants/HG002.vcf",
        vcf2="variants/HG003.vcf",
        vcf3="variants/HG004.vcf"
    output:
        vcf="merged/merged_variants.vcf"
    conda:
        "environment.yml"
    shell:
        "survivor merge {input.vcf1} {input.vcf2} {input.vcf3} > {output.vcf}"

# Rule for mendelian inconsistency analysis using BCFtools
rule mendelian_analysis:
    input:
        vcf="merged/merged_variants.vcf"
    output:
        "analysis/mendelian_results.txt"
    conda:
        "environment.yml"
    shell:
        "bcftools +mendelian {input.vcf} > {output}"

# Rule for visualization using Samplot
rule samplot_visualization:
    input:
        vcf="merged/merged_variants.vcf",
        bam_child="aligned/HG002.bam",
        bam_parent1="aligned/HG003.bam",
        bam_parent2="aligned/HG004.bam"
    output:
        "visualization/visualization.pdf"
    conda:
        "environment.yml"
    shell:
        "samplot plot -n 1000 -o {output} {input.vcf} {input.bam_child} {input.bam_parent1} {input.bam_parent2}"

# Default rule to run all steps
rule all:
    input:
        "visualization/visualization.pdf"
