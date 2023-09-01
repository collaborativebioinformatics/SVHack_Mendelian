import pandas as pd #importing package that will help us to read the csv file, create dataframes, exporting the vcf file, etc.
import re # importing package tha will help us to search for regular expressions
import io #importing package to create a dataframe from a vcf file
import os #importing package to create a dataframe from a vcf file

#Function to create a dataframe from a vcf file
def read_vcf(path):
    with open(path, 'r') as f:
        lines = [l for l in f if not l.startswith('##')]
    return pd.read_csv(
        io.StringIO(''.join(lines)),
        dtype={'#CHROM': str, 'POS': int, 'ID': str, 'REF': str, 'ALT': str,
               'QUAL': str, 'FILTER': str, 'INFO': str, 'FORMAT':str, 'HG002':str, 'HG003':str, 'HG004':str},
        sep='\t'
    ).rename(columns={'#CHROM': 'CHROM'})

#Creating a dataframe from clinvar dataset
sniffles_hg002_3_4 = read_vcf("sniffles_HG002-3-4_multisample_mendelannotate.vcf")

#Create a DataFrame
##create a list with the name of the columns that we want for our dataframe
column_names=['ID', 'CHROM', 'START', 'END', 'REF', 'ALT', 'QUAL', 'FILTER', 'SVTYPE', 'SVLEN', 'COVERAGE', 'CONSENSUS_SUPPORT', 'MEAN_MISMATCH_LEN', 'BREAKPOINTS', 'AF', 'FORMAT', 'HG002', 'HG003', 'HG004']
##create the dataframe with the column names
sniffles_mics = pd.DataFrame(columns=column_names)

#Get the info for our dataframe
for i in range(len(sniffles_hg002_3_4)):
    ##since we only want to keep the ones that are mendelian violations, we will substract the info for this data
    if re.search(r'VIOLATION', sniffles_hg002_3_4.INFO[i]):
        ##get all the fields of the column "info" by separating it by ';'
        infoColumn = sniffles_hg002_3_4.INFO[i].split(';')
        ##then, create a dictionary in order to access the columns more accurately
        information={}
        #for each element in the info column, we will save it in the dictionary according to its category
        for k in range(len(infoColumn)):
            #we want to separate the elements that have a value, so we will look for a "=" in the string
            if re.search(r'=', infoColumn[k]):
                #getting the category and the value by splitting them by "="
                key, values = infoColumn[k].split('=')
                #adding the category and value to the dictionary "information"
                information[key]=values
        #create a row for our dataframe that will include the values we need for our dataframe
        new_row=[sniffles_hg002_3_4.ID[i], sniffles_hg002_3_4.CHROM[i], sniffles_hg002_3_4.POS[i], information.get('END'), sniffles_hg002_3_4.REF[i], sniffles_hg002_3_4.ALT[i],
        sniffles_hg002_3_4.QUAL[i], sniffles_hg002_3_4.FILTER[i], information.get('SVTYPE'), information.get('SVLEN'), information.get('COVERAGE'), information.get('CONSENSUS_SUPPORT'),
        information.get('NM'), infoColumn[0], information.get('AF'), sniffles_hg002_3_4.FORMAT[i], sniffles_hg002_3_4.HG002[i], sniffles_hg002_3_4.HG003[i], sniffles_hg002_3_4.HG004[i]]

        #transform the row into a dataframe
        df=pd.DataFrame([new_row], columns=column_names)
        #concat the 2 dataframes
        sniffles_mics=pd.concat([sniffles_mics, df])
#print dataframe to visualize it
print(sniffles_mics)
#save the data frame as a csv
sniffles_mics.to_csv('sniffles_mics_hg002_3_4.csv', index=False)
