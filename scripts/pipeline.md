# SURVIVOR 
We use survivor to merge the SV's vcf files and compare the variants of the trio. The parameters used are the following:
- Max distance between breakpoints: 1000
- Minimum number of supporting caller: 1
- Take the type into account (1==yes, else no): 1
- Take the strands of SVs into account (1==yes, else no): 1
- Estimate distance based on the size of SV (1==yes, else no): 1 -> estaba DIsabled
- Minimum size of SVs to be taken into account: 50

```bash
## Merge the trio vcf files in a variable
ls *vcf > sample_files
# Run survivor
./SURVIVOR merge sample_files 1000 1 1 1 1 50 sample_merged.vcf
```

# VBT-Trio (https://github.com/sbg/VBT-TrioAnalysis/tree/master)

```bash
# Working on ppyd
dx download callsets/GIAB_trio_sniffles/SURVIVOR/HG002.vcf
dx download callsets/GIAB_trio_sniffles/SURVIVOR/HG003.vcf
dx download callsets/GIAB_trio_sniffles/SURVIVOR/HG004.vcf
# using refrence GRCH38
dx download callsets/GIAB_trio_sniffles/Resources/GRCh38_latest_genomic.fna.gz
gunzip GRCh38_latest_genomic.fna.gz
```

```bash
# running VBT
./vbt mendelian -father HG003.vcf -mother HG004.vcf  -child HG002.vcf  -ref GRCh38_latest_genomic.fna -outDir . 
# Path to save the VBT output files
dx pwd callsets/GIAB_trio_sniffles/SURVIVOR/VBT
## saving output documents in DNA Nexus directory 
# Logs of Best Path Algorithm
dx upload /home/dnanexus/VBT-TrioAnalysis/out_BestPathLogs.txt 
# Mendelian decision for Non-Ref child variants only
dx upload /home/dnanexus/VBT-TrioAnalysis/out_ChildReportLog.txt 
# Detailed human-readable logs of trio concordance analysis
dx upload /home/dnanexus/VBT-TrioAnalysis/out_DetailedLogs.txt 
# Tab delimited version of detailed logs
dx upload /home/dnanexus/VBT-TrioAnalysis/out_tab_delim_detailed_log.tsv
# Merged output trio (Mendelian decisions are annotated for each record)
dx upload /home/dnanexus/VBT-TrioAnalysis/out_trio.vcf
```
