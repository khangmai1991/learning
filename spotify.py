import requests
import pickle
from spotifywrapper import access_token


class spotify:
    def __init__(self):
        self.acc_token= access_token.Access_Token()
        self.baseurl= 'https://api.spotify.com/v1/browse/'


    # def get_list_of_categories(self):
    #     data_url = self.baseurl + 'categories?offset=0&limit=50'
    #     temp_set=set()
    #     self.acc_token.renew()
    #     data= requests.get(data_url, headers={'Authorization': 'Bearer ' +
    #                                                                          self.acc_token.access_token}).json()
    #     for x in data['categories']['items']:
    #         temp_set.add(x['id'])
    #
    #     return  temp_set
    #
    #
    # def get_category_playlists(self,categoryID):
    #     temp_set=set()
    #     data_url= self.baseurl+'categories/{0}/playlists?offset=0&limit=50'.format(categoryID)
    #     self.acc_token.renew()
    #     data = requests.get(data_url, headers={'Authorization': 'Bearer ' +
    #                                                             self.acc_token.access_token}).json()
    #     #default user = spotify
    #     for x in data['playlist']['items']:
    #         temp_set.add((x['owner']['id'], x['id']))
    #     return temp_set
    #
    #
    # def get_feature_playlists(self,categoryID):
    #     temp_set=set()
    #     data_url= self.baseurl+'featured-playlists?offset=0&limit=50'.format(categoryID)
    #     self.acc_token.renew()
    #     data = requests.get(data_url, headers={'Authorization': 'Bearer ' +
    #                                                             self.acc_token.access_token}).json()
    #     #default user = spotify
    #     for x in data['playlist']['items']:
    #         temp_set.add((x['owner']['id'], x['id']))
    #     return temp_set

    def get_list_of_categories(self,offset):
        data_url = self.baseurl + 'categories?offset={0}&limit=50'.format(offset)
        temp_set = set()
        self.acc_token.renew()
        data = requests.get(data_url, headers={'Authorization': 'Bearer ' +
                                                                self.acc_token.access_token}).json()
        for x in data['categories']['items']:
            temp_set.add(x['id'])

        return temp_set

    def get_category_playlists(self, categoryID,offset):
        temp_set = set()
        data_url = self.baseurl + 'categories/{0}/playlists?offset={1}&limit=50'.format(*(categoryID,offset))
        self.acc_token.renew()
        data = requests.get(data_url, headers={'Authorization': 'Bearer ' +
                                                                self.acc_token.access_token}).json()
        # default user = spotify
        for x in data['playlists']['items']:
            temp_set.add((x['owner']['id'],x['id']))
        return temp_set

    def get_feature_playlists(self,offset):
        temp_set = set()
        data_url = self.baseurl + 'featured-playlists?offset={0}&limit=50'.format(offset)
        self.acc_token.renew()
        data = requests.get(data_url, headers={'Authorization': 'Bearer ' +
                                                                self.acc_token.access_token}).json()
        # default user = spotify
        for x in data['playlist']['items']:
            temp_set.add((x['owner']['id'],x['id']))
        return temp_set

    def get_all_availableartist(self):
        data_url= 'https://api.spotify.com/v1/search?q=year:0000-9999&type=artist&offset=0&limit=1'
        self.acc_token.renew()
        temp_set = set()
        data = requests.get(data_url, headers={'Authorization': 'Bearer ' +
                                                                self.acc_token.access_token}).json()

        for x in range(0,data['artists']['total']):
            try:
                temp_set.add(self.get_next_artirst(x))
                print(x)
            except:
                continue

        return temp_set

    def get_next_artirst(self,offset):
        data_url = 'https://api.spotify.com/v1/search?q=year:0000-9999&type=artist&offset={0}&limit=1'.format(offset)
        self.acc_token.renew()

        data = requests.get(data_url, headers={'Authorization': 'Bearer ' +
                                                                self.acc_token.access_token}).json()
        return data['artists']['items'][0]['id']
    def get_next_artist_genre(self,offset):
        data_url = 'https://api.spotify.com/v1/search?q=year:0000-9999&type=artist&offset={0}&limit=1'.format(offset)
        self.acc_token.renew()

        data = requests.get(data_url, headers={'Authorization': 'Bearer ' +
                                                                self.acc_token.access_token}).json()
        return data['artists']['items'][0]['genres'],data['artists']['items'][0]['id']

import  json
def save(url,data):
    with open(url, 'w') as fjson:
        json.dump(data, fjson, ensure_ascii=False)

def load(url):
    with open(url, 'w') as fjson:
        data=json.load(fjson)
    return data
from pprint import pprint
import concurrent.futures
def get_listofgenre():
    lines = []
    with open("E:\\MaiKhang\\genre list.txt") as file:
        for line in file:
            line = line.lower().strip() # or someother preprocessing
            lines.append(line)
    return lines

def get_artists_and_save(startindex, endindex, saveurl):
    obj = spotify()
    temp_set = set()
    for m in range(startindex, endindex+1):
        print(m)
        try:
          temp_set.add(obj.get_next_artirst(m))

        except:
            continue
    if len(temp_set)==0:
        print("failed")
        return
    d = {}
    d1 = []
    for x in temp_set:
        d1.append({'artistID': x})
    d['artists'] = d1
    try:
        save(saveurl, d)
    except:
        print("could not save into " + saveurl)

def statistic_artist(startindex,endindex, saveurl):
    list_of_genre=get_listofgenre()
    dict1= dict()
    obj = spotify()
    artists=set()
    for m in range(startindex, endindex + 1):
        print(m)
        try:
            temp_set,x = obj.get_next_artist_genre(m)
            artists.add(x)
            print(x)
            for m in temp_set:
                if m in dict1:
                    dict1[m] += 1
                else:
                    dict1[m] = 1

        except:
            continue

    try:
        pickle.dump(dict1, open(saveurl, 'wb'))
        pickle.dump(artists, open(saveurl+'.artists', 'wb'))
    except:
        print("could not save into " + saveurl)

def test():

    m= 2879086
   # m=377
    y = (m / 100)
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        for x in range(4, 20):
            saveurl = 'E:\\MaiKhang\\4\\{0}.data'.format(x)
            if x == 0:
                startindex = (int)(y * x )
            else:
                startindex = (int)(y * x + 1)
            if x == 99:
                endindex = (int)(y * (x + 1)-1)
            else:
                endindex = (int)(y * (x + 1))
            executor.submit(statistic_artist, startindex, endindex,saveurl)


#statistic_artist(0,10,'E:\\MaiKhang\\4\\1.json')

test()

