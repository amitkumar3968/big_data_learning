import anydbm
db = anydbm.open('captions.db',  'c')

db['clear.png'] = 'My Photo is here'
print db['clear.png']

for key in db:
    print key
    
db.close
