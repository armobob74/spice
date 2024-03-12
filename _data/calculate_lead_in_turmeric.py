import numpy as np
from matplotlib import pyplot as plt
datapath = './ny_ag/output/lead_data.tsv'
with open(datapath) as f:
    data = f.read()

data = data.split('\n')
turmeric_rows = [row for row in data if 'turmeric' in row.lower()]

data = [row.split('\t') for row in data[1:-1]]
turmeric_rows = [row.split('\t') for row in turmeric_rows]

def get_levels(rows):
    levels = []
    for row in rows:
        val = row[-1]
        try:
            ret = float(val)
        except ValueError:
            # "None detected"
            ret = 0
        levels.append(ret)
    return levels


if __name__ == "__main__":
    turmeric_lead_levels = get_levels(turmeric_rows)
    data_lead_levels = get_levels(data)
    print(np.mean(turmeric_lead_levels), np.std(turmeric_lead_levels))

