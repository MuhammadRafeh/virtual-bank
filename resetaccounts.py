"""
Only run this when the structure of signup.pickle get upset. If you are getting
error on bank.py of something signup.pickle you must run this file.
Note: All the data will be erase by using this
"""

import pickle

file = open('accounts.pickle', 'wb')

obj = {'sbc':{},'apc':{},'arc':{},'as':{}}
pickle.dump(obj, file)
file.close()


print('Reset Accounts Successful')
