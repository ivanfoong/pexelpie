# -*- coding: utf-8 -*-
"""
Peter Nilson 2017 -- http://www.github.com/petenilson
"""
import json

class PexelVideo(object):
    """
    A data structure to represent a single video returned
    from the video search results.
    """
    def __init__(self, video_result):
        self.video_result = video_result
        self.height = self.video_result['height']
        self.width = self.video_result['width']
        self.image = self.video_result['image']

    @property
    def best_quality(self):
        """
        Returns the highest possible resolution.
        Resolution is measured as the width of the video.
        """
        video_files = self.video_result['video_files']
        video_files = sorted(video_files, key=lambda x: x['width'], reverse=True)
        best_quality = video_files[0]
        return dict(
            url=best_quality['link'],
            width=best_quality['width'],
            height=best_quality['height']
        )

    @property
    def preview_images(self):
        """
        Returns:
            list of preview images of the video in order
        """
        pictures = self.video_result['video_pictures']
        pictures = sorted(pictures, key=lambda x: x['nr'])
        return [i['picture'] for i in pictures]


class PexelPhoto(object):
    """
    A data structure to represent a single photo returned
    from the photo search results.
    """
    def __init__(self, photo_result):
        self.photo_result = photo_result
        self.height = self.photo_result['height']
        self.width = self.photo_result['width']
        self.url = self.photo_result['url']

    @property
    def best_quality(self):
        photos = self.photo_result['src']
        return photos['original']

    @property
    def preview(self):
        photos = self.photo_result['src']
        return photos['tiny']


class PexelSearchResult(object):
    """
    Inputs:
        response(json):
            decoded json response
    """
    def __init__(self, search_type, response):
        self.search_type = search_type
        self.response = response
        self.page = self.response['page']

    def next_page(self):
        """
        Inputs:
            None
        Returns:
            a PexelSearchResult object with search results
            from the next page.
        """
        pass

    @property
    def results(self):
        """
        Returns the results of the search
        """
        if self.search_type=='photo':
            photos = [PexelPhoto(i) for i in self.response['photos']]
            return photos
        else:
            videos = [PexelVideo(i) for i in self.response['videos']]
            return videos