import requests

from spotifywrapper import access_token


class User:
    def __init__(self):
        self.acc_token= access_token.Access_Token()
        self.acc_token.update_scope('playlist-read-private playlist-read-collaborative user-follow-read '
                                    'user-library-read user-read-private user-read-birthdate user-top-read')
        self.baseurl= 'https://api.spotify.com/v1/'
        self.userID=''

    def update(self,userID):
        self.userID=userID


    def get_userdata(self):
        data_url=self.baseurl+'users/{0}'.format(self.userID)
        self.acc_token.renew()
        self.generaldata = requests.get(data_url, headers={'Authorization': 'Bearer ' +
                                                                self.acc_token.access_token}).json()


    def get_user_name(self):
        return self.generaldata['display_name']


    def get_number_of_followers(self):
        return self.generaldata['followers']['total']

#    def get_top_artists(self) due to privacy
#   def get_top_tracks(self)

    def get_list_of_playlists(self):
        data_url=self.baseurl+'users/{0}/playlists'.format(self.userID)
        temp_set= set()
        self.acc_token.renew()
        data = requests.get(data_url, headers={'Authorization': 'Bearer ' +
                                                                                   self.acc_token.access_token}).json()
        for x in data['items']:
            set.add((self.userID, x['id']))



    def get_user_saved_album(self,offset):
        data_url=self.baseurl+'{0}/albums?offset={1}&limit=50'.format(*(self.userID,offset))
        temp_set = set()
        self.acc_token.renew()
        data = requests.get(data_url, headers={'Authorization': 'Bearer ' +
                                                                self.acc_token.access_token}).json()
        for x in data['items']:
            temp_set.add(x['album'][id])

    def get_user_saved_tracks(self, offset):
        data_url = self.baseurl + '{0}/tracks?offset={1}&limit=50'.format(*(self.userID, offset))
        temp_set = set()
        self.acc_token.renew()
        data = requests.get(data_url, headers={'Authorization': 'Bearer ' +
                                                                self.acc_token.access_token}).json()
        for x in data['items']:
            temp_set.add(x['track'][id])

    def get_user_top_tracks(self, offset):
        data_url = self.baseurl + '{0}/top/tracks?offset={1}&limit=50&time_range=long_term'.format(*(self.userID,
                                                                                                    offset))
        temp_set = set()
        self.acc_token.renew()
        data = requests.get(data_url, headers={'Authorization': 'Bearer ' +
                                                                self.acc_token.access_token}).json()
        for x in data['items']:
            temp_set.add(x[id])

    def get_user_top_artist(self, offset):
        data_url = self.baseurl + '{0}/top/artists?offset={1}&limit=50&time_range=long_term'.format(*(self.userID,
                                                                                                      offset))
        temp_set = set()
        self.acc_token.renew()
        data = requests.get(data_url, headers={'Authorization': 'Bearer ' +
                                                                self.acc_token.access_token}).json()
        for x in data['items']:
            temp_set.add(x[id])

    def get_user_followed_artist(self, offset):
        data_url = self.baseurl + '{0}/top/artists?offset={1}&limit=50&time_range=long_term'.format(*(self.userID,
                                                                                                      offset))
        temp_set = set()
        self.acc_token.renew()
        data = requests.get(data_url, headers={'Authorization': 'Bearer ' +
                                                                self.acc_token.access_token}).json()
        for x in data['artist']['items']:
            temp_set.add(x[id])
