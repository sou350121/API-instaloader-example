# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 12:31:25 2019

@author: Ken

name : login in try
"""
import instaloader
# Get instance
L = instaloader.Instaloader()

USER = "" #input your account's name
L.context.username = USER
print(L.context.username)



# Optionally, login or load session
# 1. login # for first time login in.

L.save_session_to_file() # for first time login
#L.login(USER, PASSWORD)        # (login)
L.interactive_login(USER)      # (ask password on terminal)
print(L.test_login())

# 2. load session

#L.load_session_from_file(USER) # (load session created w/
#L.login(USER, PASSWORD)        #  `instaloader -l USERNAME`)
# the login() must exist just after load_session_from_file()!!!!!!!!!!!!!!!
print(L.test_login())
