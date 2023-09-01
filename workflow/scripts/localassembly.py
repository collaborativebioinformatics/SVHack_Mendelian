import os
import sys
import pandas as pd

# Verify there is an argument
if len(sys.argv) != 2:
    print("Uso: python script.py <archivo.csv>")
    sys.exit(1)

# Read csv file
csv_file = sys.argv[1]
df = pd.read_csv(csv_file)

# Use the CHROM, START & END values to run the commands
for index, row in df.iterrows():
    CHR, START, END = row['CHROM'], row['START'], row['END']
    
    # Define commands
    commands = [
        f"samtools view -b -h HG002.SequelII.merged_15kb_20kb.pbmm2.GRCh38.haplotag.10x.bam {CHR}:{START}-{END} > HG002_{CHR}_{START}-{END}.bam",
        f"samtools view -b -h HG003.SequelII.merged_15kb_20kb.pbmm2.GRCh38.haplotag.10x.bam {CHR}:{START}-{END} > HG003_{CHR}_{START}-{END}.bam",
        f"samtools view -b -h HG004.SequelII.merged_15kb_20kb.pbmm2.GRCh38.haplotag.10x.bam {CHR}:{START}-{END} > HG004_{CHR}_{START}-{END}.bam",
        f"samtools bam2fq HG002_{CHR}_{START}-{END}.bam > HG002_{CHR}_{START}-{END}.fq",
        f"samtools bam2fq HG003_{CHR}_{START}-{END}.bam > HG003_{CHR}_{START}-{END}.fq",
        f"samtools bam2fq HG004_{CHR}_{START}-{END}.bam > HG004_{CHR}_{START}-{END}.fq",
        f"hifiasm -o HG002_{CHR}_{START}-{END}.asm --primary -t 8 HG002_{CHR}_{START}-{END}.fq",
        f"hifiasm -o HG003_{CHR}_{START}-{END}.asm --primary -t 8 HG003_{CHR}_{START}-{END}.fq",
        f"hifiasm -o HG004_{CHR}_{START}-{END}.asm --primary -t 8 HG004_{CHR}_{START}-{END}.fq",
    ]
    
    # Execution
    for command in commands:
        os.system(command)
