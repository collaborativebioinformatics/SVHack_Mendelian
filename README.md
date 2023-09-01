
<img src="https://github.com/collaborativebioinformatics/SVHack_Mendelian/blob/main/WhatsApp Image 2023-08-31 at 20.02.13.jpeg?raw=true">

# SalsaValentina: SVs detection & filtering pipeline to capture promising candidates responsible of de novo diseases

## Background

Mendelian inconsistency in SV calls can indicate two possibilities: challenges in SV calling leading to false positive or negative calls across the trio, or a genuine de novo SV. De novo SVs are rare, with an estimated rate of 0.16 de novo SVs per genome in healthy individuals. Despite their rarity, de novo SVs have been associated with human disease, including autism spectrum disorder, which has approximately 0.206 de novo structural variant events in this population [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8059337/]. In addition, benchmarking studies have used the rarity of de novo structural variants to support the validity of their SV calls under the assumption than any calls inconsistent with Mendelian inheritance are incorrect [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8454654/, https://bmcgenomics.biomedcentral.com/articles/10.1186/s12864-016-2366-2, https://www.science.org/doi/10.1126/science.abf7117]. Here, we aim to investigate putative de novo SVs to either validate them as genuine, which could assist in diagnosis of rare disease, or use their properties to inform strategies for more accurate SV calling. 

## Method: Verification of de-novo SVs from trios (diseased child; healthy parents) via visualization and local assembly of complex variants

Candidate de novo SVs can be identified from trios as variants that do not follow Mendelian inheritance patterns. :warning: Explain this more. True de novo SVs are expected to be rare; however, in practice, a high rate of inconsistent SVs will be identified, indicating false positives or negatives due to noise inherent in SV calling and merging. Using a publicly available trio :warning: Citation, we created a ‘naive’ de novo SV candidate list, and developed a QC-framework tool that enables users to visualize the alignments in inconsistent SV regions across the trio and create a local assembly of every de novo SV candidate locus to aid in confirmation of the variant as either a de novo SV or an incorrect call. 

## Workflow
![Workflow](https://github.com/collaborativebioinformatics/SVHack_Mendelian/assets/24875399/c9bc8b5e-2d19-438e-9c39-f899e468b034)



# Usage

## Installation

`git clone https://github.com/collaborativebioinformatics/SVHack_Mendelian.git`

## Dependencies

:warning: Version numbers?

* Sniffles2
* SURVIVOR
* bcftools
* samplot

## Input Files

```
/working_dir
|-- reference  # Reference genome
|   |-- genome.fa
|-- aligned  # BAM file for each sample
|   |-- HG002.bam
|   |-- HG003.bam
|   |-- HG004.bam
```

## Output Files

```
/working_dir
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

### Parameters

* SAMPLES: A list of sample names. These should correspond to the names of the input BAM files. For example: `["HG002", "HG003", "HG004"]`
* REF_GENOME: Path to the reference FASTA file. For example: `reference/genome.fa`

:warning: Example usage


## Initial Results

Sniffles multisample vs Sniffles singlesample + SURVIVOR

<img src="https://github.com/collaborativebioinformatics/SVHack_Mendelian/blob/main/sniffles.png?raw=true">

<img src="https://github.com/collaborativebioinformatics/SVHack_Mendelian/blob/main/survivor.png?raw=true">

### Potential de-novo Deletion

<img src="https://github.com/collaborativebioinformatics/SVHack_Mendelian/blob/main/de_novo.png?raw=true">


## Next steps

- Investigate more the reasons for different numbers (Sniffles multi vs SURVIVOR)

### Local Assemblies of SV candidates

# Please cite our work!

:warning: Add citation

## Contributors

* Wolfram Höps (Lead)
* Rajarshi Mondal - rajarshimondal92@gmail.com
* Alison Diaz-Cuevas - alison.m.b.g@gmail.com
* Marlon Aldair	Arciniega Sanchez
* Janet	Doolittle-Hall - janet.doolittle-hall@q2labsolutions.com
* David	Enoma (Data Engineer/ Sys Admin) - david.enoma@ucalgary.ca
* Mauricio Moldes - mauricio.moldes@crg.eu
* Tania	Sepulveda-Morales - sepulvedamortania@gmail.com
