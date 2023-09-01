import pandas as pd #importing package that will help us to read the csv file, create dataframes, exporting the vcf file, etc.
pd.options.mode.chained_assignment = None  # default='warn'

#Upload files with the SVs that have Mendelian inconsistency
sniffles_mics=pd.read_csv('sniffles_mics_hg002_3_4.csv')

#Create a DataFrame
##create a list with the name of the columns that we want for our dataframe
column_names=['ID', 'CHROM', 'START', 'END', 'REF', 'ALT', 'QUAL', 'FILTER', 'SVTYPE', 'SVLEN', 'COVERAGE', 'CONSENSUS_SUPPORT', 'MEAN_MISMATCH_LEN', 'BREAKPOINTS', 'AF', 'FORMAT', 'HG002', 'HG003', 'HG004']
##create the dataframe with the column names
sniffles_denovo_candidates = pd.DataFrame(columns=column_names)

#Filtering to identify high-quality de novo candidates
for i in range(len(sniffles_mics)):
    #Filtering by genotype
    genotype_Prob=sniffles_mics.HG002[i].split(':')[0]
    genotype_Fath=sniffles_mics.HG003[i].split(':')[0]
    genotype_Moth=sniffles_mics.HG004[i].split(':')[0]
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
        denovo_i=list(sniffles_mics.iloc[i])
        ##transform the row into a dataframe
        df=pd.DataFrame([denovo_i], columns=column_names)
        ##concat the 2 dataframes
        sniffles_denovo_candidates=pd.concat([sniffles_denovo_candidates, df])

##we will reset the index of the DataFrame
sniffles_denovo_candidates=sniffles_denovo_candidates.reset_index()

#Sort out the dataframe according to the coverage of the SVs
##First, sniffles coverage has 5 values indicating coverages near upstream, start, center, end, downstream of structural variation
##for that reason, we planned on doing a mean of the coverages and rank it by it

##we create columns that will indicate the coverage mean
sniffles_denovo_candidates.insert(loc=2, column='COVERAGE_MEAN', value=['No']*len(sniffles_denovo_candidates))
##get the mean coverage for each de novo SVs
for j in range(len(sniffles_denovo_candidates)):
    coverages_j=sniffles_denovo_candidates.COVERAGE[j].split(',')
    coverage_sum=0
    count=0 #will let us know how many coverages the SV has
    for k in range(len(coverages_j)):
        if coverages_j[k]!='.':
            coverage_sum=coverage_sum+int(coverages_j[k])
            count=count+1
    sniffles_denovo_candidates['COVERAGE_MEAN'][j]=coverage_sum/count

##sort the dataframe by coverage
sniffles_denovo_candidates=sniffles_denovo_candidates.sort_values(by=['COVERAGE_MEAN'], ascending=False)

#Filter by chromosome
##we get rid to the chrUn
chr_weird=sniffles_denovo_candidates['CHROM'].str.contains('Un_')
random=sniffles_denovo_candidates['CHROM'].str.contains('_random')
sniffles_denovo_candidates = sniffles_denovo_candidates[~chr_weird]
sniffles_denovo_candidates = sniffles_denovo_candidates[~random]

#delete the BND type variants
sniffles_denovo_candidates=sniffles_denovo_candidates[sniffles_denovo_candidates.SVTYPE!='BND']

##rename the index to "Ranking"
sniffles_denovo_candidates=sniffles_denovo_candidates.reset_index()
sniffles_denovo_candidates=sniffles_denovo_candidates.rename_axis('RANKING')
##remove index created for a reason haha
sniffles_denovo_candidates=sniffles_denovo_candidates.drop(['level_0', 'index'], axis=1)

#Save the data frame as a csv
sniffles_denovo_candidates.to_csv('sniffles_denovo_candidates.csv')
