import pandas as pd
import random
import time

random.seed(time.time())
df = pd.read_csv('OPHS_AUG_2023.csv')

s = {
    'Sophomore': df[df['Grade'] == 9],
    'Junior': df[df['Grade'] == 10],
    'Senior': df[df['Grade'] == 11]
}

def sample(strat):
    males = strat[strat['sex'] == 'M'].copy()
    females = strat[strat['sex'] == 'F'].copy()

    sampled_males = males.sample(n=12, replace=False)
    sampled_females = females.sample(n=12, replace=False)
    sampled_ = pd.concat([sampled_males, sampled_females])

    if random.randint(0, 1) == 0:
        a = males.drop(sampled_males.index).sample(n=1, replace=False)
    else:
        a = females.drop(sampled_females.index).sample(n=1, replace=False)

    sampled = pd.concat([sampled_, a])

    return sampled

sampled = {}

for grade, strat in s.items():
    sampled[grade] = sample(strat)

print(sampled)

combined_sample = pd.concat(sampled.values())
combined_sample.to_csv('sampled_list.csv', index=False)