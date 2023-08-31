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


