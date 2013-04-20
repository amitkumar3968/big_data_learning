import json
from pprint import pprint

Data = '[{"id": 1,"parent_id": 0,"name": "item 1"},\
         {"id": 2,"parent_id": 0,"name": "item 2"},\
         {"id": 3,"parent_id": 1,"name": "item 3"}]'
List = json.loads(Data)
[[IItem.update({'children' : List.pop(List.index(Item))})  for IItem in List if Item['parent_id'] == IItem['id']] for Item in List]
Data = json.dumps(List)
pprint(Data)
