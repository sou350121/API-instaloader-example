# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 10:46:15 2019

@author: Ken

Name :download Story

input : 
    1. your account
    2. target's ID

output : 
    stories from target
    * saved inside dir 
"""

import instaloader

L = instaloader.Instaloader()

# need to be logged in 
LOGIN = ''  # inpur your username
L.load_session_from_file(LOGIN)
L.interactive_login(LOGIN) # interactive login: please input your password

if L.test_login() == LOGIN:
    print("log in sucessfully.")
else:
    raise AssertionError("fail to log in")



# set up your target
# input: list of target's ID. 'None' for retriving all stoies 
TARGET_ID_LIST = list( ('','') ) # input: list of target's ID. ex. 123456789
#stories = profile.get_stories()

for story in L.get_stories(userids  = TARGET_ID_LIST):
    # story is a Story object
    for item in story.get_items(  ):
        # item is a StoryItem object
        L.download_storyitem(item, ':stories') # the second arg is the name of (created)file.
