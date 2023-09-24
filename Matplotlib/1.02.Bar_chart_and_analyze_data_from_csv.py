from matplotlib import pyplot as plt 
from collections import Counter
import numpy as np
import pandas as pd 
import csv
print("Start: ")

''' 
-- Using Python to open CSV
with open('Matplotlib/img/devs_data.csv') as csv_file:
   csv_reader = csv.DictReader(csv_file)

   language_counter = Counter()
   for row in csv_reader:
      language_counter.update(row['LanguagesWorkedWith'].split(';'))
'''

# Using Pandas to Use CSV
df = pd.read_csv("Matplotlib/img/devs_data.csv")
ids = df['Responder_id']
lan_response = df['LanguagesWorkedWith']

language_counter = Counter()
for response in lan_response:
   language_counter.update(response.split(';'))

languages = []
popularity = []
for i in language_counter.most_common(15):
   languages.append(i[0])
   popularity.append(i[1])

print(languages)
print(popularity)

plt.barh(languages, popularity)
plt.title("Popular Programming Language")
plt.xlabel("Number of Developer who use this language")

plt.tight_layout() # Add Padding
plt.savefig("Matplotlib/img/plot_1.02.png")
plt.show()







