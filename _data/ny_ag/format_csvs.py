"""
the raw output is ugly and also full of duplicate brand names and typos
this script formats it and removes some of the worst offenders
"""
import pandas as pd

df = pd.read_csv('./ny_spice_data_raw_output.tsv', sep='\t')

# Set all string values to lowercase and remove all commas
df = df.applymap(lambda x: x.lower().replace(',', '') if isinstance(x, str) else x)

# remove the rows where analyte == total, because they may confuse people
df = df[df['ANALYTE'] != 'total']

df = df.drop(['LAB_NUMBER', 'FL_NUMBER', 'Unit'], axis=1)

df.rename(columns={
        'COLDATE': 'Test date',
        'PRODUCT_NAME': 'Product name',
        'BRAND': 'Brand',
        'ANALYTE': 'Testing for',
        'RESULT':'Result (ppb)'
        },inplace=True
)

lead_df = df[df['Testing for'] == 'lead']
arsenic_df = df[df['Testing for'] == 'arsenic']
cadmium_df = df[df['Testing for'] == 'cadmium']


if __name__ == "__main__": 
    #df.to_csv('output/all_data.tsv', sep='\t', index=False)
    lead_df.to_csv('output/lead_data.tsv', sep='\t', index=False)
    arsenic_df.to_csv('output/arsenic_data.tsv', sep='\t', index=False)
    cadmium_df.to_csv('output/cadmium_data.tsv', sep='\t', index=False)
