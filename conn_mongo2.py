# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 11:04:14 2016

@author: DA
"""

import pymongo
from bson import json_util, ObjectId
from pandas.io.json import json_normalize
import json

try:
    import _locale
except ImportError:
    _locale = None
'''
class PyConnect(object):
    
    def __init__(self, host, port, db):
        self.conn = pymongo.MongoClient(host, port)
        self.db = self.conn[db]
            
    def setCollection(self, collection):
         self.coll = self.db[collection]
         
        
    def mongo_to_dataframe(self, mongo_data):
        sanitized = json.loads(json_util.dumps(mongo_data))
        df = json_normalize(sanitized)
        #df = pd.DataFrame(normalized)
        return df       
'''
           
         
def conn_mongo(host, port, db):
    conn = pymongo.MongoClient(host, port)
    db = conn[db]  
    return db    
         
def mongo_to_df(mongo_data):
        sanitized = json.loads(json_util.dumps(mongo_data))
        df = json_normalize(sanitized)
        #df = pd.DataFrame(normalized)
        return df         
         
         










