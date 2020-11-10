#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import re

authors = "['/Yazar/daron-acemoglu/s=8100', '/Yazar/james-robinson/s=35496']"
authorIds = re.findall("[0-9]+", str(authors))

authorNames = [' Daron Acemoğlu  ,', ' James Robinson  ']
#authorNames = authorNames2.replace(',', '')
tempAuthors = []

for id, name in zip(authorIds, authorNames):
    tempAuthors.append({"aId": id, "aName": name.replace(',', '').strip()})

print(tempAuthors)


