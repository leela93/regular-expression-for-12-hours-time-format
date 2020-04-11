# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 11:34:00 2020

@author: leela
"""
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"

index = log.index("[")
print(log[index+1:index+6])
#%%
import re
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])
#%%
import re

def check_aei(text):
    result = re.search(r"a.e.i", text)
    return result != None

print(check_aei("academia"))
#%%
print(re.search(r"Py.*n","Pygmalion"))
#%%
import re
def check_time(text):
  pattern = r"^(1[0-2]|[1-9])+:+([0-5]?[0-9])(\s?[A|P]M|[a|p]m)$"
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:02km")) # False
print(check_time("five o'clock")) # False
#%%
import re
def contains_acronym(text):
  pattern = r"\([A-Z]|[0-9]+[A-Z]|[a-z]\)"
  result = re.search(pattern, text)
  return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True