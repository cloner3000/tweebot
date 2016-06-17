# PYTHON AUTO TWEET / MENTION WITH MECHANIZE

### Installation

 - we use python 2.7,
 > for windows download from https://www.python.org/downloads/
 - Import Module with pip or easy_install
```python
1. pip install mechanize
2. pip install BeautifulSoup4
3. pip install tweepy
4. pip install pprint
5. pip install random
```

Just run
```python
python auto_twit.py
```

### Configuration

#### Set Twitter Accounts Username:Password
```json
akunku = [
    "usernameTwitter:passwordTwitter",
    "usernameTwitter:passwordTwitter",
    "usernameTwitter:passwordTwitter"
]
```

### Set consumer and token (key,secret)
we use tweepy for search user to mentions by keyword, you can get consumer key and screet from apps.twitter.com
```sh
consumer_key    = "bdd05L329kbnQSiZeoDmlBgNg"
consumer_secret = "dKhbOryGnCuH6o02R5oPgHzNUFbc565d3ARMwURw1JvruLOqhr"
access_token        = "377459935-2QFkhdbF3ZyTmYx2g8eWQlHGUVOO1PV5GrGT7r98"
access_token_secret = "bX9E5X5O0NOM0YazROfPHzekTCQAoDmsgnDnOTNAB47oc"
```

### Set text,keyword,url and more
```python
hit = 100000000
jeda_tweet   = 1
config_tweet = [
    {
        'link'    : "http://goo.gl/tffsKN", #url
        'keyword' : "jogja,yogya,malioboro,prambanan", ## keyword separated by (,)
        'kata'    :  [
            "Mau Duit ? Ikut Survey Online Berhadiah 1 Juta",
            "Khusus Warga Yogya ! survey online berhadiah 1 juta",
            "Ikut survey online berhadiah 1 juta"
        ] # Text to mentions or tweet
    },
    # set this if multiple
    # {
    #     'link'    : "http://goo.gl/tffsKN",
    #     'keyword' : "bekasi",
    #     'kata'    :  [
    #         "Mau Duit ? Ikut Survey Online Berhadiah 1 Juta",
    #         "Khusus Warga Bekasi ! survey online berhadiah 1 juta",
    #         "Ikut survey online berhadiah 1 juta"
    #     ]
    # },
]
```

That's it ..
