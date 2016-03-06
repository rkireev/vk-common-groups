
# coding: utf-8

import json
import urllib2
import time

#https://oauth.vk.com/authorize?client_id=5336634&redirect_uri=vk.com&response_type=token 

def get_common_groups(target_group_id, n, token):
    members_number = 0
    offset = 0
    common_groups = {}
    buf = 0
    failed = []
    while offset <= members_number:
        members_request = 'https://api.vk.com/method/groups.getMembers?group_id='+target_group_id+'&sort=id_asc&offset='+str(offset)
        data_group = json.load(urllib2.urlopen(members_request))
        members_number = data_group['response']['count']
        for user_id in data_group['response']['users']:
            groups_request = 'https://api.vk.com/method/groups.get?user_id='+str(user_id)+'&access_token='+token
            data_user = json.load(urllib2.urlopen(groups_request))
            buf+=1
            #if buf%100==0:
            #    print buf
            if data_user.get('response'):
                for group_id in data_user['response']:
                    if common_groups.get(group_id):
                        common_groups[group_id] = 1 + common_groups.get(group_id)
                    else:
                        common_groups[group_id] = 1
                time.sleep(0.32)
            else:
                time.sleep(1)
                failed.append(user_id)
        offset += 1000
    with open('data.txt', 'w') as outfile:
        json.dump(common_groups, outfile)
        
    common_groups_sorted = sorted(common_groups.items(), key=lambda (k,v): v, reverse=True)
    group_id_list = ''
    freqs = []
    for i in range(n):
        freqs.append(common_groups_sorted[i][1])
        group_id_list += str(common_groups_sorted[i][0])+','
    groups_desc_request = 'https://api.vk.com/method/groups.getById?group_ids='+group_id_list#+'&access_token='+token
    groups_desc = json.load(urllib2.urlopen(groups_desc_request))['response']
    groups_names = []
    for desc in groups_desc:
        groups_names.append(desc['name'])
    return groups_names, freqs




