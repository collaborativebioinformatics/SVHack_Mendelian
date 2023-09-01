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
survivor_hg002_3_4 = read_vcf("samples_merged_survivor_sorted_mendelannotate.vcf")

#Create a DataFrame
##create a list with the name of the columns that we want for our dataframe
column_names=['ID', 'CHROM', 'START', 'END', 'REF', 'ALT', 'QUAL', 'FILTER', 'SVTYPE', 'SVLEN', 'COVERAGE', 'CHR_END_TRANSLOCATION', 'FORMAT', 'HG002', 'HG003', 'HG004']
##create the dataframe with the column names
survivor_mics = pd.DataFrame(columns=column_names)

#Get the info for our dataframe
for i in range(len(survivor_hg002_3_4)):
    ##since we only want to keep the ones that are mendelian violations, we will substract the info for this data
    if re.search(r'VIOLATION', survivor_hg002_3_4.INFO[i]):
        ##get all the fields of the column "info" by separating it by ';'
        infoColumn = survivor_hg002_3_4.INFO[i].split(';')
        ##then, create a dictionary in order to access the columns more accurately
        information={}
        ##for each element in the info column, we will save it in the dictionary according to its category
        for k in range(len(infoColumn)):
            ##we want to separate the elements that have a value, so we will look for a "=" in the string
            if re.search(r'=', infoColumn[k]):
                ##getting the category and the value by splitting them by "="
                key, values = infoColumn[k].split('=')
                ##adding the category and value to the dictionary "information"
                information[key]=values
        ##create a row for our dataframe that will include the values we need for our dataframe
        new_row=[survivor_hg002_3_4.ID[i], survivor_hg002_3_4.CHROM[i], survivor_hg002_3_4.POS[i], information.get('END'), survivor_hg002_3_4.REF[i], survivor_hg002_3_4.ALT[i],
        survivor_hg002_3_4.QUAL[i], survivor_hg002_3_4.FILTER[i], information.get('SVTYPE'), information.get('SVLEN')]
        ##since not all SVs have the following information
        if re.search(r'RE=',survivor_hg002_3_4.INFO[i]):
            new_row.append(information.get('RE'))
        else:
             new_row.append('NA')
        if re.search(r'CHR2=',survivor_hg002_3_4.INFO[i]):
            new_row.append(information.get('CHR2'))
        else:
            new_row.append('NA')
        new_row.append(survivor_hg002_3_4.FORMAT[i])
        new_row.append(survivor_hg002_3_4.HG002[i])
        new_row.append(survivor_hg002_3_4.HG003[i])
        new_row.append(survivor_hg002_3_4.HG004[i])
        ##transform the row into a dataframe
        df=pd.DataFrame([new_row], columns=column_names)
        ##concat the 2 dataframes
        survivor_mics=pd.concat([survivor_mics, df])
#Print dataframe to visualize it
print(survivor_mics)
#Save the data frame as a csv
survivor_mics.to_csv('survivor_mics_hg002_3_4.csv', index=False)
