import simplejson as json  # helps to exchange data b/w browser and server
import os  # allows to interact with  operating system

if os.path.isfile('./ages.json') and os.stat('./ages.json').st_size != 0:  # checks presence of file and emptiness
    old_file = open('./ages.json', 'r+')
    data = json.loads(old_file.read())  # load string
    print('current age=', data['age'])
    data['age'] += 1
    print('new age=', data['age'])

else:  # file is empty
    old_file = open('./ages.json', 'w+')
    data = {'name': 'harsh', 'age': 12}
    print('no change in age, default age=', data['age'])

old_file.seek(0)
old_file.write(json.dumps(data))