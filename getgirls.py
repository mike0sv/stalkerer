from api import call_api
import pickle
import warnings
warnings.filterwarnings("ignore")


def get_group_users(group):
    users = []
    new_users = call_api('groups.getMembers', group_id=group)['users']
    offset = 1000
    while len(new_users) > 0:
        users = users + new_users
        new_users = call_api('groups.getMembers', group_id=group, offset=offset)['users']
        offset += 1000

    return users

users = get_group_users('tinthelp')
print len(users)

user_info = []
ch = 300
chunks = [users[x*ch:(x+1)*ch] for x in xrange(len(users) / ch)] + [users[ch * (len(users) / ch):]]
for chunk in chunks:
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
