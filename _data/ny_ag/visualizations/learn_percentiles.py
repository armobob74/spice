from matplotlib import pyplot as plt
import pandas as pd 
import numpy as np

df = pd.read_csv('lead_data.tsv', sep='\t')
def parseFloat(s):
    try:
        return float(s)
    except ValueError:
        # if it is a string, it means 'none'
        return 0
lead_levels = df['Lead level'].apply(parseFloat)

sorted_data = np.sort(lead_levels)
lead_levels = sorted_data[:-20] # remove outliers


# calculate percentiles 
percentiles = np.arange(0,100,5)
lead_values = np.percentile(sorted_data, percentiles)

print("percentiles =", list(percentiles))
print("lead_values =", list(lead_values))
#fig, ax = plt.subplots()
#ax.plot(lead_values, percentiles, '-')
#ax.set_xlabel('lead')
#ax.set_ylabel('%ile')
#ax.set_title('ax_title') 
#plt.show()
