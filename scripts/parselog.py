#!/usr/bin/python3

import yaml
import json

dumpme = {"errorips": []}

## open files /log.example
with open ("/home/student/ans/files/log.example") as lef:
   for line in lef:
       if "ERROR" in line:
           loggedip = line.split()[1]
           dumpme["errorips"].append(loggedip)

#print(json.dumps(dumpme))
with open ("/home/student/ans/files/parsed.ips", "w") as iif:
    iif.write(yaml.dump(dumpme))


## parse files /log.example for ERROR and collect second items in the line 
## store in dictionary  {'errorips': [list of ips]}

## dump (print) collected IPs out as Json 
