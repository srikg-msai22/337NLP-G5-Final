with open('dialogues_001.json', 'r') as f:
  data01 = json.load(f)

with open('dialogues_002.json', 'r') as f:
  data02 = json.load(f)

with open('dialogues_003.json', 'r') as f:
  data03 = json.load(f)

with open('dialogues_004.json', 'r') as f:
  data04 = json.load(f)

with open('dialogues_005.json', 'r') as f:
  data05 = json.load(f)

with open('dialogues_006.json', 'r') as f:
  data06 = json.load(f)

with open('dialogues_007.json', 'r') as f:
  data07 = json.load(f)

with open('dialogues_008.json', 'r') as f:
  data08 = json.load(f)

with open('dialogues_009.json', 'r') as f:
  data09 = json.load(f)

with open('dialogues_010.json', 'r') as f:
  data10 = json.load(f)

with open('dialogues_011.json', 'r') as f:
  data11 = json.load(f)

with open('dialogues_012.json', 'r') as f:
  data12 = json.load(f)

with open('dialogues_013.json', 'r') as f:
  data13 = json.load(f)

with open('dialogues_014.json', 'r') as f:
  data14 = json.load(f)

with open('dialogues_015.json', 'r') as f:
  data15 = json.load(f)

with open('dialogues_016.json', 'r') as f:
  data16 = json.load(f)

with open('dialogues_017.json', 'r') as f:
  data17 = json.load(f)

with open('dialogues_018.json', 'r') as f:
  data18 = json.load(f)

with open('dialogues_019.json', 'r') as f:
  data19 = json.load(f)

with open('dialogues_020.json', 'r') as f:
  data20 = json.load(f)

with open('dialogues_021.json', 'r') as f:
  data21 = json.load(f)
  
data = data01 + data02 + data03 + data04 + data05 + data06 + data07 + data08 + data09 + data10 + data11 + data12 + data13 + data14 + data15 + data16 + data17 + data18 + data19 + data20 + data21

dialogue_counts = {'muls': 0, 'pmuls': 0, 'sngs': 0, 'ssngs': 0, 'wozs':0}

for element in data:
  if 'MUL' in element['dialogue_id']:
    if 'PMUL' in element['dialogue_id']:
      dialogue_counts['pmuls'] += 1
    else:
      dialogue_counts['muls'] += 1
  if 'SNG' in element['dialogue_id']:
    if 'SSNG' in element['dialogue_id']:
      dialogue_counts['ssngs'] += 1
    else:
      dialogue_counts['sngs'] += 1
  if 'WOZ' in element['dialogue_id']:
      dialogue_counts['wozs'] += 1

dialogue_counts

services_types = []

for element in data:
  temp = element['services']
  for temp1 in temp:
    services_types.append(temp1)

services = list(set(services_types))

len(services_types)

services_counts = {'bus': 0, 'taxi': 0, 'hospital': 0, 'train': 0, 'hotel':0, 'restaurant':0, 'attraction':0}

for service in services_types:
  if service == 'bus':
    services_counts['bus'] += 1
  if service == 'taxi':
    services_counts['taxi'] += 1
  if service == 'hospital':
    services_counts['hospital'] += 1
  if service == 'train':
    services_counts['train'] += 1
  if service == 'hotel':
    services_counts['hotel'] += 1
  if service == 'restaurant':
    services_counts['restaurant'] += 1
  if service == 'attraction':
    services_counts['attraction'] += 1

services_counts
