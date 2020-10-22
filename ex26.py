#dictionaries

#dicstionary of state abbreviation with full state name as key
states = {
    'Washington': 'WA',
    'Wisconsin': 'WI',
    'Rhode Island': 'RI',
    'Florida': 'FL',
    'Colorado': 'CO'
}

#dictionary of cities with state abbreviation as key
cities = {
    'CA': 'Sacramento',
    'FL': 'Jacksonville',
    'CO': 'Denver'
}

#adding cities to cities dictionary
cities['WI'] = 'Green Bay'
cities['WA'] = 'Everett'

#print states
print('-' * 20)
print("Washington's abbreviation is: ", states['Washington'])
print("Colorado's abbreviation is: ", states['Colorado'])

#print out cities
print('-' * 20)
print('WI state has: ', cities['WI'])
print('CA state has: ', cities['CA'])
