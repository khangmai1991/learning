import requests

from spotifywrapper import access_token


class track:
    def __init__(self):
        self.trackID='' #spotifyID
        self.baseurl='https://api.spotify.com/v1/'
        self.acc_token= access_token.Access_Token()

    def get_track_ID_from_spotify(self, myinput):
        string = "https://api.spotify.com/v1/search?q=track:" + myinput[0] + " artist:" + str(
            myinput[1]) + "&type=track"
        data = requests.get(string, headers={'Authorization': 'Bearer ' + self.acc_token.access_token}).json()
        return data


    def get_trackdata(self):
        data_url=self.baseurl+'tracks/'+ self.trackID
        self.acc_token.renew()
        self.general_data = requests.get(data_url, headers={'Authorization': 'Bearer ' + self.acc_token.access_token}).json()


    def get_track_analysis_data(self):
        data_url=self.baseurl+ 'audio-analysis'+ self.trackID
        self.acc_token.renew()
        self.analysis_data = requests.get(data_url, headers={'Authorization': 'Bearer ' +
                                                                              self.acc_token.access_token}).json()


    def get_track_feature_data(self):
        data_url=self.baseurl+ 'audio-features'+ self.trackID
        self.acc_token.renew()
        self.feature_data = requests.get(data_url, headers={'Authorization': 'Bearer ' +
                                                                             self.acc_token.access_token}).json()

#please look at https://developer.spotify.com/web-api/get-audio-features/ for more information about the features
    def get_acousticness(self):
        return self.feature_data['acousticness']


    def get_danceabilty(self):
        return self.feature_data['danceability']

    def get_energy(self):
        return self.feature_data['energy']

    def get_speechiness(self):
        return self.feature_data['speechiness']

    def get_loudness(self):
        return self.feature_data['loudness']

    def get_mode(self):
        return self.feature_data['mode']

    def get_instrumentalness(self):
        return self.feature_data['instrumentalness']

    def get_liveness(self):
        return self.feature_data['liveness']

    def get_valence(self):
        return self.feature_data['valence']

    def get_time_signature(self):
        return self.feature_data['time_signature']

    def get_tempo(self):
        return self.feature_data['tempo']

    def get_key(self):
        return self.feature_data['key']


    def get_id(self):
        return  self.general_data['id']

    def get_name(self):
        return  self.general_data['name']

    def get_popularity(self):
        return  self.general_data['popularity']


    def get_available_market(self):
        return self.general_data['available_markets']


    def get_analysis_elements(self,key_string):
        return self.analysis_data[key_string]





