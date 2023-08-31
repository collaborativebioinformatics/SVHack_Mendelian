# SalsaValentina

<img src="https://github.com/collaborativebioinformatics/SVHack_Mendelian/blob/main/salsa.png?raw=true">

## Background
Mendelian disorders, aka monogenic diseases, are undiagnosed by exome sequencing in ~50-75% of cases [https://www.nature.com/articles/ncomms15824]. A sizable portion of mendelian diseases are caused by SVs, (including complex SVs), but the extent of this is unclear [Schuy et al. 2022]. In the absence of reliable databases for phenotypically relevant SVs - like gnomAD or clinvar for SNVs - the interpretation of variants is often challenging. 


## Method: Verification of de-novo SVs from trios (diseased child; healthy parents) via visualization and local assembly of complex variants

In the case of a diseased child of healthy parents, all de-novo SVs are promising candidates for disease association and thus interesting to know. They can, in principle, be found via mendelian inconsistency analysis. 
In practice, this will yield false positives due to noise inherent in SV calling and merging. Using publicly available trio(s), we will create a ‘naive’ de-novo SV candidate list, and work on a QC-framework tool that creates a local assembly of every de-novo SV candidate locus in each member of the trio to review the ‘de-novo’ status. 

## Workflow
![Workflow](https://github.com/collaborativebioinformatics/SVHack_Mendelian/assets/24875399/6bc8a877-4fc5-4fde-8ac4-567f9d2565c3)




## Pipeline

Snakemake 


## Initial Results

Sniffles multisample vs Sniffles singlesample + SURVIVOR

<img src="https://github.com/collaborativebioinformatics/SVHack_Mendelian/blob/main/sniffles.png?raw=true">

<img src="https://github.com/collaborativebioinformatics/SVHack_Mendelian/blob/main/survivor.png?raw=true">

### Potential de-novo Deletion

<img src="https://github.com/collaborativebioinformatics/SVHack_Mendelian/blob/main/de_novo.png?raw=true">


## Next steps

- Investigate more the reasons for different numbers (Sniffles multi vs SURVIVOR)

### Local Assemblies of SV candidates

##Programs and Tools Used
##Team
