[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=21&pause=1000&color=F76B1E&width=435&lines=Welcome+To+Our+Github+Page;We+are+Team+Salsa+Valentina)](https://git.io/typing-svg)

```
   _____       _            __      __   _            _   _              
  / ____|     | |           \ \    / /  | |          | | (_)             
 | (___   __ _| |___  __ _   \ \  / /_ _| | ___ _ __ | |_ _ _ __   __ _  
  \___ \ / _` | / __|/ _` |   \ \/ / _` | |/ _ \ '_ \| __| | '_ \ / _` | 
  ____) | (_| | \__ \ (_| |    \  / (_| | |  __/ | | | |_| | | | | (_| | 
 |_____/ \__,_|_|___/\__,_|     \/ \__,_|_|\___|_| |_|\__|_|_| |_|\__,_|

                                                                         
```                                                                         

<img src="https://github.com/collaborativebioinformatics/SVHack_Mendelian/blob/main/WhatsApp Image 2023-08-31 at 20.02.13.jpeg?raw=true">

# SV detection & filtering pipeline to identify putative de novo variants from mendelian inconsistencies. 

## Table of Contents
1. [How to use it](#how-to-use-it)
2. [Installation](#installation)
3. [Dependendencies](#dependencies)
4. [Usage](#usage)
5. [Input](#input)
6. [Output](#output)
7. [Workflow Diagram](#workflow)
8. [Background](#background)
9. [Results](#results)
10. [Citation](#Please-cite-our-work!)
11. [Contributors](#contributors)

## Background

Candidate de novo SVs can be identified from trios as variants that do not follow Mendelian inheritance patterns. Mendelian inconsistencies are identified when a child has a genotype that is not possible given the genotypes of the parents, for example, when a child is homozygous for an allele that does not exist in either parent. Mendelian inconsistency in SV calls can indicate two possibilities: challenges in SV calling leading to false positive or negative calls across the trio, or a genuine de novo SV. De novo SVs are rare, with an estimated rate of 0.16 de novo SVs per genome in healthy individuals. Despite their rarity, de novo SVs have been associated with human diseases such as [Autism Spectrum Disorder](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8059337/), [Hereditary Pulmonary Alveolar Proteinosis](https://www.nature.com/articles/srep43469) and [Alzheimer's disease](https://www.nature.com/articles/nature20814). In addition, some benchmarking studies have used the rarity of de novo structural variants to support the validity of their SV calls under the assumption than any calls inconsistent with Mendelian inheritance are incorrect ([Zook et al., 2021](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8454654/); [Parikh et at., 2016](https://bmcgenomics.biomedcentral.com/articles/10.1186/s12864-016-2366-2); [Eberth et al.,2021](https://www.science.org/doi/10.1126/science.abf7117)). Here, we aim to investigate putative de novo SVs to either validate them as genuine, which could assist in the diagnosis of rare diseases, or use their properties to inform strategies for more accurate SV calling. 

## Method: Verification of de-novo SVs from trios via visualization and local assembly of complex variants

True de novo SVs are expected to be rare; however, in practice, a high rate of inconsistent SVs will be identified, indicating false positives or negatives due to noise inherent in SV calling and merging. SalsaValentina creates a ‘naive’ de novo SV candidate list, develops a QC-framework tool to filter those candidates and enables users to visualize & create a local assembly of every de novo SV locus to aid in confirmation of the variant as either a de novo SV or an incorrect call.

SalsaValentina is an integrated pipeline for Mendelian inconsistency of SVs. We demonstrate the pipeline using the Genome in a Bottle (GIAB) Ashkenazim trio ( [HG002 son](https://ftp-trace.ncbi.nlm.nih.gov/ReferenceSamples/giab/data/AshkenazimTrio/HG002_NA24385_son/PacBio_CCS_15kb_20kb_chemistry2/GRCh38), [HG003 father](https://ftp-trace.ncbi.nlm.nih.gov/ReferenceSamples/giab/data/AshkenazimTrio/HG003_NA24149_father/PacBio_CCS_15kb_20kb_chemistry2/GRCh38) & [HG004 mother](https://ftp-trace.ncbi.nlm.nih.gov/ReferenceSamples/giab/data/AshkenazimTrio/HG004_NA24143_mother/PacBio_CCS_15kb_20kb_chemistry2/GRCh38)) sequenced on Sequel II System with 2.0 chemistry and aligned to the GRCh38 genome reference. SVs are called using the [Sniffles2](https://github.com/fritzsedlazeck/Sniffles) variant caller. 


To merge the SV calls into a single VCF, two methods are compared: multi-sample SV calling using Sniffles2 and variant merging with [SURVIVOR](https://github.com/fritzsedlazeck/SURVIVOR) using default parameters ([Jeffares, D. et al., 2017](https://www.nature.com/articles/ncomms14061)). Each of the resulting merged VCFs is annotated for Mendelian inconsistencies using the [mendelian plugin of BCFtools](https://samtools.github.io/bcftools/howtos/plugin.mendelian.html) ([Heng Li, 2011](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3198575/)). The positions of each SV inconsistent with Mendelian inheritance is extracted from the merged VCFs and [Samplot](https://github.com/ryanlayer/samplot) is used to visualize the region of each variant in each member of the trio ([Belyeu, J.R.,2021](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-021-02380-5)).

To further investigate the validity of the candidate variants, local assembly was performed by extracting reads aligned 50 kb upstream and downstream of the region of interest and assembling with [Hifiasm](https://github.com/chhylp123/hifiasm) (--primary to generate primary and alternate assembly) ([Cheng, H. et al., 2021](https://doi.org/10.1038/s41592-020-01056-5)). The [YASS](https://bioinfo.univ-lille.fr/yass/) Genomic Similarity Search Tool webserver was used to create dotplots visualizing pairwise alignments of the resulting contigs to GRCh37 to verify the deletion in HG002 ([Noe, L. and Kucherov, G., 2005](https://doi.org/10.1093/nar/gki478)).

## How to use it

## Installation

```
git clone https://github.com/collaborativebioinformatics/SVHack_Mendelian.git
```

## Dependencies

* Sniffles2 Version 2.0.7
* SURVIVOR Version 1.0.7
* bcftools Version 1.17
* samplot Version 1.3.0
* Hifiasm Version 0.19.6

## Usage

Edit the input paths in workflow/Snake.config.yaml
* SAMPLES: A list of sample names. These should correspond to the names of the input BAM files. For example: `["HG002", "HG003", "HG004"]`
* REF_GENOME: Path to the reference FASTA file. For example: `reference/genome.fa`

```
cd workflow
snakemake --use-conda
```

## Input Files

```
/working_dir/workflow
|-- input_data/reference  # Reference genome
|   |-- genome.fa
|-- aligned  # BAM file for each sample
|   |-- HG002.bam
|   |-- HG003.bam
|   |-- HG004.bam
```

## Output Files

```
/working_dir/workflow/
|-- variants  # Variant calls from Sniffles
|   |-- HG002.vcf
|   |-- HG003.vcf
|   |-- HG004.vcf
|-- snfs  # SNF files from Sniffles
|   |-- HG002.snf
|   |-- HG003.snf
|   |-- HG004.snf
|-- merged  # SV calls merged by SURVIVOR
|   |-- merged_variants.vcf
|-- analysis  # Mendelian inconsistencies
|   |-- mendelian_results.txt
|-- visualization  # Visualizations from samplot
|   |-- visualization.pdf
```

## Workflow
![Workflow](https://github.com/collaborativebioinformatics/SVHack_Mendelian/blob/main/workflow2.jpg)


## Results

SalsaValentina compares two different methods of merging SV calls within the trio: multi-sample calling using Sniffles and merging using SURVIVOR. The two methods give different numbers of overall SV calls within the trio as well as percentages of SVs that are inconsistent with Medelian inheritance. We found a total of approximately 32,000 SV calls in our merged call set using either Sniffles multi-sample calling or SURVIVOR. For Sniffles multi-sample calling, 5.2% of these were Mendelian inconsistent while for SURVIVOR 2.4% were inconsistent (Fig. 1). The different number of inconsistent SV calls between the two methods is due to differences in genotype assignment between the tools, with SURVIVOR treating some variants as missing while Sniffles reports them as reference.

A mendelian inconsistent deletion was identified in HG002 at chr7:142,786,222-142,796,849 by the Sniffles multi-sample calling method (Fig. 2). This is in the T cell receptor beta locus and thus likely the result of somatic recombination rather than a de novo germline variant. However, it can still be used to demonstrate the method. This deletion was called heterozygous with 12 reads supporting the reference and 13 supporting the variant in HG002, while it was homozygous reference supported by 45 and 44 reads respectively in HG003 and HG004. In addition, GIAB previously reported a de novo deletion in HG002 at chr17:51417826–51417932 using GRCH37 reference as part of their v0.6 SV benchmark set, which was derived from high confidence calls supported by multiple methods ([Zook et al., 2020](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8454654/)). This deletion was also identified in this study, at chr17:53,340,465-53,340,571 when using GRCH38 as reference (Fig. 3). This heterozygous deletion was supported by 30 reads and the reference at this location by 27 reads, while the parents had only reads supporting the reference allele (65 in HG003 and 72 in HG004).

### Figure 1. Comparison of Mendelian Inconsistencies in Sniffles multi-sample calling and single-sample calling followed by SURVIVOR.

<img src="https://github.com/collaborativebioinformatics/SVHack_Mendelian/blob/main/results/ratio_violation_sniffles.png?raw=true">

<img src="https://github.com/collaborativebioinformatics/SVHack_Mendelian/blob/main/results/ratio_violation_survivor.png?raw=true">

Discrepancy: integrated calling (Sniffles) reports 0/0 for reference alleles, Survivor reports ./. 
For now: Continue with Sniffles file.

### Figure 2. Literature-known de novo Deletion at chr17:53340465-53340571 visualized with samplot

<img src="https://github.com/collaborativebioinformatics/SVHack_Mendelian/blob/main/results/de_novo_literature_lift_samplot.png">


### Figure 3. Potential de novo Deletion at chr7:142786222-142796849 visualized with samplot

<img src="https://github.com/collaborativebioinformatics/SVHack_Mendelian/blob/main/results/de_novo_ours_samplot.png">


### Figure 4 

Pairwise alignment of hg38 reference (y-axis) vs assembled contig (x-axis) using YASS.  

![image](https://github.com/collaborativebioinformatics/SVHack_Mendelian/assets/24875399/3190f44d-6f88-44fc-84f8-a4e0433cad7e)

### Figure 5 

Pairwise alignment of hg38 reference (y-axis) vs assembled contig (x-axis) as output of our pipeline using pafr.
![c0b211c1-1c1b-483b-b6b1-3b7d89f8d58c](https://github.com/collaborativebioinformatics/SVHack_Mendelian/assets/24875399/4b5692bc-a785-4e43-b20b-b5a08bae1d66)


# Future work

### - Fully automate the evaluation of SV-containing contigs
### - Test assembly in the most complex genomic regions


## Contributors

* Wolfram Höps - wolfram.hoeps@gmail.com
* Rajarshi Mondal - rajarshimondal92@gmail.com
* Alison Diaz-Cuevas - alison.m.b.g@gmail.com
* Marlon Arciniega-Sanchez - aldarchez26@gmail.com
* Janet	Doolittle-Hall - janet.doolittle-hall@q2labsolutions.com
* David	Enoma (Data Engineer/ Sys Admin) - david.enoma@ucalgary.ca
* Mauricio Moldes - mauricio.moldes@crg.eu
* Tania	Sepulveda-Morales - sepulvedamortania@gmail.com
