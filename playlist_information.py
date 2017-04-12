import requests

from spotifywrapper.access_token import Access_Token


class playlist:
    def __init__(self):
        self.playlistID=''
        self.userID=''
        self.baseurl='https://api.spotify.com/v1/users/{0}/playlists/{1}'
        self.acc_token=Access_Token()

    def update(self,userID,playistID):
        self.userID=userID
        self.playlistID=playistID

    def get_data(self):
        self.inquiery_data_url = self.baseurl.format(*(self.userID,self.playlistID))
        self.acc_token.renew()
        self.general_data = requests.get(self.inquiery_data_url,
                                         headers={'Authorization': 'Bearer ' + self.acc_token.access_token}).json()

    def get_track_list(self):
        temp_set=set()
        for x in self.general_data['tracks']['items']:
            try:
                 temp_set.add(x['track']['id'])
            except:
                continue
        return temp_set

    def get_playlist_name(self):
        return self.general_data['name']


    def get_playlist_description(self):
        return self.general_data['description']

    def get_list_artists(self):
        temp_set=set()
        for x in self.general_data['tracks']['items']:
            try:
                 temp_set.add(x['track']['artist']['id'])
            except:
                continue
        return temp_set