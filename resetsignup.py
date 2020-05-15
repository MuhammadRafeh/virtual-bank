"""
Only run this when the structure of signup.pickle get upset. If you are getting
error on bank.py of something signup.pickle you must run this file.
Note: All the data will be erase by using this
"""

import pickle

file = open('signup.pickle', 'wb')

obj = {}
pickle.dump(obj, file)
file.close()


print('Reset Signup Successful')