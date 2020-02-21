#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 15:48:21 2020

@author: fred
"""
from pymongo import MongoClient

class DBInteract:
    
    def __init__(self, host, port, base="", collec=""):
        self.client = MongoClient(host, port)
        self.dbase = self.client[base]
        self.collec = self.dbase[collec]
    
    
    def insert(self, data={}, method="one"):
        if method == "one":
            self.collec.insert_one(data)
        else:
            self.collec.insert_many(data)

    
    
    def update(self, filtre={}, updata={}, method="one"):
        if method == "one":
            self.collec.update_one(filtre, {"$set": updata})
        else:
            self.collec.update_many(filtre, {"$set": updata})
    
    
    def read(self, collec="", key=""):
        self.result = self.collec.find({})
        return self.result
    
    
    def delete(self, filtre={}, method="one"):
        if method == "one":
            self.collec.delete_one(filtre)
        else:
            self.collec.delete_many(filtre)