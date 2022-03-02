import pandas as pd
import random
data_file = pd.read_csv("./data/french_words_2.csv")
print(data_file)

option1 = data_file.to_dict()
option3 = data_file.to_dict(orient='records')
print(option3)

some_list = ['a','b','c']

random_pick =  random.choice(some_list)

print(random_pick)

print (random.choice(option3))
print(random.choice(option3)["French"])