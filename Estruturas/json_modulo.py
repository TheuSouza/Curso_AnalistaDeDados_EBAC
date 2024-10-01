import json


# De Json para Dict
data = json.load(open(file='nome do arquivo', mode='r'))

# De dict para Json
data_json = json.dumps(data, indent=4, ensure_ascii=False)
