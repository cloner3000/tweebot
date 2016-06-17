## PYTHON AUTO TWEET / MENTION WITH MECHANIZE

![alt tag](https://raw.githubusercontent.com/aldiferdiyan/python_auto_tweet/master/ss.png)


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

For running just
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
we use tweepy for search user to mentions by keyword, you can get consumer key and screet from [http://apps.twitter.com](http://apps.twitter.com)
```sh
consumer_key    = "YOUR consumer_key"
consumer_secret = "YOUR consumer_secret"
access_token        = "YOUR access_token"
access_token_secret = "YOUR access_token_secret"
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

##### Thanks To original developer
[MR. DRAT](https://github.com/drat)
