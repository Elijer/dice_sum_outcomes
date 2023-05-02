from itertools import permutations, combinations_with_replacement
from plays_possible_2 import possible_plays

sides = [x for x in range(1, 7)]
rolls = [x for x in combinations_with_replacement(sides, 4)]
plays = []

for r in rolls:
  plays = plays + possible_plays(r)
  
occ = {n: 0 for n in range(1, 14)}
for p in plays:
  if (p < 14):
    occ[p] = occ[p] + 1

check = 0 
for o in occ.values():
  prob = o/len(plays)
  check = check + prob
  print(f"={o}/{len(plays)}")

print(f"total possibilities are: {len(plays)}")
    
    
# check = 0 
# for o in occ.values():
#   prob = o/len(plays)
#   check = check + prob
#   print(f"={o}/{len(plays)}")
#   # print(prob)
  
# # print(check)
  

# plays = []
# for r in rolls:
#   plays = plays + possible_plays(r)

# occ = {n: 0 for n in range(1, 14)}
# for p in plays:
#   if p < 14:
#     occ[p] = occ[p] + 1
#   # occ[r] = occ[r] + 1
  
# check = 0 
# for o in occ.values():
#   prob = o/len(plays)
#   check = check + prob
#   print(f"={o}/{len(plays)}")
#   # print(prob)
  
# # print(check)