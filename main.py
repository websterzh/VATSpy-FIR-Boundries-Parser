#!/usr/bin/python3
import json
import re

# Config
INPUT_FILE = './FIRBoundaries.dat'
OUTPUT_FILE = './out.json'
INDENT = 2 # None or specify a number

# Input
with open(INPUT_FILE) as f:
    fileContent = f.readlines()
    
# Init
firSet = []
currentFir = {}
currentFirPoints = []

# Check file content
for line in (fileContent):
    elem = re.split(r'\|', line.strip())
    if (len(elem) > 2):
        # Definition of FIR
        if (len(currentFirPoints) > 0):
            currentFir = {
                "ident": currentFir["ident"],
                "boundaries": currentFirPoints
            }
            firSet.append(currentFir)
            currentFirPoints = []
        currentFir = {
            "ident": elem[0],
            "boundaries": None
        }
    else:
        # Just a waypoint
        waypoint = {
            "lat": elem[0],
            "lon": elem[1]
        }
        currentFirPoints.append(waypoint)

# Add the last one
currentFir = {
    "ident": currentFir["ident"],
    "boundaries": currentFirPoints
}
firSet.append(currentFir)

# Output
with open(OUTPUT_FILE, 'w') as f:
    f.write(json.dumps(firSet, indent=INDENT))
