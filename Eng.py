# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 14:58:34 2019

@author: user
"""
import json
import codecs

list_A=[]
list_B=[]
list_file=["1","2","3","4"]
for num in list_file:
    file = open('Eng'+num+'.csv', 'r')
    content=file.readlines()
    for line in content:
        line = line.strip()
        if line.split(',')[0] in list_A:
            continue
        else:
            list_A.append(line.split(',')[0])
            list_B.append(line.split(',')[1])
    file.close()

dict = dict.fromkeys(list_A)

x=0
for data in dict.keys():
    dict[data]=list_B[x]
    x=x+1
new_dict = {v : k for k, v in dict.items()}
with codecs.open('英文單字.json','w',"utf-8") as f:#給網頁讀取資訊的檔案
      f.write(json.dumps(dict,ensure_ascii=False))
