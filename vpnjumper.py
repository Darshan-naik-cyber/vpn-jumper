#!/usr/bin/env python3

import os
from time import sleep
import random 

codeList = ["TR","US-C","DE","CH","FR","US"]

try:
  os.system("windscribe connect")
  while True:
    codeChoice = random.choice(codeList)
    sleep(random.randrange(12,30))
    print("Changing IP Address")
    os.system("windscribe connect " + codeChoice)

except:
  os.system("windsrcribe disconnect")
  print("Error Occured")
