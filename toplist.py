
import requests
import time
import json
for a in range(52):
    url = 'https://c.y.qq.com/v8/fcg-bin/fcg_v8_toplist_cp.fcg?topid={}'.format(a)
    data = requests.get(url).text
    time(1)
    if len(data) > 1:
        jsondata = json.loads(data)

        songlist = jsondata.get('songlist')
        topinfo = jsondata.get('topinfo')
        print(topinfo['ListName'])
        print('------------------------------------------')
        b = len(songlist)
        for i in range(b):
                songlistDict = songlist[i]
                data = songlistDict['data']
                print(i+1, data['songname'])
                print('  ', data['interval'])
                singer = data['singer']
                singerDict = singer[0]
                print('  ', singerDict['name'])
                print('---------------')

    else:
        pass