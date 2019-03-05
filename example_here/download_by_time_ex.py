# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 00:14:52 2019

@author: Ken

"""
import sys
if sys.stdin.isatty():
    import win_unicode_console
    win_unicode_console.enable()


from datetime import datetime
from itertools import dropwhile, takewhile

import instaloader

L = instaloader.Instaloader()

USER = "" #input your name
TARGET = "" #input target's name
#posts = L.get_hashtag_posts('milfgarden')
# or
posts = instaloader.Profile.from_username(L.context, USER).get_posts()  

SINCE = datetime(2019, 2, 1)  # close to now
UNTIL = datetime(2019, 1, 2)  # far from now

for post in takewhile(lambda p: p.date > UNTIL, dropwhile(lambda p: p.date > SINCE, posts)):
    print(post.date)
    L.download_post(post, TARGET)
    
    