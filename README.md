# pexelpie
python client for Pexel images

## usage

```python
>>> from pexelpie import PexelClient

>>> client = PexelClient(api_key='your_api_key_here')

>>> results = client.search(['apple', 'technology'], search_type='photo')

```

get all the urls from our search results
```python
>>> urls = [photo.url for photo in results]
```
get the high res original from a single result
```python
>>> single_image = results[0]

>>> original = single_image.best_quality
```
or get a low res preview
```python
>>> preview = single_image.preview
```
alternatively get a list of all the image sources
```python
>>> sources = single_image.sources
```
if your search type was for videos then you get back a PexelVideo object
```python
>>> results = client.search(['apple', 'technology'], search_type='video')

>>> single_video = results[0]

>>> hd_video = single_video.best_quality

```
or get a list of still to use as a video preview
```python
>>> preview_images = single_video.preview_images
```
