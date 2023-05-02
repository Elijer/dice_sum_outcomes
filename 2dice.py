sides = [x for x in range(1, 7)]

rolls = []

for a in sides:
  for b in sides:
    rolls.append(a)
    rolls.append(b)
    rolls.append(a+b)
    
    
occ = {n: 0 for n in range(1, 14)}
  
for r in rolls:
  occ[r] = occ[r] + 1
  
for o in occ.values():
  if o == 0:
    print(0)
  else:
    print(o/len(rolls))
    
print(f"total possibilities are: {len(rolls)}")
