import  datetime
import requests
class Access_Token:
    def __init__(self):
        self.client_id = '42fb1ad46ba246d29185d0c9f79c6aa8'
        self.client_secret = 'fb80ab1b36544803a52895a754eeeb87'
        self.token_url = "https://accounts.spotify.com/api/token"
        self.scope = "playlist-read-private"
        self.access_token = self.get_access_token()


    def update(self, _cliend_id, _client_secret, _token_url):
        self.client_id = _cliend_id
        self.client_secret = _client_secret
        self.token_url = _token_url
        self.access_token = self.get_access_token()

    def update_scope(self,scope):
        self.scope=scope

    def get_access_token(self):
        self.oldtime = datetime.datetime.now()
        rp = requests.post(self.token_url, data={'grant_type': 'client_credentials', 'client_id': self.client_id,
                                                 'client_secret': self.client_secret})
        return rp.json()['access_token']
        # check if the access token is expired

    def is_expired(self):
        t = datetime.datetime.now()
        m = datetime.timedelta(seconds=1800)
        if t - self.oldtime > m:
            return True
        return False

    def renew(self):
        if self.is_expired()==True:
            self.access_token = self.get_access_token()