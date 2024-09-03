
expected_keys = {'type', 'event', 'visit_start', 'visit_end', 'user_id', 'product'}
metric = {'type': 'fe',
          'event': 'site_creation',
          'visit_start': 1622521388,
          'user_id': 342341,
          'product': 'control_panel',
          'user_pseudo_id': 23456789096344}

keys = set(metric.keys())

print(expected_keys.difference(keys))
print(keys.difference(expected_keys))
print(keys.symmetric_difference(expected_keys))

for key in expected_keys.difference(keys):
    print('\n' + key + ' parameter is missing')


for key in keys.difference(expected_keys):
    print('\n' + key + ' parameter is superfluous')

