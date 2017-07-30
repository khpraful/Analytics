import random
import os
import sys

#Dictionary operations
super_heroes = {'Bond' : 'Peter',
                'Ironman': 'Roland',
                'Invincible' : 'James'}

print(super_heroes['Ironman'])
del super_heroes['Bond']
super_heroes['Invincible'] = 'Henry'
print(super_heroes)
print(len(super_heroes))
print(super_heroes.get("Ironman"))
print(super_heroes.get("Bond"))
print(super_heroes.keys())
print(super_heroes.values())
