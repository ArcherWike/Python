
##################<<< sets in python >>>#####################

x = set('abcde')
y = set('bdxyz')

print('x=', x, '\n')

print(x-y, ' #< Difference in sets\n\n')

print(x | y, ' #< Sum of sets\n\n')

print(x & y, ' #< The common part of the sets\n\n')

print(x ^ y, ' #< Symmetrical difference (XOR)\n\n')

print(x > y, x < y,  ' #< Supervision, subset\n\n')

print('e' in x)


engineers = {'Felix', 'Jacob', 'Ann', 'Alex'}
managers = {'David', 'Jacob'}
print('\n\nengineers', engineers)
print('managers', managers)

print('Felix' in engineers)

print('\nWho are the engineers and managers?', engineers & managers)

print(' \nWho are the engineers or managers?', engineers | managers)

print(' \nEngineers who are not managers:', engineers - managers)

print(' \nManagers who are not engineers:', managers - engineers)

print(' \nAre all managers engineers? (supervision)', engineers > managers)

print(' \nAre they both engineers? (subset)', {'Ann', 'Felix'} < engineers)