"""
use the venv at ~/venvs/ML
the NY State Dept. of Agriculture gave me the data in .pdf form
This script converts it to a usable .csv
"""
from tabula import read_pdf
import pandas as pd
import pdb

filename = './Record_R000599-102623.pdf'
output_filename = 'ny_spice_data_raw_output.tsv'
pages = []
errors = []
num_pages = 178
error_pages = [90]
desired_page_nums = [ i for i in range(1,178+1) if i not in error_pages]
auto_pages = read_pdf(filename, pages=desired_page_nums)

# note: page 90 has improper formatting, so it must be extracted by hand 
page_90 = pd.read_csv('./extracted_by_hand/page_90.tsv',sep='\t')
hand_extracted_pages = [page_90]

all_pages = auto_pages + hand_extracted_pages
df = pd.concat(all_pages)

if __name__ == "__main__":
    df.to_csv(output_filename, sep='\t', index=False)
    # this also writes the row numbers of the df. Do not include that.
