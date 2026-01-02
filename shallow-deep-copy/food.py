
from copy import copy

from copy import deepcopy

arun_fvt_foods=[
    ["dosa","tea"], #0
    ["meals","lime juice"],
    ["chapthy","lime tea"]
]


resin_fvt_food=deepcopy(arun_fvt_foods)

resin_fvt_food[0][0]="idly"

print("Arun",arun_fvt_foods)

print("Resin",resin_fvt_food)