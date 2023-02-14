# RANDOM GENERATOR

import random

for i in range(3):
    print(random.randint(10, 50))
    # print(random.random())

members = ['john', 'mary', 'bob', 'mosh']
leader = random.choice(members)
print(leader)