import pandas as pd

import numpy as np

columns = []

rows = np.array([
                 ['q1', 'q2', 'q3', 'q4', 'q5'], 
                 ['q1', 'q2', 'q3', 'q4', 'q5'],
                 ['q1', 'q2', 'q3', 'q4', 'q5'],
                 ['q1', 'q2', 'q3', 'q4', 'q5'],
                 ['q1', 'q2', 'q3', 'q4', 'q5']
                ])
indeks = ['1','2', '3','4','5']
for i, row in enumerate(rows):
    columns.append('kata '+ str(i+1))

df = pd.DataFrame(rows,columns=columns, index=indeks)