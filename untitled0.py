# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:28:57 2019

@author: zzy
"""

import json
a = ["asdads", "asdasd", {"a":1, "b":2}]
the_json = json.dumps(a)
with open("file.json", "w") as f:
    f.write(the_json)

another_json = None   
with open("file.json", "r") as f:
    another_json = f.read()
    
print(type(another_json))