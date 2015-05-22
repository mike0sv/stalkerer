from api import call_api
import pickle
import warnings
warnings.filterwarnings("ignore")

group = call_api('groups.getMembers', group_id=94018597)
users = group['users']
print users

user_info = []
for chunk in [users[x:x+300] for x in xrange(0, len(users), 100)]:
    chunk_info = call_api('users.get', user_ids=','.join(map(str, chunk)), fields='sex')
    user_info += chunk_info

girls = []
for user in user_info:
    if user['sex'] is 1:
        girls.append(user['uid'])

with open('girls.txt', 'w') as out:
    for girl in girls:
        out.write(str(girl) + '\n')

pickle.dump(girls, open('girls', 'w'))
