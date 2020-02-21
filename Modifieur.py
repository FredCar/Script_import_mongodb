#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 13:45:17 2020

@author: fred
"""
import pprint


class Modifieur:
    
    def __init__(self):
        pass
    
    def spliter(self, data, key):
        data[key] = data[key].split(",")
        return data
        
    
    def integer(self, data, key):
        if data[key] != "\\N":
            data[key] = int(data[key])
        return data
                        
