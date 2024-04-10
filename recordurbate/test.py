#!/usr/bin/python3
#
import time
import requests


def is_online_(username):
        url = "https://chaturbate.com/"+username
        
        print(url)
        try:
            r = requests.get(url)
            if r.status_code != 200: return False
            if r.text.find("404") != -1:
                #print("find 404")
                return False
            if r.text.find("Room is currently offline") != -1:
                #print("Room is currently offline")
                return False
            if r.text.find("chat_room") != -1:
                #print("chat_room")
                return True
            return False
        except Exception as e:
            #print("Exception")
            return False
        
print(is_online_("_amyliu_"))
print(is_online_("galantini"))
print("-------------")