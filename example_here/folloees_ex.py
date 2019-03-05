# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 20:20:50 2019

@author: Ken

name : auto-like machine
"""


import instaloader 

L = instaloader.Instaloader()

TARGET = "" # input the username that you want to check


profile = instaloader.Profile.from_username(L.context, TARGET)

# log in a account for using the function : profile.get_followers().
# I use my account ken_sou_ as an example below. 
USER = '' # input your account
L.load_session_from_file(USER) 
L.interactive_login(USER)  # input my password for logging in. USER

# check if it logs in successfully or not.
if L.test_login is not None:
    print("log in successfully.")
else:
    print("fail to log in !")


# save the list as txt file.
with open("user_{}_followees.txt".format(TARGET),'w') as f :
    for follow in profile.get_followees(): 
        print( follow ,file = f )
    print("user_{}_followees.txt built sucessfully.".format(TARGET))


def nameOnly_format():
        # to check if the profile is empty or not.
    if profile.get_followees() is None:
        raise AssertionError('profile must not be empty.')
        
    followees_list = []
    for follow in profile.get_followees():
        line = str(follow).split(' ')
        followees_list.append(line[1])
    
    with open("user_{}_followees_name.txt".format(TARGET),'w') as f :
        for name in followees_list:
            print(name, file = f)
    print("user_{}_followees_name.txt built sucessfully.".format(TARGET))

nameOnly_format()