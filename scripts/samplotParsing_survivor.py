import pandas as pd #importing package that will help us to read the csv file, create dataframes, exporting the vcf file, etc.
import re # importing package tha will help us to search for regular expressions
import io #importing package to create a dataframe from a vcf file
import os #importing package to create a dataframe from a vcf file

#function to create a dataframe from a vcf file
def read_vcf(path):
    with open(path, 'r') as f:
        lines = [l for l in f if not l.startswith('##')]
    return pd.read_csv(
        io.StringIO(''.join(lines)),
        dtype={'#CHROM': str, 'POS': int, 'ID': str, 'REF': str, 'ALT': str,
               'QUAL': str, 'FILTER': str, 'INFO': str, 'FORMAT':str, 'HG002':str, 'HG003':str, 'HG004':str},
        sep='\t'
    ).rename(columns={'#CHROM': 'CHROM'})

#creating a dataframe from clinvar dataset
survivor_hg002_3_4 = read_vcf("samples_merged_survivor_sorted_mendelannotate.vcf")

#create a DataFrame
samplot_survivor_input_hg002_3_4 = pd.DataFrame(columns=['ID', 'CHROM', 'START', 'END', 'TYPE', 'MENDELIAN_VIOLATION'])

for i in range(len(survivor_hg002_3_4)):
    #get all the fields of the column "info" by separating it by ';'
    infoColumn = survivor_hg002_3_4.INFO[i].split(';')
    infoColumn = infoColumn[1:]
    #then, create a dictionary in order to access the columns more accurately
    information={}
    #for each element in the info column, we will save it in the dictionary according to its category
    for k in range(len(infoColumn)):
        #we want to separate the elements that have a value, so we will look for a "=" in the string
        if re.search(r'=', infoColumn[k]):
            #getting the category and the value by splitting them by "="
            key, values = infoColumn[k].split('=')
            #adding the category and value to the dictionary "information"
            information[key]=values

    #create a row for our dataframe that will include the values we need aka id, chromosome, start, end, type and mendelian violation classification
    new_row=[]
    #add the ID for the variant in order to keep track of which variant we are seeing
    new_row.append(survivor_hg002_3_4.ID[i])
    #add the chromosome
    new_row.append(survivor_hg002_3_4.CHROM[i])
    #add the START position
    new_row.append(survivor_hg002_3_4.POS[i])
    #add the END position
    new_row.append(information.get('END'))
    #add the variant type
    new_row.append(information.get('SVTYPE'))
    #we want to know if they are mendelian violations
    if re.search(r'VIOLATION', survivor_hg002_3_4.INFO[i]):
        new_row.append('YES')
    else:
        new_row.append('NO')
    #transform the row into a dataframe
    df=pd.DataFrame([new_row], columns=['ID', 'CHROM', 'START', 'END', 'TYPE', 'MENDELIAN_VIOLATION'])
    #concat the 2 dataframes
    samplot_survivor_input_hg002_3_4=pd.concat([samplot_survivor_input_hg002_3_4, df])

#save the data frame as a csv
samplot_survivor_input_hg002_3_4.to_csv('samplot_survivor_input_hg002_3_4.csv', index=False)
