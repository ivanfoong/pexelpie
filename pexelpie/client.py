# -*- coding: utf-8 -*-
"""
Peter Nilson 2017 -- http://www.github.com/petenilson
"""
import requests
import json
from .models import PexelSearchResult

DEFAULT_PHOTO_URL = 'http://api.pexels.com/v1/search'
DEFAULT_VIDEO_URL = 'http://api.pexels.com/videos/search'

class PexelClientException(Exception):
    pass


"""
XXX: TODO ADD SOME TYPE OF CACHE SYSTEM
"""

class PexelClient(object):
    """docstring for PexelClient"""
    def __init__(self, api_key=None, default_photo_url=DEFAULT_PHOTO_URL,
                 default_video_url=DEFAULT_VIDEO_URL):
        self.api_key = api_key
        self.default_photo_url = default_photo_url
        self.default_video_url = default_video_url
        self._session = requests.session()

        # Instantiate API credentials

        if not self.api_key:
            raise PexelClientException(
                'Not API key provided to client')

    def search(self, keywords, search_type='photo', per_page=15, page=1):
        """
        Inputs:
            search_type(str):
                either 'photo' or 'video'
            per_page(int):
                max results per page
            page(int):
                which page number to return
        Returns:
            a search result object
        """
        if search_type not in ['video', 'photo']:
            raise PexelClientException('Invalid search_type given')

        params = {
            'query': keywords,
            'per_page': per_page,
            'page': page
        }
        header = {
            'Authorization': self.api_key
        }
        if search_type == 'photo':
            response = self._session.get(
                self.default_photo_url, params=params,
                headers=header
            )
            return PexelSearchResult(
                search_type='photo', response=response.json(),
                keywords=keywords)
        else:
            response = self._session.get(
                self.default_video_url, params=params,
                headers=header
            )
            return PexelSearchResult(
                search_type='video',response=response.json(),
                keywords=keywords)