#!/usr/bin/env python

import mechanize
import string
import cookielib
from bs4 import BeautifulSoup
import time
import random
from pprint import pprint
import sys
import tweepy


print "=================================================================="
print "                        INDONESIA MERDEKA                         "
print "=================================================================="
#========================================================================

# Set Twitter Accounts Username:Password
akunku = [
    "usernameTwitter:passwordTwitter",
    "usernameTwitter:passwordTwitter",
    "usernameTwitter:passwordTwitter"
]

## ======================================================================
# consumer and token (key,secreet) from apps.twitter.com
consumer_key    = "YOUR consumer_key"
consumer_secret = "YOUR consumer_secret"
access_token        = "YOUR access_token"
access_token_secret = "YOUR access_token_secret"
## =======================================================================
# Configuration text,keyword,url and more
hit = 100000000
jeda_tweet   = 1
config_tweet = [
    {
        'link'    : "http://goo.gl/tffsKN",
        'keyword' : "jogja,yogya,malioboro,prambanan",
        'kata'    :  [
            "Mau Duit ? Ikut Survey Online Berhadiah 1 Juta",
            "Khusus Warga Yogya ! survey online berhadiah 1 juta",
            "Ikut survey online berhadiah 1 juta"
        ]
    },
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
# ========================================================================

# Login ke website twitter dengan menyamar sebagai web browser
# Jika terjadi kesalahan / di blok silahkan gunakan daftar proxy
def login(username,password):
    try:
        write_log("<br>Mencoba koneksi dengan twitter ... <br>")
        print "[Coba login ke twitter.com]"
        br = mechanize.Browser()

        cookies = cookielib.LWPCookieJar()
        br.set_cookiejar(cookies)

        br.set_handle_equiv(True)
        br.set_handle_redirect(True)
        br.set_handle_referer(True)
        br.set_handle_robots(False)
        br.set_debug_http(False)
        br.set_debug_responses(False)
        br.set_debug_redirects(False)
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time = 1)
        #br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; BOLT/2.340) AppleWebKit/530+ (KHTML, like Gecko) Version/4.0 Safari/530.17 UNTRUSTED/1.0 3gpp-gba')]
        br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; id-ID; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
        #br.addheaders = [('User-agent', 'Mozilla/5.0 (Linux; U; Android 4.0.3; id-ID; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30')]
        #br.set_proxies({"http":"116.68.249.133:8080"})

        br.open('https://mobile.twitter.com/session/new')
        #print_forms(br)
        #print(br.response().read())
        br.select_form(nr=0)

        br['session[username_or_email]'] = username
        br['session[password]'] = password
        br.submit()
        return br

    except Exception as e:
        print e
        print"Gagal login"

# Debugging dengn beautifulsoup
def print_forms(br):
  page = br.response().read()
  soup = BeautifulSoup(page, "html.parser");
  forms = soup.find_all("form")
  print forms[0]


# Mengirimkan Tweets
def tweet(text,br):
  try:
    write_log("Mencoba Kirim tweet ... <br>")
    print "[Mencoba kirim pesan tweet]"
    br.open('https://mobile.twitter.com/compose/tweet')
    br.select_form(nr=0)
    br['tweet[text]'] = text
    br.submit() #error originates from here
    write_log("Sukses tweet... <br>")
    print "[OK] Sukses tweet!"
  except:
    write_log("Gagal tweet... <br>")
    #test = (br.response().read())
    print "[FAILED] Gagal mengirimkan tweet!"
    #print test

# # Unfollowing user
# def unfollow(user,br):
#   try:
#     print "Unfollowing "+user
#     br.open('https://mobile.twitter.com/'+user+'/unfollow')
#     br.select_form(nr=0)
#     br.submit()
#   except:
#     print "Gagal unfollow "+user
#
# # Follow user
# def follow(user,br):
#   try:
#     print "Following "+user
#     br.open('https://mobile.twitter.com/'+user)
#     br.select_form(nr=0)
#     br.submit()
#   except:
#     print "Gagal follow "+user
#
# # Keluar dari Twitter
# def logout():
#   try:
#     br.open('http://mobile.twitter.com/logout')
#     br.select_form(nr=0)
#     br.submit()
#   except:
#     print "Gagal Logout "+user

def write_log(log_text):
    try:
        with open("cari.log", "a") as log: log.write(log_text)
    except:
        print "Gagal save log"

#
# def get_text(link):
#      try:
#        with open('data.txt') as f: s = f.read()
#        status_list = s.split(',')
#        status_tag = []
#        for word in status_list:
#              status_tag.append(word+" "+link)
#        return status_tag
#
#      except:
#        print "Error saat generate text"
#
# def generate_text(tags,link):
#   try:
#     with open('data.txt') as f: s = f.read()
#     status_list = s.split(' ')
#     text = ""
#     i    = 0
#     ganjil_genap = 1
#     status_tag = []
#     for word in status_list:
#       if i != 3:
#         text += word+" "
#         i    += 1
#       else:
#         ganjil_genap += 1
#         if ganjil_genap % 2 == 0: # jika (i) genap
#           status_tag.append(tags+" "+text+" "+link)
#         else:
#           status_tag.append(link+" "+text+" "+tags)
#         text = "" # reset text
#         i    = 0  # reset i
#
#     return status_tag
#
#   except:
#     print "Error saat generate text"

def cari_orang(kata_kunci):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    #auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    users = []
    for tweet in api.search(kata_kunci):
        users.append(tweet.user.screen_name)
    return users

# generate text untuk status
def start():
        for x in range(0, hit):
                for config in config_tweet:
                    keywords  = config['keyword'].split(",")
                    for key in keywords:
                        users   = cari_orang(key)
                        for user in users:
                            akun_user = random.choice(akunku).split(":")
                            log_user = akun_user[0] + "," + akun_user[1]
                            print "Akun       : " + log_user
                            br = login(akun_user[0], akun_user[1])
                            time.sleep(jeda_tweet)
                            kata = random.choice(config['kata'])
                            status_tweet = "@"+user+" "+kata+" "+config['link']
                            print "Keyword    : " + key
                            print "Mention Ke : @" + user
                            print "Text       : " + kata
                            print "Link       : " + config['link']
                            tweet(status_tweet, br)
                            print "----------------------------------------------------------------------"
                            print " "
                            time.sleep(jeda_tweet)


start()

#print cari_orang("bekasi")
