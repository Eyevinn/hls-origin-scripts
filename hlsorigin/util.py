import re

def isValidTimestamp(ts):
    if ts == None:
        return False
   
    res = re.match('\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d', ts) 
    if not res:
        return False

    return True
