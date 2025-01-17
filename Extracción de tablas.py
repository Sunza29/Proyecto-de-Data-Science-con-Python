import pandas as pd
import pickle
from string import ascii_uppercase as alphabet


all_tables = pd.read_html('https://en.wikipedia.org/wiki/2022_FIFA_World_Cup')


dict_table = {}
for letter, i in zip(alphabet, range(18,67,7)): # A=11, B=18, ...
    df = all_tables[i]
    df.rename(columns={df.columns[1]:'Team'}, inplace=True)
    df.pop('Qualification')
    dict_table[f'Group {letter}'] = df
    
    # Upload (..verify if uploaded correctly)
with open('dict_table', 'wb') as output:
    pickle.dump(dict_table, output)