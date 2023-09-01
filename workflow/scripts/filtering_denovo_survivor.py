import pandas as pd #importing package that will help us to read the csv file, create dataframes, exporting the vcf file, etc.
pd.options.mode.chained_assignment = None  # default='warn'

#Upload files with the SVs that have Mendelian inconsistency
survivor_mics=pd.read_csv('survivor_mics_hg002_3_4.csv')

#Create a DataFrame
##create a list with the name of the columns that we want for our dataframe
column_names=['ID', 'CHROM', 'START', 'END', 'REF', 'ALT', 'QUAL', 'FILTER', 'SVTYPE', 'SVLEN', 'COVERAGE', 'CHR_END_TRANSLOCATION', 'FORMAT', 'HG002', 'HG003', 'HG004']
##create the dataframe with the column names
survivor_denovo_candidates = pd.DataFrame(columns=column_names)

#Filtering to identify high-quality de novo candidates
for i in range(len(survivor_mics)):
    #Filtering by genotype
    genotype_Prob=survivor_mics.HG002[i].split(':')[0]
    genotype_Fath=survivor_mics.HG003[i].split(':')[0]
    genotype_Moth=survivor_mics.HG004[i].split(':')[0]
    ##flag to indicate if the genotype is correct
    flag=0
    ##cases where we have a heterozygous genotype for t.to_string()he proband while having a homozygous reference genotype for both parents
    if genotype_Prob=='0/1' and ((genotype_Fath=='0/0' and genotype_Moth=='0/0') or (genotype_Fath=='./.' and genotype_Moth=='./.')):
        flag=1
    ##cases where we have a homozygous alternate genotype for proband and heterozygous or homozygous reference genotype for parents
    if genotype_Prob=='1/1' and ((genotype_Fath=='0/1' and genotype_Moth=='0/0') or (genotype_Fath=='0/0' and genotype_Moth=='0/1') or (genotype_Fath=='0/1' and genotype_Moth=='./.') or (genotype_Fath=='./.' and genotype_Moth=='0/1') or (genotype_Fath=='./.' and genotype_Moth=='0/0') or (genotype_Fath=='0/0' and genotype_Moth=='./.') or (genotype_Fath=='0/0' and genotype_Moth=='0/0') or (genotype_Fath=='./.' and genotype_Moth=='./.')):
        flag=1

    if flag==1:
        #Get the row of the SV
        denovo_i=list(survivor_mics.iloc[i])
        ##transform the row into a dataframe
        df=pd.DataFrame([denovo_i], columns=column_names)
        ##concat the 2 dataframes
        survivor_denovo_candidates=pd.concat([survivor_denovo_candidates, df])

#Exclude BND aka translocations
bnd=survivor_denovo_candidates['ID'].str.contains('BND')
survivor_denovo_candidates=survivor_denovo_candidates[~bnd]

##we will reset the index of the DataFrame
survivor_denovo_candidates=survivor_denovo_candidates.reset_index()

#Filtrate by Proband ratio
##we create columns that will indicate the ratio
survivor_denovo_candidates.insert(loc=2, column='RATIO', value=['']*len(survivor_denovo_candidates))
##get the mean coverage for each de novo SVs
for j in range(len(survivor_denovo_candidates)):
    format_j=survivor_denovo_candidates.HG002[j].split(':')
    reads_j=format_j[3].split(',')
    reference=int(reads_j[0])
    variant=int(reads_j[1])
    ratio=variant/(reference+variant)
    survivor_denovo_candidates['RATIO'][j]=ratio

#Filtrar by ratio min 0.3 max 0.7
survivor_denovo_candidates=survivor_denovo_candidates[survivor_denovo_candidates.RATIO>=0.3]
survivor_denovo_candidates=survivor_denovo_candidates[survivor_denovo_candidates.RATIO<=0.7]

#Save the data frame as a csv
survivor_denovo_candidates.to_csv('survivor_denovo_candidates.csv', index=False)
