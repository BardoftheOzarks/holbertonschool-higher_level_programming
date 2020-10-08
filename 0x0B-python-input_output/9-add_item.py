#!/usr/bin/python3
'''Add things to a file'''

from sys import argv as av
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = 'add_item.json'
try:
    jlist = list(load_from_json_file(filename))
except:
    jlist = []

for ele in av[1:]:
    jlist.append(ele)

save_to_json_file(jlist, filename)
