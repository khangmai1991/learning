import requests

from spotifywrapper import access_token


class Artist:
    def __init__(self):
        self.acc_token= access_token.Access_Token()
        self.baseurl= 'https://api.spotify.com/v1/'
        self.artistID=''


    def update(self,artistID):
        self.artistID=artistID

    def get_artist_genre(self):
        data_url = self.baseurl + 'artists/{0}'.format(self.artistID)
        self.acc_token.renew()
        self.data = requests.get(data_url, headers={'Authorization': 'Bearer ' +
                                                                self.acc_token.access_token}).json()


        return self.data['genre']

    def get_artist_name(self):
        return self.data['name']

    def get_artist_popularity(self):
        return self.data['popularity']


    def get_artist_album(self,offset):
        temp_set=set()
        data_url=self.baseurl+'artist/{0}/albums?offset={1}&limit=50&album_type=album'.format(*(self.artistID,offset))
        data= requests.get(data_url, headers={'Authorization': 'Bearer ' +
                                                                self.acc_token.access_token}).json()
        for  x in data['items']:
            temp_set.add(x['id'])

        return temp_set

    def get_artist_toptracks(self):
        temp_set = set()
        data_url = self.baseurl + 'artists/{0}/top-tracks'.format(
            self.artistID)
        data = requests.get(data_url, headers={'Authorization': 'Bearer ' +
                                                                self.acc_token.access_token}).json()
        for x in data['tracks']:
            temp_set.add(x['id'])

        return temp_set

    def get_related_artist(self):
        temp_set=set()
        data_url=self.baseurl+'artists/{0}/related-artists'.format(self.artistID)
        data= requests.get(data_url, headers={'Authorization': 'Bearer ' +
                                                                self.acc_token.access_token}).json()
        for  x in data['artists']:
            temp_set.add(x['id'])

        return temp_set