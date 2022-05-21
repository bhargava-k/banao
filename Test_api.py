import requests
import json


# key = "6be512237a0d7552f529ad6e2a9beae0"
# uid = "152644485%40N08"

# API_endpoint = "https://www.flickr.com/services/rest/?method=flickr.photos.getPopular&api_key="+key+"&user_id="+uid+"&per_page=500&format=json&nojsoncallback=1"
# json_data = requests.get(API_endpoint).json()

def test_key1(): #KEY and UID Both are correct
    key = "6be512237a0d7552f529ad6e2a9beae0"
    uid = "152644485%40N08"
    API_endpoint = "https://www.flickr.com/services/rest/?method=flickr.photos.getPopular&api_key="+key+"&user_id="+uid+"&format=json&nojsoncallback=1"
    response=requests.post(API_endpoint)
    data = json.loads(response.content)
    # print(data)
    assert data["photos"]["page"] == 1

    
def test_key2(): #KEY is wrong and UID is correct
    key = "f1d878cd8954c835bbf20046680dff5z"
    uid = "152644485%40N08"
    API_endpoint = "https://www.flickr.com/services/rest/?method=flickr.photos.getPopular&api_key="+key+"&user_id="+uid+"&format=json&nojsoncallback=1"
    response=requests.post(API_endpoint)
    data = json.loads(response.content)
    # print(data)
    assert data["stat"] == "fail"

def test_key3(): #KEY is correct and UID is wrong
    key = "f1d878cd8954c835bbf20046680dff5a"
    uid = "A52644485%40N08"
    API_endpoint = "https://www.flickr.com/services/rest/?method=flickr.photos.getPopular&api_key="+key+"&user_id="+uid+"&format=json&nojsoncallback=1"
    response=requests.post(API_endpoint)
    data = json.loads(response.content)
    # print(data)
    assert data["stat"] == "fail"

def test_key4(): # Both KEY and UID is Wrong
    key = "f1d878cd8954c835bbf20046680dff5z"
    uid = "A52644485%40N08"
    API_endpoint = "https://www.flickr.com/services/rest/?method=flickr.photos.getPopular&api_key="+key+"&user_id="+uid+"&format=json&nojsoncallback=1"
    response=requests.post(API_endpoint)
    data = json.loads(response.content)
    # print(data)
    assert data["stat"] == "fail"


