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
cities['RI'] = 'Providence'

#print states
print('-' * 20)
print("Washington's abbreviation is: ", states['Washington'])
print("Colorado's abbreviation is: ", states['Colorado'])

#print out cities
print('-' * 20)
print('WI state has: ', cities['WI'])
print('CA state has: ', cities['CA'])

#using state then cities dictionary
print('-' * 20)
print('Washington has: ', cities[states['Washington']])
print('Florida has: ', cities[states['Florida']])

#print every state abbreviation
print('-' * 20)
for state, abbre in states.items(): #state is key, value is abbre
    print('%s is abbreviated as %s.' % (state, abbre))
    
#print every cite in state
print('-' * 20)
for abbre, city in cities.items(): #abbre, city is the key-value pair
    print('%s has the city %s.' % (abbre, city))
    
#doing both at the same time
print('-' * 20)
for state, abbre in states.items():
    print('%s is abbreviated as %s and has %s.' % (state, abbre, cities[abbre]))

print('-' * 20)    
#abbreviating a state that may not be there
state = states.get('Michigan', None)

if not state:
    print('Sorry, that state is not in the dictionary.')
    
#get a city with a default value
city = cities.get('MI', 'not listed')
print('The city for MI is: %s' %city)
