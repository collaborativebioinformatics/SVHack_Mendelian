# ~~~ SalsaValentina ~~~

<img src="https://github.com/collaborativebioinformatics/SVHack_Mendelian/blob/main/salsa5.png?raw=true">


## Background

Mendelian inconsistency in SV calls can indicate two possibilities: challenges in SV calling leading to false positive or negative calls across the trio, or a genuine de novo SV. De novo SVs are rare, with an estimated rate of 0.16 de novo SVs per genome in healthy individuals. Despite their rarity, de novo SVs have been associated with human disease, including autism spectrum disorder, which has approximately 0.206 de novo structural variant events in this population [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8059337/]. In addition, benchmarking studies have used the rarity of de novo strucutral variants to support the validity of their SV calls under the assumption than any calls inconsistent with Mendelian inhertiance are incorrect [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8454654/, https://bmcgenomics.biomedcentral.com/articles/10.1186/s12864-016-2366-2, https://www.science.org/doi/10.1126/science.abf7117]. Here, we aim to investigate putative de novo SVs to either validate them as genuine, which could assist in diagnosis of rare disease, or use their properties to inform strategies for more accurate SV calling. 

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
