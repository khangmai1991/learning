#from spotifywrapper import spotify
from pprint import pprint
#
    # s=  m.get_list_of_categories(0)
    # for x in s:
    #     for i in range(0,100):
    #         offset=i*50
    #         k= m.get_category_playlists(x,offset)
    #         for v in k:
    #             pprint(v)


testurl='http://www.last.fm/user/afrodisiax/library/playlists'
import urllib.request
import json
def get_pagecontent(url):
    response = urllib.request.urlopen(url).read()
    result = response.decode('utf-8')
    pprint(result)

get_pagecontent(testurl)