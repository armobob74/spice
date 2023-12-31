"""
the raw output is ugly and also full of duplicate brand names and typos
this script formats it and removes some of the worst offenders
"""
import pandas as pd
from utils import parseFloat

df = pd.read_csv('./ny_spice_data_raw_output.tsv', sep='\t')

df = df[::-1] # reverse the order of rows

# Set all string values to lowercase and remove all commas
df = df.applymap(lambda x: x.lower().replace(',', '') if isinstance(x, str) else x)

# remove the rows where analyte == total, because they may confuse people
df = df[df['ANALYTE'] != 'total']

df = df.drop(['LAB_NUMBER', 'FL_NUMBER', 'Unit'], axis=1)

df.rename(columns={
        'COLDATE': 'Test date',
        'PRODUCT_NAME': 'Product name',
        'BRAND': 'Brand',
        },inplace=True
)

df['RESULT'] = df['RESULT'].apply(parseFloat) # replace all strings with 'None detected'

lead_df = df[df['ANALYTE'] == 'lead']
lead_df = lead_df.drop('ANALYTE', axis=1)
lead_df = lead_df.rename(columns={'RESULT':'Lead level'})

#arsenic_df = df[df['ANALYTE'] == 'arsenic']
#cadmium_df = df[df['ANALYTE'] == 'cadmium']


if __name__ == "__main__": 
    #df.to_csv('output/all_data.tsv', sep='\t', index=False)
    lead_df.to_csv('output/lead_data.tsv', sep='\t', index=False)
    #arsenic_df.to_csv('output/arsenic_data.tsv', sep='\t', index=False)
    #cadmium_df.to_csv('output/cadmium_data.tsv', sep='\t', index=False)
