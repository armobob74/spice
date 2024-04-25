import pandas as pd
import json

path_to_data = '../ny_ag/output/lead_data.tsv'
df = pd.read_csv(path_to_data, sep='\t')
raw_categories = list(df['Product name'].unique())

# keys are raw names, values are assigned categories
path_to_categories = './category_classifier.json'
category_classifier = {}
with open(path_to_categories) as j:
    category_classifier = json.load(j)

with open("./chatgpt.json") as j:
    chatgpt_classifier = json.load(j)

## conduct checks

problems = 0

for key in category_classifier:
    cgpt_answer = chatgpt_classifier.get(key, None)
    if cgpt_answer and cgpt_answer != category_classifier[key]:
        problems += 1
        print('disagreement', key, cgpt_answer, category_classifier[key], sep=' | ')

for key in chatgpt_classifier:
    if key not in raw_categories:
        problems += 1
        print('hallucination', key)

for key in raw_categories:
    if key not in chatgpt_classifier and key not in category_classifier:
        problems += 1
        print('missing',key)

if problems:
    raise ValueError(f"Fix {problems} issues with classifierbefore resuming analysis")
## after

if False:
    unknown_categories = raw_categories.copy()
    for category in raw_categories:
        if category.lower() in category_classifier:
            unknown_categories.remove(category)
        elif 'masala' in category.lower():
            print(f'"{category}":"pickle masala",')

    print(unknown_categories)
    print(len(unknown_categories))
