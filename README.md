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

# SalsaValentina: SVs detection & filtering pipeline to identify putative de novo variants from mendelian inconsistencies. 

## Background

Mendelian inconsistency in SV calls can indicate two possibilities: challenges in SV calling leading to false positive or negative calls across the trio, or a genuine de novo SV. De novo SVs are rare, with an estimated rate of 0.16 de novo SVs per genome in healthy individuals. Despite their rarity, de novo SVs have been associated with human diseases such as [Autism Spectrum Disorder](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8059337/), [Hereditary Pulmonary Alveolar Proteinosis](https://www.nature.com/articles/srep43469) and [Alzheimer's disease](https://www.nature.com/articles/nature20814). In addition, some benchmarking studies have used the rarity of de novo structural variants to support the validity of their SV calls under the assumption than any calls inconsistent with Mendelian inheritance are incorrect ([Zook et al., 2021](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8454654/); [Parikh et at., 2016](https://bmcgenomics.biomedcentral.com/articles/10.1186/s12864-016-2366-2); [Eberth et al.,2021](https://www.science.org/doi/10.1126/science.abf7117)). Here, we aim to investigate putative de novo SVs to either validate them as genuine, which could assist in the diagnosis of rare diseases, or use their properties to inform strategies for more accurate SV calling. 

## Method: Verification of de-novo SVs from trios via visualization and local assembly of complex variants

Candidate de novo SVs can be identified from trios as variants that do not follow Mendelian inheritance patterns. Mendelian inconsistencies are identified when a child has a genotype that is not possible given the genotypes of the parents, for example, when a child is homozygous for an allele that does not exist in either parent. True de novo SVs are expected to be rare; however, in practice, a high rate of inconsistent SVs will be identified, indicating false positives or negatives due to noise inherent in SV calling and merging. SalsaValentina creates a ‘naive’ de novo SV candidate list, develops a QC-framework tool to filter those candidates and enables users to visualize & create a local assembly of every de novo SV locus to aid in confirmation of the variant as either a de novo SV or an incorrect call

SalsaValentina is an integrated pipeline for Mendelian inconsistency of SVs. We demonstrate the pipeline using the Genome in a Bottle (GIAB) Ashkenazim trio ( [HG002 son](https://ftp-trace.ncbi.nlm.nih.gov/ReferenceSamples/giab/data/AshkenazimTrio/HG002_NA24385_son/PacBio_CCS_15kb_20kb_chemistry2/GRCh38), [HG003 father](https://ftp-trace.ncbi.nlm.nih.gov/ReferenceSamples/giab/data/AshkenazimTrio/HG003_NA24149_father/PacBio_CCS_15kb_20kb_chemistry2/GRCh38) & [HG004 mother](https://ftp-trace.ncbi.nlm.nih.gov/ReferenceSamples/giab/data/AshkenazimTrio/HG004_NA24143_mother/PacBio_CCS_15kb_20kb_chemistry2/GRCh38)) sequenced on Sequel II System with 2.0 chemistry and aligned to the GRCh38 genome reference. SVs are called using the [Sniffles2](https://github.com/fritzsedlazeck/Sniffles) variant caller. 


To merge the SV calls into a single VCF, two methods are compared: multi-sample SV calling using Sniffles2 and variant merging with [SURVIVOR](https://github.com/fritzsedlazeck/SURVIVOR) :warning: parameters for survivor? ([Jeffares, D. et al., 2017](https://www.nature.com/articles/ncomms14061)). Each of the resulting merged VCFs is annotated for Mendelian inconsistencies using the [mendelian plugin of BCFtools](https://samtools.github.io/bcftools/howtos/plugin.mendelian.html) ([Heng Li, 2011](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3198575/)). The positions of each SV inconsistent with Mendelian inheritance is extracted from the merged VCFs and [Samplot](https://github.com/ryanlayer/samplot) is used to visualize the region of each variant in each member of the trio ([Belyeu, J.R.,2021](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-021-02380-5)). :warning: Local assembly... 

## Workflow
![Workflow](https://github.com/collaborativebioinformatics/SVHack_Mendelian/blob/main/workflow.jpg)


## Installation

```
git clone https://github.com/collaborativebioinformatics/SVHack_Mendelian.git
```


# Usage
```
cd workflow
snakemake --use-conda
```


## Dependencies

:warning: Version numbers?

* fastqc
* pbmm2
* Sniffles2
* SURVIVOR
* bcftools
* samplot

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

## How to run the pipeline

Edit the input paths in workflow/Snake.config.yaml

### Parameters

* SAMPLES: A list of sample names. These should correspond to the names of the input BAM files. For example: `["HG002", "HG003", "HG004"]`
* REF_GENOME: Path to the reference FASTA file. For example: `reference/genome.fa`

:warning: Example usage

## Results

SalsaValentina compares two different methods of merging SV calls within the trio: multi-sample calling using Sniffles and merging using SURVIVOR. The two methods give different numbers of overall SV calls within the trio as well as percentages of SVs that are inconsistent with Medelian inheritance. We found approximately 19,000 SV calls using Sniffles multi-sample calling, of which 5.2% were Mendelian inconsistent and approximately 32,000 SV calls by SURVIVOR, of which 2.4% are inconsistent (Fig. 1). The different number of total SV calls between the two methods is from differences in genotype assignment for some locations (either missing or reference) between the tools as well as size filtering of SVs of at least 50 bp by SURVIVOR. In addition, SURVIVOR was able to merge additional variant types, such as duplications, inversions, and translocations that were not included in the Sniffles calls. :warning: More explanation needed...

A potential de novo deletion was identified in HG002 at chr7:142,786,222-142,796,849 (:warning: Do I have the coords right? couldn't find the ones in the slack message..) by the Sniffles multi-sample calling method (Fig. 2). The deletion was called as hetrozygous with 12 reads supporting the reference and 13 supporting the variant in HG002, while it was homozygous reference supported by 45 and 44 reads respectively in HG003 and HG004. In addition, GIAB previously reported a de novo deletion in HG002 at chr17:51417826–51417932 as part of their v0.6 SV benchmark set, which was derived from high confidence calls supported by multiple methods (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8454654/). This deletion was not observed in the PacBio dataset using Sniffles to call SVs.  

### Figure 1. Comparison of Mendelian Inconsistencies in Sniffles multi-sample calling and single-sample calling followed by SURVIVOR.
<img src="https://github.com/collaborativebioinformatics/SVHack_Mendelian/blob/main/results/de_novo_literature_igv.png" height=50, width=50>

<img src="https://github.com/collaborativebioinformatics/SVHack_Mendelian/blob/main/sniffles.png?raw=true">

<img src="https://github.com/collaborativebioinformatics/SVHack_Mendelian/blob/main/survivor.png?raw=true">

### Figure 2. Potential de novo Deletion

The top panel shows a deletion in HG002 at chr7:142,757,892-142,824,789, which is absent in the parents (father HG003 middle panel, and mother HG004 bottom panel).

<img src="https://github.com/collaborativebioinformatics/SVHack_Mendelian/blob/jdh/de_novo_chr7.png">

### Figure 3. Potential de nove Deletion at chr7:142786222-142796849 visualized with samplot

<img src="https://github.com/collaborativebioinformatics/SVHack_Mendelian/blob/main/results/de_novo_ours_samplot.png">

### Figure 4. Potential de nove Deletion at chr17:53340465-53340571 visualized with samplot

<img src="https://github.com/collaborativebioinformatics/SVHack_Mendelian/blob/main/results/de_novo_literature_lift_samplot.png">

## Next steps

- Investigate more the reasons for different numbers (Sniffles multi vs SURVIVOR)

### Local Assemblies of SV candidates

# Please cite our work!

:warning: Add citation

## Contributors

* Wolfram Höps (Lead)
* Rajarshi Mondal - rajarshimondal92@gmail.com
* Alison Diaz-Cuevas - alison.m.b.g@gmail.com
* Marlon Arciniega-Sanchez - aldarchez26@gmail.com
* Janet	Doolittle-Hall - janet.doolittle-hall@q2labsolutions.com
* David	Enoma (Data Engineer/ Sys Admin) - david.enoma@ucalgary.ca
* Mauricio Moldes - mauricio.moldes@crg.eu
* Tania	Sepulveda-Morales - sepulvedamortania@gmail.com
